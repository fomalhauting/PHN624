# j = 3/2  gpl = 1  gnl = 0  gps = 5.585
# 7Li
a = int(input())
j = int(input())
gpl = 1
gnl = 0
gps = 5.585

r_sq = (3/5)*(1.2*(a**1/3))**2
Q_sp = -((2*j-1)/(2*(j+1)))*r_sq

# j = l + 1/2
u = (j-1/2)*gpl + (1/2)*gps
Q = Q_sp/100

print(Q, u)
