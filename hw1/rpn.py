# TODO add error checking on inputs and calculations
#   divide by 0 - leave the bois on the stack
#   find how to check for EOF (ctrl+d)

calc = []

while (True):
    try:
        line = input()
    except EOFError:
        exit(0)

    if line.isdigit():
        print(line)
        calc.append(float(line))
    elif line == '+':
        if len(calc) <= 1:
            print("invalid operation")
            continue
        var1 = calc.pop()
        var2 = calc.pop()
        result = var1+var2
        print(result)
        calc.append(result)
    elif line == '-':
        if len(calc) <= 1:
            print("invalid operation")
            continue
        var1 = calc.pop()
        var2 = calc.pop()
        result = var2-var1
        print(result)
        calc.append(result)
    elif line == '*':
        if len(calc) <= 1:
            print("invalid operation")
            continue
        var1 = calc.pop()
        var2 = calc.pop()
        result = var1*var2
        print(result)
        calc.append(result)
    elif line == '/':
        if len(calc) <= 1:
            print("invalid operation")
            continue
        var1 = calc.pop()
        var2 = calc.pop()
        if var1 == 0:
            print("error: division by zero")
            calc.append(var2)
            calc.append(var1)
        else:
            result = float(var2)/float(var1)
            print(result)
            calc.append(result)
    elif line == '~':
        if len(calc) == 1:
            print("invalid operation")
            continue
        var1 = calc.pop()
        result = var1 * -1
        print(result)
        calc.append(result)