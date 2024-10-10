from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(*args):
    return sum(int(a) for a in args)

def subtract_numbers(a, *args):
    result = int(a)
    for num in args:
        result -= int(num)
    return result

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= int(num)
    return result

def divide_numbers(a, *args):
    result = int(a)
    for num in args:
        if int(num) == 0:
            raise ValueError("Cannot divide by 0.")
        result /= int(num)
    return result

server = SimpleXMLRPCServer(('localhost', 9000))
print("Listening on port 9000...")
server.register_function(add_numbers, 'add')
server.register_function(subtract_numbers, 'subtract')
server.register_function(multiply_numbers, 'multiply')
server.register_function(divide_numbers, 'divide')

server.serve_forever()