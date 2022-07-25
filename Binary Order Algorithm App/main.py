from B_O_algorythm import sorting
import numpy as np

# = np.array([("Ma","p1","p2","p3","p4","p5","p6","p7","p8","999"),("A",1,1,0,0,1,0,0,0,0),("B",0,0,1,0,0,0,0,1,0),("C",0,1,1,0,0,1,1,0,0),("D",0,0,0,1,0,0,0,1,0),("E",0,0,1,1,0,1,1,0,0),("F",1,1,0,0,1,0,0,0,0),(999,0,0,0,0,0,0,0,0,0)])

def mainRun(x):

  c=x
  while True:
      b = sorting(x)
      if (b==x).all()==True:
          break
      else:
          x=b
  print(c)
  print("  ")
  print(b)
  return b

#mainRun(a)
