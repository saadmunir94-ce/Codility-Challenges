import math


def pal_detector(num):
    orig = num
    is_neg = False
    if num < 0:
        num *= -1
        is_neg = True
    elif num == 0:
        return 0
    n = math.floor(math.log10(num))
    reversed = 0
    while num > 0:
        remainder = num % 10
        reversed += remainder * 10 ** n
        num = num // 10
        n -= 1
    if is_neg:
        reversed *= -1
    return True if orig == reversed else False


nums = [121, 0, -1, -876, -87, 1891, 747, 1890]
reverses = []

for no in nums:
    reverses.append(pal_detector(no))
print(reverses)
is_run = False

def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1

if is_run:
    for i in infinite_seq():
        if pal_detector(i):
            print(f"{i} is palindrome")
