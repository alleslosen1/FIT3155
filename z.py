
def z_algo(s):
    z = [0] * (len(s))
    l, r = 0, 0

    for k in range(1, len(s)):
        if k > r:
            q = k
            start = 0
            while s[q] == s[start]:
                z[k] += 1
                start += 1
                q += 1
            else:
                if z[k] > 0:
                    r = q-1
                    l = k
        
        elif k <= r:
            if z[k-l] < r-k+1:
                z[k] = z[k-l]
            elif z[k-l] >= r-k+1:
                q = r+1
                start = r-k+1
                while s[q] == s[start]:
                    start += 1
                    q += 1
                else:
                    z[k] = q-k
                    l = k
                    r = q-1
    return z

s = 'aabcaabxaabcaabcay'
print(z_algo(s))