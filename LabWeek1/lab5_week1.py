def find_min_number(nums):
    x = nums.split()
    if len(x) > 10 or len(x) == 1:
        return "Invalid"
    for i in x:
        if not i.isdigit() or int(i)>9:
            return "Invalid"

    x = list(map(int, x))
    x.sort()

    if x[0] == 0:
        for i in range(1, len(x)):
            if x[i] != 0: 
                x[0], x[i] = x[i], x[0]
                break

    return ''.join(map(str, x))

nums = input()
output = find_min_number(nums)
print(output)
