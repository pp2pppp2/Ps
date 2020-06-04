a, b = map(float, input().split())
c = (a+b)/(1+(a*b)/(300000 ** 2))
print('%.9f' %c)