#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    total_sum = add(a, b)
    total_sub = sub(a, b)
    total_mul = mul(a, b)
    total_div = div(a, b)

    print("{} + {} = {}".format(a, b, total_sum))
    print("{} - {} = {}".format(a, b, total_sub))
    print("{} * {} = {}".format(a, b, total_mul))
    print("{} / {} = {}".format(a, b, total_div))
