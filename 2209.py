def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fac(n-1) * n


print(fac(8))

def f(n, dv=1, all_dv=[]):
    if dv == n:
        all_dv.append(dv)
        return all_dv
    elif dv<n:
        if n%dv == 0:
            all_dv.append(dv)
        return f(n,dv=dv+1,all_dv=all_dv)
    else:
        print('mnbv')

print(f(735,dv=1,all_dv=[]))

def ord(n):
    if n < 10:
        return [n]
    return ord(n // 10)+[n % 10]

print(ord(628)) 
