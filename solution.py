def answer(n):
    nxt = 0
    n = bin(int(n))[2:]
    length = len(n)
    count = length-1
    
    for i in xrange(length-1,0,-1):
        if n[i] == '1' and nxt == 0:
            count += 1
            if i > 1 and n[i-1] == '1':
                nxt = 1
        elif n[i] == '0' and nxt == 1:
            count += 1
            if i == 1 or n[i-1] == '0':
                nxt = 0
    return count + nxt