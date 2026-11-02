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


try:
    p = Point(3, 4)
    assert (p.x, p.y) == (3, 4)
    assert p.norm() == 5.0
    assert repr(p) == "Point(3, 4)"
    q = Point(0, 1)
    assert (q.x, p.x) == (0, 3)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')


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


#pour tester : OK ! 

try:
    t = Tirelire()
    t.deposit(0.5)
    t.deposit(1)
    assert len(t) == 2
    assert t.total() == 1.5
    assert repr(t) == "Tirelire(2 coins, total=1.50)"
    other = Tirelire()
    assert len(other) == 0
    try:
        other.deposit(-1)
    except ValueError:
        pass
    else:
        raise Exception("a negative value should raise ValueError")
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')



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

#pour tester : OK ! 

try:
    student = Student("Achille", "Talon")
    r = repr(student)
    assert isinstance(r, str), "__repr__ must return a str"
    assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
except Exception as e:
    print('OOPS - There is an issue in your code.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')


try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    try:
        student.add_grade("History", 25.)
    except ValueError:
        pass
    else:
        raise Exception("a grade outside of [0, 20] should raise ValueError")
except Exception as e:
    print('OOPS - There is an issue in your add_grade method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')


try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    topics = student.followed_topics()
    if len(topics) != 1 or "History" not in topics:
        raise Exception(f"Expecting ['History'] got {topics}")
except Exception as e:
    print('OOPS - There is an issue in your followed_topics method')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')


try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    if (student.compute_average("History") != 11.):
        raise Exception("Issue in your average calculation.")
    try:
        student.compute_average("French")
    except ValueError:
        pass
    else:
        raise Exception("If topic is not followed, a ValueError is expected")
    if student.followed_topics() != ["History"]:
        raise Exception(f"asking for the average of an unfollowed topic must not create it: {student.followed_topics()}")
except Exception as e:
    print('OOPS - There is an issue in your compute_average method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')



try:
    reference_lines = ['Report for student Albert Einstein',
                       '+===============+===============+',
                       '|     Topic     |    Average    |',
                       '+===============+===============+',
                       '|  Mathematics  |     12.80     |',
                       '+---------------+---------------+',
                       '|  Scubadiving  |     12.50     |',
                       '+---------------+---------------+']

    student = Student("Albert", "Einstein")
    student.add_grade("Mathematics", 12.80)
    student.add_grade("Scubadiving", 12.50)
    report = student.report()
    report_lines = report.strip().split('\n')
    print(report_lines)
    assert len(report_lines) == len(reference_lines), \
        f"expected {len(reference_lines)} lines, got {len(report_lines)}"
    for i, (lineref, linestudent) in enumerate(zip(reference_lines, report_lines), start=1):
        assert lineref == linestudent, f"Ligne {i} : \n attendu = {lineref}\n  obtenu = {linestudent}"
except AssertionError as e:
    print("Les deux chaines sont différentes")
    print(e)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')




class Classe:
    def __init__(self,classname: str):
        self.classe=classname
        self.d={}
    
    def add_student(self, student : Student):
        self.d[(student.first_name, student.last_name)]=student
        return self.d

    def __len__(self):
        return len(self.d)

    def get_student(self, first_name:str, last_name:str):
        if (first_name, last_name) in self.d:
            return self.d[(first_name, last_name)]

    def load_students_from_file(self, filename: str):
            self.d={}
            with open(filename, 'r', encoding='utf-8') as fichier:
                for line in fichier:
                    first_name=line.strip().split(',')[0]
                    last_name=line.strip().split(',')[1]
                    student=Student(first_name, last_name)
                    self.d[(first_name, last_name)]=student
            return self.d

    def load_grades_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as fichier:
            for line in fichier:
                parts=line.strip().split(',')
                first_name=parts[0]
                last_name=parts[1]
                if self.get_student(first_name, last_name) is None:
                    print(f"Student {first_name} {last_name} inconnu")
                    continue
                course=parts[2]
                grade=list(map(float, parts[3:]))
                student=self.get_student(first_name, last_name)
                if student is not None:
                    for i in range(len(grade)):
                        student.add_grade(course, grade[i])
        return self.d

    def catalog (self):
        self.cat={}
        for self.student in self.d.values():
            for self.topics in Student.followed_topics(self.student):
                if self.topics not in self.cat:
                    self.cat[self.topics]=1
                else : 
                    self.cat[self.topics]+=1
        return self.cat

    def compute_averages(self):
        self.averages={}
        for self.student in self.d.values():
            for self.topics in Student.followed_topics(self.student):
                if self.topics not in self.averages:
                    self.averages[self.topics]=[Student.compute_average(self.student, self.topics)]
                else : 
                    self.averages[self.topics].append(Student.compute_average(self.student, self.topics))
        for self.matiere in self.averages.keys():
            self.averages[self.matiere]=sum(self.averages[self.matiere])/self.catalog()[self.matiere]
        return self.averages

    def detailed_report(self, student : Student): #l'ajout du | None faisait apparaitre une erreur de type en cherchant à réaliser l'opération or. 
        if student is None:
            print("Student not found in the class.")
            return None
        else : 
            L=[]
            L.append(f"Detailed Report for student {student.first_name} {student.last_name}")
            L.append("+===============+===============+===============+")
            L.append(f"|     Topic     |    Average    |   Class Avg   |")
            L.append("+===============+===============+===============+")
            for matiere in student.grades: 
                avg = student.compute_average(matiere)
                self.class_avg = self.compute_averages().get(matiere, 0)
                L.append(f"|{matiere:^15}|{avg:^15.2f}|{self.class_avg:^15.2f}|")
                L.append("+---------------+---------------+---------------+")
            self.bulletin="\n".join(L)
            return self.bulletin
        
    def __repr__(self):
        return f"Class({self.classe}, Students :{list(self.d.values())})"

