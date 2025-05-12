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

def main():
    while True:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            op = input("Введите операцию (+, -, *, /): ")
            result = calculate(a, b, op)
            print(f"Результат: {result}")
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

if name == "main":
    main()