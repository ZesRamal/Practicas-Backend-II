import xmlrpc.client
import re

def calculate(expression):
    proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
    tokens = re.findall(r'(\d+|[+\-*/])', expression)
    numbers = []
    operators = []

    for token in tokens:
        if token.isdigit():
            numbers.append(int(token))
        else:
            operators.append(token)
    while '*' in operators or '/' in operators:
        for i, op in enumerate(operators):
            if op == '*':
                result = proxy.multiply(numbers[i], numbers[i + 1])
                numbers[i] = result
                numbers.pop(i + 1)
                operators.pop(i)
                break
            elif op == '/':
                result = proxy.divide(numbers[i], numbers[i + 1])
                numbers[i] = result
                numbers.pop(i + 1)
                operators.pop(i)
                break
    while '+' in operators or '-' in operators:
        for i, op in enumerate(operators):
            if op == '+':
                result = proxy.add(numbers[i], numbers[i + 1])
                numbers[i] = result
                numbers.pop(i + 1)
                operators.pop(i)
                break
            elif op == '-':
                result = proxy.subtract(numbers[i], numbers[i + 1])
                numbers[i] = result
                numbers.pop(i + 1)
                operators.pop(i)
                break
    return numbers[0]

expression = input("Enter an expression (e.g., 3+2-1*4): ")
result = calculate(expression)
print("Result of", expression, "is:", result)
