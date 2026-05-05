import math
def prime_factorization_optimized(n):
    factors = []
    divisor = 2
    while divisor <= math.sqrt(n):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors
number = int(input("请输入一个整数: "))
result = prime_factorization_optimized(number)
result_str = '*'.join(map(str, result))
print("改整数的因式分解为:", result_str)