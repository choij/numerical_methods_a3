import csv
import numpy as np

def getBH():
  b = []
  h = []
  with open('bhm19.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      b.append(float(row[0]))
      h.append(float(row[1]))
  f.close()
  return b,h

def getFj( bool_Fj , X, x0 ):
  Fj = np.empty([len(X)],dtype='float64')
  Fj[:]=1
  #x_0=0;
  #if bool_Fj == 0:
  #  x_0 = x0
  #else:
  #  x_1 = X[i]
  for i in range (len(X)):
    if bool_Fj == 0:
      x_0 = x0
    else:
      x_0 = X[i]
    Fj[i] = 1
    for j in range (len(X)):
      if (j==i):
        pass
      else:
        Fj[i] *= (x_0-X[j]) 
  #elif bool_Fj == 1:
  #  for i in range (len(X)):
  #    for j in range (len(X)):
  #      if (j==i):
  #        pass
  #      else:
  #        #Fj[i] += str(i)+str(j)
  #        Fj[i] *= (X[i]-X[j]) 
  return Fj

def getY( L, a ):
  y = 0
  for i in range (len(L)):
    y += a[i]*L[i]
  return y

def lagrange_polynomial(B,h,x0):
  Fj_num = getFj ( 0, B, x0 )
  Fj_den = getFj ( 1, B, 0 )
  Lj = [ Fj_num[i]/Fj_den[i] for i in range (len(Fj_num)) ]
  return getY ( Lj, h )

def interpolatePartA():
  B = getBH()[0][0:6]
  h = getBH()[1][0:6]
  y = [ lagrange_polynomial(B,h,x0) for x0 in B ]
  return y

def interpolatePartB():
  B = getBH()[0]
  h = getBH()[1]
  del B[1:8]
  del h[1:8]
  del B[3:5]
  del h[3:5]

  y = [ lagrange_polynomial(B,h,x0) for x0 in B ]
  return y

if __name__ == "__main__":
  print interpolatePartA() 
  print interpolatePartB() 
