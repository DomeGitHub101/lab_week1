def plus(x):
    if x > 9 or x < 0:
        return "Invalid"
    xx = x*11
    xxx = x*111
    xxxx = x*1111
    y = x+xx+xxx+xxxx
    return y


value = int(input())
output = plus(value)
print(output)