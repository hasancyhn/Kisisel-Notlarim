def usalma(number):
    def inner(power):
        return number ** power
    return inner
two = usalma(2) # 2-3
print(two(3))