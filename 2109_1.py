
def qwer(n):
    if n < 8:
        return [n]
    return qwer(n // 8)+[n % 8]




#1) вывести 1 разряд
#2) вызвать эту функцию со всем кроме 1 разряда

print(qwer(78345))
print(qwer(89546))
