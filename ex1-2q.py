import math
class Abc:
    def Rectangle(self,l,b):
        p= 2*l+2*b
        a=l*b
        print(p, a)
    def Circle(self,r):
        p=2*3.14*r
        a=3.14*r*r
        print(p, a)
    def Triangle(self,a,b,c):
        z=a+b+c
        p=z/2
        a=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(z, a)

d=Abc()
d.Rectangle(5,10)
d.Circle(10)
d.Triangle(3,4,5)