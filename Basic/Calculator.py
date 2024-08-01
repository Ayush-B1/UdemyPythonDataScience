from calculatorart import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number: "))

operation_perform = input("which operation do you want to perform '+' for add, '-' for subtract, '*' for multiply, '/' for divide: ")

num2 = int(input("What is the second number: "))


function = operations[operation_perform]
ans = function(num1, num2)

print(f"{num1} {operation_perform} {num2} = {ans}")