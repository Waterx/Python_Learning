from math import sqrt


def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    else:
        return True


def noprime(no): # This function is to get the no. prime
    count = 0
    num = 2
    while count != no:
        if prime(num):
            count = count + 1
            if count == no:
                return num
            else:
                num = num + 1
        else:
            num = num + 1


def monisen(no):
    count = 0
    nop = 1
    while count != no:
        m = 2 ** noprime(nop) - 1
        if prime(m):
            count = count + 1
            if count == no:
                return m
            else:
                nop = nop + 1
        else:
            nop = nop + 1


print(monisen(int(input())))
