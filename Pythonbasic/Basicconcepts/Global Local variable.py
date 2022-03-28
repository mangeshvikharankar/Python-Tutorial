
a = 10

def demo():
    a = 9
    print("in fun",a)
    globals()['a'] =15

demo()
print("outside", a)