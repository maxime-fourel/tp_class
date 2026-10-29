# Echauffement 1 

import math
from collections import defaultdict

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


# pour tester : OK ! 

# try:
#     t = Tirelire()
#     t.deposit(0.5)
#     t.deposit(1)
#     assert len(t) == 2
#     assert t.total() == 1.5
#     assert repr(t) == "Tirelire(2 coins, total=1.50)"
#     other = Tirelire()
#     assert len(other) == 0
#     try:
#         other.deposit(-1)
#     except ValueError:
#         pass
#     else:
#         raise Exception("a negative value should raise ValueError")
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')



class Student: 
    def __init__(self, first_name:str, last_name:str):
        self.grades=defaultdict(list)
        self.first_name=first_name
        self.last_name=last_name

    def add_grade(self, course:str, grade:float):
        if grade>20 or grade<0:
            raise ValueError
        if course in self.grades.keys():
            self.grades[course].append(grade)
        else : 
            self.grades[course]=[grade]
        return self.grades

    def followed_topics(self):
        return list(self.grades.keys()) #Ceci permet d'éviter le problème d'ajout de matière que l'élève ne suit pas - en lien avec le compute_average

    def compute_average(self,course:str):
        
        if course in self.grades: 
            if len(self.grades[course])==0: #ici defaultdict va créer la clé associé à course 
                        raise ValueError
            else :
                S=0
                for note in self.grades[course]:
                    S+=note
                return S/len(self.grades[course])
        else: 
            raise ValueError   

    def report(self):
        L=[]
        L.append(f"Report for student {self.first_name} {self.last_name}")
        L.append("+===============+===============+")
        L.append(f"|     Topic     |    Average    |")
        L.append("+===============+===============+")
        for matiere in self.grades: 
            avg = self.compute_average(matiere)
            L.append(f"|{matiere:^15}|{avg:^15.2f}|")
            L.append("+---------------+---------------+")
        self.bulletin="\n".join(L)
        return self.bulletin

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, Grades: {self.grades})"

# pour tester : OK ! 

# try:
#     student = Student("Achille", "Talon")
#     r = repr(student)
#     assert isinstance(r, str), "__repr__ must return a str"
#     assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
# except Exception as e:
#     print('OOPS - There is an issue in your code.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


# try:
#     student = Student("Achille", "Talon")
#     student.add_grade("History", 10.)
#     student.add_grade("History", 12.)
#     try:
#         student.add_grade("History", 25.)
#     except ValueError:
#         pass
#     else:
#         raise Exception("a grade outside of [0, 20] should raise ValueError")
# except Exception as e:
#     print('OOPS - There is an issue in your add_grade method.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


# try:
#     student = Student("Achille", "Talon")
#     student.add_grade("History", 10.)
#     topics = student.followed_topics()
#     if len(topics) != 1 or "History" not in topics:
#         raise Exception(f"Expecting ['History'] got {topics}")
# except Exception as e:
#     print('OOPS - There is an issue in your followed_topics method')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


# try:
#     student = Student("Achille", "Talon")
#     student.add_grade("History", 10.)
#     student.add_grade("History", 12.)
#     if (student.compute_average("History") != 11.):
#         raise Exception("Issue in your average calculation.")
#     try:
#         student.compute_average("French")
#     except ValueError:
#         pass
#     else:
#         raise Exception("If topic is not followed, a ValueError is expected")
#     if student.followed_topics() != ["History"]:
#         raise Exception(f"asking for the average of an unfollowed topic must not create it: {student.followed_topics()}")
# except Exception as e:
#     print('OOPS - There is an issue in your compute_average method.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')



# try:
#     reference_lines = ['Report for student Albert Einstein',
#                        '+===============+===============+',
#                        '|     Topic     |    Average    |',
#                        '+===============+===============+',
#                        '|  Mathematics  |     12.80     |',
#                        '+---------------+---------------+',
#                        '|  Scubadiving  |     12.50     |',
#                        '+---------------+---------------+']

#     student = Student("Albert", "Einstein")
#     student.add_grade("Mathematics", 12.80)
#     student.add_grade("Scubadiving", 12.50)
#     report = student.report()
#     report_lines = report.strip().split('\n')
#     assert len(report_lines) == len(reference_lines), \
#         f"expected {len(reference_lines)} lines, got {len(report_lines)}"
#     for i, (lineref, linestudent) in enumerate(zip(reference_lines, report_lines), start=1):
#         assert lineref == linestudent, f"Ligne {i} : \n attendu = {lineref}\n  obtenu = {linestudent}"
# except AssertionError as e:
#     print("Les deux chaines sont différentes")
#     print(e)
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')




# class Classe:
#     def __init__(self,):
        

#     def add_student(self, student):
#         self.d={}
#         self.d[(self.first_name, self.last_name)]=student
#         return self.d

#     def __len__(self):
#         return len(self)

#     def __repr__(self):
#         return f"Class({self.classe}, Students :{list(self.d.values())}, Grades: {self.grades}"


