def calculate(a, b, op):
    if op == '+': return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
    return a / b

    else:
        raise ValueError("Неверная операция")