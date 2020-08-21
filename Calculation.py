# operation = input()
# a = int(input())
# b = int(input())
#
#
# def calculate(a, b, operation):
#     if operation == 'multiply':
#         return a * b
#     elif operation == 'divide':
#         return a // b
#     elif operation == 'add':
#         return a + b
#     elif operation == 'subtract':
#         return a - b
#
#
# print(calculate(a, b, operation))


operation = input()
a = int(input())
b = int(input())


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def execute(a, b, operation):
    mapping = [
        ['multiply', multiply],
        ['divide', divide],
        ['add', add],
        ['subtract', subtract],
    ]
    for operation_name, i in mapping:
        if operation_name == operation:
            return i(a, b)

print(execute(a, b, operation))