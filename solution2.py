def sum_of_divisors(n):
    print(n)
    i = 1
    result = 0
    while i <= n:
        if n % i == 0:
            result += i
    return result

print ("dasad")
print (sum_of_divisors(8))
print (sum_of_divisors(7))
print (sum_of_divisors(1))
print (sum_of_divisors(1000))
