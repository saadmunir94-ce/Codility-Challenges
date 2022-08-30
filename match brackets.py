def match_brackets(A):
    stack = []
    for i in A:
        if i == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return 0
        elif i == "}":
            if len(stack) == 0 or stack.pop() != "{":
                return 0
        elif i == "]":
            if len(stack) == 0 or stack.pop() != "[":
                return 0
        elif i == "(" or i == "{" or i  == "[":
            stack.append(i)
    return 1

A = ["[9+{4-(6/2)}]",
    "[9+{4-(6/2)}]]"]
for el in A:
    print(match_brackets(el))
