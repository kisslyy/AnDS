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

text = input("Введите строку: ")
if check_brackets(text):
    print("Строка существует")
else:
    print("Строка не существует")