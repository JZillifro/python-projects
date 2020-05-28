seen ={}

def collatz(n):
    if n == 1:
        return 1
    res = 0
    while(n != 1):
        if n in seen:
            return res + seen[n]
        if n%2 :
            n = n*3 +1
        else:
            n = n/2
        res+=1
    seen[n] = res
    return res

def max_collatz(n):
    max_n = 0
    max_c = 0
    for i in reversed(range(1,n+1)):
        c = collatz(i)
        print(i, c)
        if c > max_c:
            max_n = i
            max_c = c
    return max_n, max_c

def collatz_finder(k):
    return collatz_finder_helper(1, k, 0)

def collatz_finder_helper(n, k, l):
    if l == k:
        return [n]
    return collatz_finder_helper(n*2, k, l+1) + collatz_finder_helper((n-1)/3, k, l+1)

print(collatz_finder(5))

from collections import Counter
def a(s1, s2):
    return Counter(s1) == Counter(s2)