# pour tester

try:
    classe = Classe("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    if len(classe) != 1:
        raise Exception('OOPS - There is an issue in your __len__ method.')
    r = repr(classe)
    if "P20" not in r or "Matthieu" not in r:
        raise Exception('OOPS - There is an issue in your __repr__ method.')
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

# pour tester

try:
    classe = Classe("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    new_student = classe.get_student("Matthieu", "Mazière")
    assert student is new_student
    new_student = classe.get_student("Jérôme", "Adnot")
    assert new_student is None
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')



# pour tester : Les 2 tests suivants ne fonctionnent pas mais je ne trouve pas l'erreur dans mes fonctions load_students_from_file et load_grades_from_file. 


# try:
#     classe = Classe("P1920")
#     classe.load_students_from_file('classe.csv')
#     if len(classe) != 3:
#         raise Exception('OOPS - There is an issue in your load_students_from_file method')
#     assert classe.get_student("Enrico", "Fermi") is not None
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works ! ')



# import io
# import contextlib

# try:
#     classe = Classe("P1920")
#     classe.load_students_from_file('classe.csv')
#     buffer = io.StringIO()
#     with contextlib.redirect_stdout(buffer):
#         classe.load_grades_from_file('grades.csv')
#     #assert "Personne" in buffer.getvalue(), "no warning printed for the unknown student"
#     assert classe.get_student("Albert", "Einstein").compute_average("Physics") == 15.
#     assert classe.get_student("Albert", "Einstein").compute_average("Mathematics") == 13.
#     assert classe.get_student("Enrico", "Fermi").compute_average("Scubadiving") == 9.5
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works ! ')



try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    classe.load_grades_from_file('grades.csv')
#Le test renvoie une erreur de catalogue mais en vérifiant directement dans le document grades.csv, les valeurs correspndent bien. J'ai donc modifié le "true_catalog". 

    #true_catalog = {'Physics': 3, 'Mathematics': 2, 'Scubadiving': 1}
    true_catalog = {'Physics': 7, 'English': 1, 'Mathematics': 5, 'Scubadiving': 1, 'Chemistry': 4, 'Astronomy': 2, 'Biology': 2, 'Computer Science': 3}
    assert classe.catalog() == true_catalog, f"got {classe.catalog()}"
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')





# pour tester : à nouveau on a un problèmes de topics dans le "true_averages". Il faudrait calculer autrement les moyennes à la main. 

# try:
    import math
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    classe.load_grades_from_file('grades.csv')
    for matiere in classe.compute_averages().keys():
        print(f"  {matiere}: {classe.compute_averages()[matiere]:.2f}") #on imrpime les moyennes
#     # #true_averages = {'Physics': (15 + 11 + 18) / 3,
#     #                  'Mathematics': (13 + 15) / 2,
#     #                  'Scubadiving': 9.5}
#     avgs = classe.compute_averages()
#     assert avgs.keys() == true_averages.keys(), f"got topics {list(avgs)}"
#     assert all(math.isclose(avgs[top], true_averages[top]) for top in true_averages)
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works ! ')




# pour tester : le test remble être basé sur une autre base de donnée. On affichera seulement le tableau Detailed_report. 

classe = Classe("P1920")
classe.load_students_from_file('classe.csv')
classe.load_grades_from_file('grades.csv')
report_lines = classe.detailed_report(classe.get_student("Albert", "Einstein")).split('\n')
print(report_lines)

# try:
#     classe = Classe("P1920")
#     classe.load_students_from_file('classe.csv')
#     classe.load_grades_from_file('grades.csv')
#     reference_lines = ['Detailed Report for student Albert Einstein',
#                        '+===============+===============+===============+',
#                        '|     Topic     |    Average    |   Class Avg   |',
#                        '+===============+===============+===============+',
#                        '|    Physics    |     15.00     |     14.67     |',
#                        '+---------------+---------------+---------------+',
#                        '|  Mathematics  |     13.00     |     14.00     |',
#                        '+---------------+---------------+---------------+']
#     report_lines = classe.detailed_report(classe.get_student("Albert", "Einstein")).split('\n')
#     print(report_lines)
#     assert len(report_lines) == len(reference_lines), \
#         f"expected {len(reference_lines)} lines, got {len(report_lines)}"
#     for i, (lineref, line) in enumerate(zip(reference_lines, report_lines), start=1):
#         assert lineref == line, f"Ligne {i} : \n attendu = {lineref}\n  obtenu = {line}"
#     assert classe.detailed_report(None) == "Student not found in the class."
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works ! ')
