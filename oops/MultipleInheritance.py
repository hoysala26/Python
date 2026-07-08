class Flyable :
    def fly(self):
        print("flying")

class swin :
    def swin(self):
        print("swimming")

class duck (Flyable,swin):
    pass

d = duck()
d.fly()
d.swin()

