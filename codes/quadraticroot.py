import cmath


def quadratic_root(a,b,c):
  x1 = (-b+cmath.sqrt(b^2-4*a*c))/(2*a)
  x2 = (-b-cmath.sqrt(b^2-4*a*c))/(2*a)
  
  
  if x1 == x2:
    return x1
  else:
    return x1,x2

#print(quadratic_root(1,0,-4))
#print(quadratic_root(1,3,2))
#print(quadratic_root(1,2,5))