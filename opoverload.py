class student:
    def __init__(self,m1,m2):
        self.m1= m1
        self.m2= m2
    def __add__(self, other):
        return self.m1+other.m1,self.m2+other.m2
    def __sub__(self, other):
        return self.m1-other.m1,self.m2-other.m2
    def __mul__(self, other):
        return self.m1*other.m1,self.m2*other.m2
    def __truediv__(self, other):
        return self.m1/other.m1,self.m2/other.m2

s1=student(5,7)
s2=student(5,7)
print(s1+s2)
print(s2-s1)
print(s1*s2)
print(s2/s1)
