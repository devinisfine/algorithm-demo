import sys
while True:
    try:
        num = int(sys.stdin.readline().strip())
        for i in range(num):
            s = sys.stdin.readline().strip()
            s = list(s)
            k = 0
            for i in range(len(s)):
                s[k]=s[i]
                k = k+1
                if k>=3 and s[k-1]==s[k-2] and s[k-2]==s[k-3]:
                    k = k-1
                if k>=4 and s[k-2]==s[k-1] and s[k-4]==s[k-3]:
                    k = k-1
            res = s[0:k]
            print(res)
    except:
        break
# helllo -> hello, aabbcc->aabcc