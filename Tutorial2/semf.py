import numpy as np

# EB = av*A − as*(A^2/3) − aA*((A-2*Z)^2)/A − ac*(Z^2)/(A^1/3) + ap/(A^3/4) 

# be - a = 10, z = 4
b1 = 10
b2 = - np.math.pow(10,2/3)
b3 = - np.math.pow(10-(2*4),2)/10
b4 = - np.math.pow(4,2)/np.math.pow(10,1/3)
b5 = 1/np.math.pow(10,3/4)

# c - a = 14, z = 6
c1 = 14
c2 = - np.math.pow(14,2/3)
c3 = - np.math.pow(14-(2*6),2)/14
c4 = - np.math.pow(6,2)/np.math.pow(14,1/3)
c5 = 1/np.math.pow(14,3/4)

# o - a = 18, z = 8
o1 = 18
o2 = - np.math.pow(18,2/3)
o3 = - np.math.pow(18-(2*8),2)/18
o4 = - np.math.pow(8,2)/np.math.pow(18,1/3)
o5 = 1/np.math.pow(18,3/4)

# mg - a = 26, z = 12
m1 = 26
m2 = - np.math.pow(26,2/3)
m3 = - np.math.pow(26-(2*12),2)/26
m4 = - np.math.pow(12,2)/np.math.pow(26,1/3)
m5 = 1/np.math.pow(26,3/4)

# si - a = 30, z = 14
s1 = 30
s2 = - np.math.pow(30,2/3)
s3 = - np.math.pow(30-(2*14),2)/30
s4 = - np.math.pow(14,2)/np.math.pow(30,1/3)
s5 = 1/np.math.pow(30,3/4)

A = np.array([[b1,b2,b3,b4,b5],[c1,c2,c3,c4,c5],[o1,o2,o3,o4,o5],[m1,m2,m3,m4,m5],[s1,s2,s3,s4,s5]])
b = np.array([6.489, 7.520, 7.767, 8.334, 8.521])
val = np.linalg.solve(A,b)
print(val)

'''
import numpy as np

# EB = av*A − as*(A^2/3) − aA*((A-2*Z)^2)/A − ac*(Z^2)/(A^1/3) + ap/(A^3/4)

# be - a = 10, z = 4
b1 = 10
b2 = - np.math.pow(10,2/3)
b3 = - np.math.pow(10-(2*4),2)/10
b4 = - np.math.pow(4,2)/np.math.pow(10,1/3)
b5 = 1/np.math.pow(10,3/4)

# c - a = 14, z = 6
c1 = 14
c2 = - np.math.pow(14,2/3)
c3 = - np.math.pow(14-(2*6),2)/14
c4 = - np.math.pow(6,2)/np.math.pow(14,1/3)
c5 = 1/np.math.pow(14,3/4)

# o - a = 18, z = 8
o1 = 18
o2 = - np.math.pow(18,2/3)
o3 = - np.math.pow(18-(2*8),2)/18
o4 = - np.math.pow(8,2)/np.math.pow(18,1/3)
o5 = 1/np.math.pow(18,3/4)

# mg - a = 26, z = 12
m1 = 26
m2 = - np.math.pow(26,2/3)
m3 = - np.math.pow(26-(2*12),2)/26
m4 = - np.math.pow(12,2)/np.math.pow(26,1/3)
m5 = 1/np.math.pow(26,3/4)

# si - a = 30, z = 14
s1 = 30
s2 = - np.math.pow(30,2/3)
s3 = - np.math.pow(30-(2*14),2)/30
s4 = - np.math.pow(14,2)/np.math.pow(30,1/3)
s5 = 1/np.math.pow(30,3/4)

A = np.array([[b1,b2,b3,b4,b5],[c1,c2,c3,c4,c5],[o1,o2,o3,o4,o5],[m1,m2,m3,m4,m5],[s1,s2,s3,s4,s5]])
b = np.array([6.489, 7.520, 7.767, 8.334, 8.521])
z = np.linalg.solve(A,b)
print(z)
'''
