
# write a pyhom program that calculate factoril of a number?

def factoril(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factoril(n-1)

n =int(input("plese Enter a number"))
result=factoril(n)
print(result)
