class person1:
    def __init__(self):
        pass
    def walk(self):
        print("person can walk")
    def smile(self):
        print("person can smile hahaha")
    def speak(self):
        print("person1 can speak")

class person2():
    def __init__(self):
        pass
    def read(self):
        print("person can read")
    def write(self):
        print("person can write")
    def speak(self):
        print("person2 can speak")

class person3():
    def __init__(self):
        pass
    def fly(self):
        print("person can fly")
    def swim(self):
        print("person can swim")
    def speak(self):
        print("person3 can speak")

class person4(person1,person2,person3):
    def __init__(self):
        pass
    def sleep(self):
        print("person can sleep")
    def eat(self):
        print("person can eat")
    def speak(self):
        print("person4 can speak")
        super().speak()


p = person4()     
p.fly()
p.speak()

