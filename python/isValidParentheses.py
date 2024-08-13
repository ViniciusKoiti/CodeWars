def isValidParentheses(s):
    stack = []  # Declaração de uma pilha usando lista
    opening = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif stack and char == opening[stack[-1]]:
            print(opening[stack[-1]])
            stack.pop() 
        else:
            return False
    
    return len(stack) == 0

examples = ["({[]})", "([)]", "((({[}])))", "({[[]]})"]
results = [isValidParentheses(example) for example in examples]

