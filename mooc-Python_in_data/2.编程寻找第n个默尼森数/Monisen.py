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


def monisen(no):
    count1 = 0
    count2 = 2
    (nop, nump) = (1, 2)  # no of P
    newnump = 2
    while count1 != no:
        m = 2**nump - 1
        if prime(m):
            if count1 == no:
                return m
            count1 = count1 + 1  # ??????
        else:
            while newnump == nump:
                count2 = count2 + 1
                if prime(count2):
                    newnump = count2
                    # break
            nop = nop + 1
            nump = newnump








print(monisen(int(input())))