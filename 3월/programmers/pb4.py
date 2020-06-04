def findnum(n):
    global d
    if d.get(n):
        num = d.get(n)
        if num > 0:
            if d.get(n+num):
                while d.get(n+num):
                    d[n] += d.get(n+num)
                    t = n+num
                    num += d.get(n+num)
                    d[t] = -n
                tmp = d[n]
                d[n] += 1
            else:
                tmp = d[n]
                d[n] += 1
            return n+tmp
        else:
            while num < 0:
                v = -num
                num = d.get(v)
            return findnum(v + num)
    else:
        d[n] = 1
        return n

def solution(k, room_number):
    global d
    answer = []
    d = dict()
    for fn in room_number:
        answer.append(findnum(fn))
        # print(answer)
    return answer


print(solution(10, [2, 3, 4, 2, 2, 2, 4]))
