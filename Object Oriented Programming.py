# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:02:00 2019

@author: xiaob
"""

#%% Project Manipulating the Datebase for Student Info
class Student:
    def __init__(self,No,Name,Gender,Age):
        self.No = No
        self.Name = Name
        self.Gender = Gender
        self.Age = Age
    def show(self):
        print("%-16s %-16s %-8s %-4s" %(self.No, self.Name, self.Gender, self.Age))

class StudentList:
    def __init__(self):
        self.students = [] #列表中每一个元素都是 Student类的一个对象
    
    def show(self):
        print("%-16s %-16s %-8s %-4s" %("No", "Name", "Gender", "Age"))
        for s in self.students:
            s.show()
    
    def __insert(self,s): #插入一个student的对象 s
        i = 0
        while (i < len(self.students) and s.No > self.students[i].No):
            i = i + 1
        if (i < len(self.students) and s.No == self.students[i].No):
            print(s.No + "This student No. has already existed.")
        self.students.insert(i,s)
        print("Success in adding this student.")
        return True
    
    def __update(self,s):
        flag = False
        for i in range (len(self.students)):
            if(s.No == self.students[i].No):
                self.students[i].Name = s.Name
                self.students[i].Gender = s.Gender
                self.students[i].Age= s.Age
                print("Successfully Updated")
                flag = True
                break
        if (not flag):
            print("The student with this No. doesn't exist")
        return flag
    
    def __delete(self,No):
        flag = False
        for i in range (len(self.students)):
            if(No == self.students[i].No):
                del self.students[i]
                print("Successfully Deleted")
                flag = True
                break
        if (not flag):
            print("The student with this No. doesn't exist")
        return flag
    
    def delete(self):
        No = input("Student No: ")
        if No != '':
            self.__delete(No)
            
    def insert(self):
        No = input("Student No: ")
        Name = input("Student Name: ")
        while True:
            Gender = input("Gender: ")
            if (Gender == 'Male' or Gender == 'Female'):
                break
            else:
                print("Given gender is not defined.")
        Age = input("Student's Age: ")
        if Age == '':
            Age = 0
        else:
            Age = int(Age)
        
        if (No != '' and Name != ''):
            self.__insert(Student(No,Name,Gender,Age))
        else:
            print("Student No. and Student's Name can not be empty")
        
    def update(self):
        No = input("Student No. to be updated: ")
        Name = input("Student Name to be updated: ")
        while True:
            Gender = input("Gender to be updated: ")
            if Gender == 'Male' or Gender == 'Female':
                break
            else:
                print("Give Gender is not defined.")
        Age = input("Age to be updated: ")
        if Age == '':
            Age = 0
        else:
            Age = int(Age)
        if (No != '' and Name != ''):
            self.__update(Student(No,Name,Gender,Age))
        else:
            print("Student No. and Student's Name can not be empty")    
    
    def process(self):
        while True:
            s = input(">")
            if s == "show":
                self.show()
            elif s == "insert":
                self.insert()
            elif s == "update":
                self.update()
            elif s == "delete":
                self.delete()
            elif s == "exit":
                break
            else:
                print("show: show students")
                print("insert: insert a new student")
                print("update: update a new student")
                print("delete: delete a student")
                print("exit: exit the program" )


st = StudentList()
st.process()