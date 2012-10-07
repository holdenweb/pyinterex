#
# Sample file to be executed interactively, producing a playerpiano script
#
a = 1
b = 2
a + 3
("this is a"
" single string")
for i in  1, 2, 3:
    print i

def f(x):
    return x+x

class ListCreator(object): # new-style class
    def __init__(self, ct):
        self.ct = ct
    def listof(self, val):
        return [val for x in range(self.ct)]

creator = ListCreator(3)
creator.listof(None)
f(creator.listof(None))

("just "
"checking")
