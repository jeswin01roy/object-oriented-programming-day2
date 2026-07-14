class student:
    def __init__(self):
        pass
    def hello(self):
        print(" i say hallo")
    def interest(self,roi,rs):
        monthlyint=(roi*rs*.01)/12
        return monthlyint

s1=student()
s1.hello()
print(s1.interest(12.5,100000))