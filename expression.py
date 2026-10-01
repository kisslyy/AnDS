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

def custom_eval(expr):
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        if expr[i].isspace():
            i += 1
            continue
        if expr[i].isdigit() or expr[i] == '.':
            val = ""
            while i < n and (expr[i].isdigit() or expr[i] == '.'):
                val += expr[i]
                i += 1
            tokens.append(float(val) if '.' in val else int(val))
            continue
        if expr[i] in "+-*/()":
            if expr[i] in "+-" and (not tokens or tokens[-1] in "+-*/("):
                tokens.append(0)
            tokens.append(expr[i])
            i += 1

    prec = {'+': 1, '-': 1, '*': 2, '/': 2}

    def process_op(values, operators):
        b = values.pop()
        a = values.pop()
        curr_op = operators.pop()
        if curr_op == '+':
            values.append(a + b)
        elif curr_op == '-':
            values.append(a - b)
        elif curr_op == '*':
            values.append(a * b)
        elif curr_op == '/':
            values.append(a / b)

    values = []
    ops = []

    for token in tokens:
        if isinstance(token, (int, float)):
            values.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                process_op(values, ops)
            ops.pop()
        elif token in prec:
            while ops and ops[-1] in prec and prec[ops[-1]] >= prec[token]:
                process_op(values, ops)
            ops.append(token)

    while ops:
        process_op(values, ops)

    return values[0]

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
        result = custom_eval(clean_expr)
        return f"Результат: {result}"
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception:
        return "Ошибка в синтаксисе выражения"

text = input("Введите выражение: ")
print(evaluate_expression(text))