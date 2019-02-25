n = int(input())
p = dict(input().split() for _ in range(n))
#print(p)

while True:
    try:
        s= input()
        #print(s)
        if s in p:
            print('%s=%s' % (s, p[s]))
        else:
            print('Not found')
    except:
        break


