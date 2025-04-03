"""
Goh Shu Jie
32694121
"""

import sys

def z_algo(txt, pat):
    s = pat + '$' + txt
    z = [0] * len(s)
    l, r = 0, 0

    for k in range(1, len(s)):
        # Case k > r
        if k > r:
            q = k
            start = 0
            while s[q] == s[start]:
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
                else:
                    z[k] = q - k
                    l = k
                    r = q - 1
    
    return z[len(pat) + 1:]


def find_matches(z, rz, txt, pat):
    matches = []
    for i in range(len(z)):
        # Check insert bounds
        if i+len(pat)-2 <= len(z):
            # Check insert
            if z[i] + rz[i+len(pat)-2] == len(pat)-1:
                matches.append((i, 1))
                print(i, 1)
                continue
        # Check delete bounds
        elif i+len(pat) <= len(z):
            # Check delete
            if z[i] + rz[i+len(pat)] == len(pat):
                matches.append((i, 1))
                print(i, 1)
        # Check sub bounds
        elif z[i] + rz[i+len(pat)-1] == len(pat)-1:
            matches.append((i, 1))
            print(i, 1)
        # Check swap
        elif pat[z[i]] == txt[z[i]+1] and pat[z[i]+1] == txt[z[i]]:
            matches.append((i, 1))
            print(i, 1)
        


def main():
    if len(sys.argv) != 3:
        print("Usage: python a1q1.py <text filename> <pattern filename>")
        sys.exit(1)

    text_file = sys.argv[1]
    pattern_file = sys.argv[2]

    with open(text_file, 'r') as f:
        text = f.read().strip()
    with open(pattern_file, 'r') as f:
        pattern = f.read().strip()

    z = z_algo(text, pattern)
    print(z)
    rz = z_algo(text[::-1], pattern[::-1])[::-1]
    print(rz)
    find_matches(z, rz, text, pattern)


    # with open('output_a1q1.txt', 'w') as f:
    #     for pos, dl in z:
    #         f.write(f"{pos} {dl}\n")

if __name__ == "__main__":
    main()