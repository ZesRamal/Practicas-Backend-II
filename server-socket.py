import socket
import threading
import sys
import os
import pickle

class Servidor():
    def __init__(self, host="localhost", port=7000):
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        # Threads for accepting and processing connections
        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)
        aceptar.daemon = True
        aceptar.start()
        procesar.daemon = True
        procesar.start()
        
        try:
            while True:
                msg = input('-> ')
                if msg == 'salir':
                    break
        finally:
            self.sock.close()
            sys.exit()

    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            if c != cliente:
                try:
                    c.send(msg)
                except:
                    self.clientes.remove(c)

    def aceptarCon(self):
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                print(f"Cliente {addr} conectado")
            except:
                pass

    def procesarCon(self):
        print("ProcesarCon iniciado")
        while True:
            if self.clientes:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            self.msg_to_all(data,c)
                            command = pickle.loads(data)
                            if command == "lsFiles":
                                self.list_files(c)
                            elif command.startswith("get "):
                                filename = command.split(" ", 1)[1]
                                self.send_file(c, filename)
                    except:
                        pass

    def list_files(self, client):
        files = os.listdir("Files")
        client.send(pickle.dumps(files))

    def send_file(self, client, filename):
        filepath = os.path.join("Files", filename)
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as f:
                file_data = f.read()
            client.send(pickle.dumps({"filename": filename, "data": file_data}))
        else:
            client.send(pickle.dumps({"error": "File not found"}))

server = Servidor()
