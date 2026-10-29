# Echauffement 1 

import math
class Point: 

    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

    def norm(self):
        return math.sqrt(self.x**2+self.y**2)

    def __repr__(self):
        return f"Point{(self.x,self.y)}"


# try:
#     p = Point(3, 4)
#     assert (p.x, p.y) == (3, 4)
#     assert p.norm() == 5.0
#     assert repr(p) == "Point(3, 4)"
#     q = Point(0, 1)
#     assert (q.x, p.x) == (0, 3)
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


#Réponses : 
# 1. p.norm() et Point.norm(p) donnent bien le même résultat (5.0)
# 2. Sans mettre self dans norm(), on a une erreur d'arguments donnés lorsqu'on appelle p.norm()
# 3. Sans __repr__, il nous renvoie <__main__.Point object at 0x10438ffd0> 

# Échaufement 3 : 

#Le code devrait afficher une liste '[1]' car on a lié a et b par Bad()

class Bad:
    def __init__(self):
        self.items = []

    def add(self, x):
        self.items.append(x)

a, b = Bad(), Bad()
a.add(1)
print(b.items)

#Réponses : 
# 1. a et b sont reliés comme attribut dans la class de Bad 
# 2. il faut rajouter une initialisation à Bad()

# Échauffement 4 

class Tirelire: 
    def __init__(self):
        self.items=[]

    def deposit(self,value:float):
        if value<=0:
            raise ValueError
        else : 
            self.items.append(value)
        return self.items

    def total(self):
        S=0
        for p in self.items:
            S+=p
        return S

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Tirelire({len(self)} coins, total={Tirelire.total(self):.2f})" # .2f force Python à afficher 2 chiffres après la virgule


# t = Tirelire()
# t.deposit(0.5)
# t.deposit(-1)


