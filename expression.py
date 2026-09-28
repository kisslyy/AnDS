def check_brackets(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

def evaluate_expression(expr):
    if not expr.endswith('='):
        return "Ошибка: выражение должно заканчиваться на '='"

    clean_expr = expr[:-1].strip()

    if not check_brackets(clean_expr):
        return "Ошибка: неверная скобочная структура"

    allowed = "0123456789+-*/(). "
    for char in clean_expr:
        if char not in allowed:
            return "Ошибка: недопустимые символы в выражении"

    try:
        result = eval(clean_expr)
        return f"Результат: {result}"
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception:
        return "Ошибка в синтаксисе выражения"

text = input("Введите выражение: ")
print(evaluate_expression(text))