import numpy as np

def classic(a,b):
    MAX_DIGITS = max(len(a),len(b))
    product = [0] * (MAX_DIGITS * 2)

    for i in range(MAX_DIGITS):
        for j in range(MAX_DIGITS):
            product[i + j] += a[i] * b[j]
            product[i + j + 1] += product[i + j] // 10
            product[i + j] %= 10

    product_size = MAX_DIGITS * 2 - 1
    
    for i in range(product_size, -1, -1):
        print(product[i], end="")
    print()


def karatsuba(x, y):
    if (x == 0 or y == 0):
        return 0
    if (len(x) <= 1 or len(y) <= 1):
        return x[0] * y[0]
    else:
        mid = max(len(x),len(y)) // 2
        a = x[:mid] # left x
        b = x[mid:] # right x
        c = y[:mid] # left y
        d = y[mid:] # right y
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ab_sum = (np.array(a) + np.array(b)).tolist()
        cd_sum = (np.array(c) + np.array(d)).tolist()
        ad_plus_bc = karatsuba(ab_sum, cd_sum)-ac-bd

        return ac * (10 ** (2 * mid)) + (ad_plus_bc * (10 ** mid)) + bd
    
if __name__ == "__main__":
    x = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    y = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    print(karatsuba(x,y))
    classic(x,y)