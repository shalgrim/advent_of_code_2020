from file_ops import readlines


def calculate(left, operator, right):
    if operator == '+':
        return left + right
    else:
        return left * right


def evaluate(problem):
    items = problem.replace('(', ' ( ').replace(')', ' ) ').split()
    left = 0
    operator = '+'
    stack = []
    for item in items:
        try:
            right = int(item)
        except ValueError:
            if item  == '(':
                stack.append(left)
                stack.append(operator)
                left = 0
                operator = '+'
            elif item == ')':
                right = left
                operator = stack.pop()
                left = stack.pop()
                left = calculate(left, operator, right)
            else:
                operator = item
        else:
            left = calculate(left, operator, right)

    return left


if __name__ == '__main__':
    lines = readlines(18)
    values = [evaluate(line) for line in lines]
    print(sum(values))
