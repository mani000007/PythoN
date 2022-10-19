#####STUDENT CLASS#####
class Student:
    lectures = []

    def getData(self, First_Name, Last_Name, Age, l1, l2, l3):
        Student.First_Name = First_Name
        Student.Last_Name = Last_Name
        Student.Age = Age
        Student.lectures.append(l1)
        Student.lectures.append(l2)
        Student.lectures.append(l3)

    def Display(self, New_Lectures=None):
        print(f"Student Name: {self.First_Name + self.Last_Name}")
        print(f"Age is:{self.Age}")
        print(f"Lectures he/she Attends: {self.lectures}")

    def Add_lctAndRemove(self, New_Lectures,Remv_lectures):
        Remv_lectures = Remv_lectures.split(" ")
        New_Lectures = New_Lectures.split(" ")
        for i in New_Lectures:
            Student.lectures.append(i)
        print(f"After Adding The New_Lectures:{self.lectures} ")
        for i in Remv_lectures:
            for j in Student.lectures:
                if i == j:
                    Student.lectures.remove(i)
        print(f"After Removing The Lecture:{self.lectures}")


fs = input("Enter The First_Name: ")
ls = input("Enter The Last_Name: ")
age = int(input("Enter the age: "))
ls1 = input("Enter l1: ")
ls2 = input("Enter l2: ")
ls3 = input("Enter l3: ")
nl = input("Enter the new_Lectures: ")
rml = input("Enter the Removal Lectures: ")

s = Student()
s.getData(fs, ls, age, ls1, ls2, ls3)
s.Display()
s.Add_lctAndRemove(nl,rml)



####OutPut####
Enter The First_Name: mani
Enter The Last_Name: kumar
Enter the age: 23
Enter l1: maths
Enter l2: physics
Enter l3: social
Enter the new_Lectures: computers java dbms
Enter the Removal Lectures: dbms
Student Name: manikumar
Age is:23
Lectures he/she Attends: ['maths', 'physics', 'social']
After Adding The New_Lectures:['maths', 'physics', 'social', 'computers', 'java', 'dbms'] 
After Removing The Lecture:['maths', 'physics', 'social', 'computers', 'java']
  
  
####Professor Class######



class Professor:
    Subjects = []

    def getData(self, First_Name, Last_Name, Age, s1, s2, s3):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Age = Age
        self.Subjects.append(s1)
        self.Subjects.append(s2)
        self.Subjects.append(s3)

    def Display(self):
        print(f"Student Name: {self.First_Name + self.Last_Name}")
        #print(f"Age is:{self.Age}")
        print(f"Subject he/she Teaches : {self.Subjects}")

    def Add_SubAndRemove(self, New_Sub, Remv_Sub):
        Remv_Sub = Remv_Sub.split(" ")
        New_Sub = New_Sub.split(" ")
        for i in New_Sub:
            self.Subjects.append(i)
        print(f"After Adding The New_Subjects: {self.Subjects} ")
        for i in Remv_Sub:
            for j in self.Subjects:
                   if i == j:
                       Professor.Subjects.remove(i)
        print(f"After Removing The Subjects:{self.Subjects}")


fn = input("Enter The First_Name: ")
ln = input("Enter The Last_Name: ")
a = int(input("Enter The age Of professor: "))
ls1 = input("Enter The Sub1: ")
ls2 = input("Enter The Sub2: ")
ls3 = input("Enter The Sub3: ")
ns = input("Enter The New_sub: ")
rm = input("Enter The Remove_Sub: ")
p=Professor()
p.getData(fn, ln, a, ls1, ls2, ls3)
p.Display()
p.Add_SubAndRemove(ns,rm)

#####OutPut#######

Enter The First_Name: mani
Enter The Last_Name: kumar
Enter The age Of professor: 54
Enter The Sub1: economics
Enter The Sub2: business
Enter The Sub3: accounts
Enter The New_sub: english
Enter The Remove_Sub: business
Student Name: manikumar
Subject he/she Teaches : ['economics', 'business', 'accounts']
After Adding The New_Subjects: ['economics', 'business', 'accounts', 'english'] 
After Removing The Subjects:['economics', 'accounts', 'english']