>>> #
>>> # Sample file to be executed interactively, producing a playerpiano script
>>> #
>>> a = 1
>>> b = 2
>>> a + 3
4
>>> ("this is a"
... " single string")
'this is a single string'
>>> for i in  1, 2, 3:
...     print i
... 
1
2
3
>>> def f(x):
...     return x+x
... 
>>> class AnyOld(object): # new-style class
...     def __init__(self, ct):
...         self.ct = ct
...     def listof(self, val):
...         print range(self.ct)
...         return [val for x in range(self.ct)]
... 
>>> anyold = AnyOld(3)
>>> f(anyold.listof(None))
[0, 1, 2]
[None, None, None, None, None, None]
>>> 
>>> ("just "
... "checking")
'just checking'
