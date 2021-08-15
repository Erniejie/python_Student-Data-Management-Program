#python_Student Data Management Program
"Computer Programming Tutor,9th July 2021"

#1. Create Class Student

class Student:
    def __init__(self,name,rollno,score1,score2):
        self.name = name
        self.rollno = rollno
        self.score1 = score1
        self.score2 = score2

    #2.Function to Create and Append New Student

    def accept(self,Name,Rollno,marks1,marks2):
        ob = Student(Name,Rollno,marks1,marks2)
        ls.append(ob)

    #3.Function to Display Student Details:

    def display(self,stud):
            print("Name:",stud.name)
            print("RollNo:",stud.rollno)
            print("Marks1:",stud.score1)
            print("Marks2:",stud.score2)
            print("\n")

    #4. Search Function

    def search(self,rn):
        for k in range(ls.__len__()):
            if(ls[k].rollno == rn):
                return k
    #5.Delete Function

    def delete(self,sn):
        k = classstud.search(sn)
        del ls[k]

    #6.Update Function

    def update(self,sn,No):
        k = classstud.search(sn)
        roll = No
        ls[k].rollno = roll

#7. Create a List to Add Students

ls = []

# An Object of Student Class

classstud = Student("",0,0,0)

print("\nMain Menu",)
print("""\n1.Display Student Details
2.Search Details of a Student
3.Delete Details of Student
4.Update Student Detais\n5.Exit""")
    
option = int(input("Enter Your Option:"))

classstud.accept("A",1,100,100)
classstud.accept("B",2,90,90)
classstud.accept("C",3,80,80)

if(option == 1):
    print("\n")
    print("\nList of Students\n")
    for i  in range(ls.__len__()):
        classstud.display(ls[i])

elif(option == 2):
    print("\n Student Found,")
    s = classstud.search(2)
    classstud.display(ls[s])

elif(option ==3):
    classstud.delete(2)
    print(ls.__len__())
    print("List After Deletion")
    for i in range(ls.__len__()):
        classstud.display(ls[i])

elif(option == 4):
    classstud.update(3,2)
    print(ls.__len__())
    print("List after Updating")
    for i in range(ls.__len__()):
        classstud.display(ls[i])




    
        

    
