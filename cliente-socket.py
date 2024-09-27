import socket
import threading
import sys
import pickle
import os

class Cliente():
    def __init__(self, host="localhost", port=7000):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((str(host), int(port)))
            msg_recv = threading.Thread(target=self.msg_recv)
            msg_recv.daemon = True
            msg_recv.start()
            while True:
                msg = input('-> ')
                if msg != 'salir':
                    self.send_msg(msg)
                else:
                    self.sock.close()
                    sys.exit()
        except:
            print("Error al conectar el socket")

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    data = pickle.loads(data)
                    if isinstance(data, list):  # List of files
                        print("Archivos en el servidor:")
                        for filename in data:
                            print(filename)
                    elif isinstance(data, dict) and 'data' in data:  # File data
                        self.save_file(data['filename'], data['data'])
                    elif 'error' in data:  # Error message
                        print(data['error'])
                    elif data.startswith("get") == False:
                        print(data)
            except Exception as e:
                print(f"Error al recibir datos: {e}")
            finally:
                pass

    def send_msg(self, msg):
        try:
            self.sock.send(pickle.dumps(msg))
        except:
            print('Error al enviar mensaje')

    def save_file(self, filename, data):
        download_path = os.path.join("Downloads", filename)
        with open(download_path, 'wb') as f:
            f.write(data)
        print(f"Archivo '{filename}' guardado en 'Downloads'")

cliente = Cliente()