def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

def largest_palindrome(n):
    if(n.isalpha()):
        return "Invalid"
    if not(n.isalpha()):
        n = int(n)
    if(n<2 or n>3):
        return "Invalid"
    
    upper_limit = 10**n - 1  
    lower_limit = 10**(n - 1)
    max_palindrome = 0

    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product

    return max_palindrome

n = input()
result = largest_palindrome(n)
print(result)