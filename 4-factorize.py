def factorize(number):
    prime_factors = set()
    if number % 2 == 0:
        prime_factors.add(2)
    while number % 2 == 0:
        number = number // 2
        if number == 1:
            return prime_factors
    for factor in range(3, number + 1, 2):
        if number % factor == 0:
            prime_factors.add(factor)
            while number % factor == 0:
                number = number // factor
                if number == 1:
                    return prime_factors


input_number = 20
output = factorize(input_number)
print("Prime factors of {} are {}".format(input_number, output))
input_number = 1260
output = factorize(input_number)

print("Prime factors of {} are {}".format(input_number, output))
if factorize=="_main_":
    factorize