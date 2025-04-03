
def z_algo(s, pat):
    s = pat + '$' + s
    z = [0] * len(s)
    l, r = 0, 0
    print(s)

    for k in range(1, len(s)):
        # Case k > r
        if k > r:
            q = k
            start = 0
            while q < len(s) and s[q] == s[start]:
                z[k] += 1
                start += 1
                q += 1
            if z[k] > 0:
                r = q - 1
                l = k
        
        elif k <= r:
            # Case 2a
            if z[k - l] < r - k + 1:
                z[k] = z[k - l]
            # Case 2b
            else:
                q = r + 1
                start = r - k + 1
                while s[q] == s[start]:
                    start += 1
                    q += 1
                z[k] = q - k
                l = k
                r = q - 1
    
    return z[len(pat) + 2:]


print(z_algo('aabcaabxaabcaabcay', 'aabc'))