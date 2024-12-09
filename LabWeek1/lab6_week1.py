def max_product(value):
    try:
        if not (value.startswith('[') and value.endswith(']')):
            return "Invalid"

        lst = eval(value)

        if len(lst) < 2:
            return "Invalid"
        
        if all(x == 0 for x in lst):
            return "Invalid"

        lst.sort(reverse=True)
        return lst[0] * lst[1]
    

    except (SyntaxError, ValueError,NameError):
        return "Invalid"

value = input()
output = max_product(value)
print(output)
