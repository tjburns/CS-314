# TODO add error checking on inputs and calculations
#   divide by 0 - leave the bois on the stack
#   find how to check for EOF (ctrl+d)

calc = []

while (True):
    line = input()

    if line.isdigit():
        print(line)
        calc.append(int(line))
    elif line == '+':
        var1 = calc.pop()
        var2 = calc.pop()
        result = var1+var2
        print(result)
        calc.append(result)
    elif line == '-':
        var1 = calc.pop()
        var2 = calc.pop()
        result = var2-var1
        print(result)
        calc.append(result)
    elif line == '*':
        var1 = calc.pop()
        var2 = calc.pop()
        result = var1*var2
        print(result)
        calc.append(result)
    elif line == '/':

        # check for division by zero

        var1 = calc.pop()
        var2 = calc.pop()
        # potentially cast this to int
        result = float(var2)/float(var1)
        print(result)
        calc.append(result)
    elif line == '~':
        var1 = calc.pop()
        result = var1 * -1
        print(result)
        calc.append(result)