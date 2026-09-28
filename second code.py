print("usman")
#(variable and datatype)
a=23
b=34
print(a+b)
a +=4
print(a)
b *=2
print(b)
print(a+b)
#start with underscore
#_a=34
#print(_a)
#copmarsion operator
a= 4<=6
print(a)
b= 5>=4
print(b)
c=7!=7
print(c)
#copmarise operator
A=5>7 and 5<7
print(A)
B=4<3 or 4>3
print(B)
a=32
print(type(a))
f=3.4
print(type(f))
#convert bool into str
g=True
d=str(g)
print(type(d))
int_s=34
strs=str(int)
print(type(strs))
#convert string into int
str="34"
ints=int(str)
print(type(ints))
#input function()
#a=int(input("enter the number 1:"))
#b=int(input("enter the number 2:"))
#print("number is =",a)
#print("number is =",b)
#print("sum is",a+b)

#practise test
a=3
b=3
print("reminder is",a % b  )

#a=int(input("enter the number"))
#b=int(input("enter the number"))
#print("average is",a**2)

#string function
#string slice
name="usmantahir"
a=len(name)
print(a)
a=name[2:7]
print(a)

names="raousman"
b=names[:4]
print(b)

#slice with skip
string="1234567890"
r=string[1:6:3]
print(r)
ints="abcdefghijklmn"
int=ints[1:8:2]
print(int)

a="usman\"tahir\""
a="usman\rtahir"
print(a)
#practise test
#name=input("user enter name")
#print( f"good afternon {name}",)
name="usman tahir   is good boy"
print(name.replace("   ","  "))
name="usman \ttahir"
print(name.replace("tahir","rao"))

#list are mutable we can change the list
number=[1,3,42,2,22,55,12,25]
number.remove(42)
print(number)
print(number.count(22))
print(number.index(12))
number[3]=33
print(number)
number.append(99)
print(number)
number.remove(55)
print(number)
number.insert(1,100)
print(number)
number.pop(3)
print(number)
#tuple are immutable
a=(12,34,55,55)
print(type(a))
print(a)
print(a.count(12))
print(sum(a))
print(a.index(12))
#dictonary are mutable
student={
    "name":"usman",
    "age":21,
    "gpa":3.12,
    "list":[1,3,4,"usman"]
}
print(student["age"])
#dictonary mehtod
print(student.items())
student.update({"name":"rao"})
print(student)
print(student.get("name"))
s1=student.pop("number",22)
print(s1)
print(student)
#set
s=set() #empty set
print(type(s))
#nested condition
#number=float(input("enter the number :"))
#if(number>=15):
 #   if(number>60):
  #      print("number is greater")
   # elif(number>30):
    #    print("out of range")
    #else:
     #   print("number not grater")
#else:
 #   print("not")               

#while loop
i=1
while(i<6):
    print(i)
    i +=1
l=["usman",22,33.4,"rao",3323]
i=0
while(i<len(l)):
    print(l[i])
    i +=1

 #for loop
tuples=(1,2,3,4,5,6,55,44)
for i in tuples:
    print(i)   

for i in range(1,6):
    print(i)    
s="usman"
for i in s:
    print(i)    

#break statment
for i in range(1,50):
    if(i==32):
        break
    print(i)
#continues statment for loop
for a in range(1,10):
    if(a == 5):
        continue
    print(a)

#function defition
def funct1():
    y=float(input("enter the number:"))
    z=float(input("enter the number:"))
    average= (y+z)/2
    print(average)
funct1() #function call 

def func(name):
    print("hello"+name)
    return "ok"
a=func("usman")   
print(a)        


#recusrion
def show(n):
    if(n == 0):
     return
    print(n)
    show(n-1)

show(5)    

#file input and output read moded
f=open("demo.py","r")
data=f.read()
print(data)
print(type(data))
f.close()

#read line one by one
f=open("demo.py","r")
readline=f.readline()
print(readline)

#write mode means overwrite is my jo phely write kya ha iss ko ktam kar day new write kar day tha ha
f=open("demo.py","w")
datas=f.write("usman tahir")
print(datas)

#write mode but a means append at the last
f=open("demo.py","a")
datas=f.write("\nrao")
print(datas)

#r++ start sa overwrite ka lay use kary thy ha
f=open("demo.py","r+")
data=f.write("abcd")
data=f.read()
print(data)

#w+ is used to terminate the file
f=open("demo.py","w+")
data=f.read()
data=f.write("usman tahir is the student of software\nuniversity")

print(data)

#oop in python
class student():
     collage_name="riphah college"#class atribute

     def __init__(self,fullname,age):
         self.name=fullname
         self.age=age

     def welcom(self):
         print("welcom student")
     
s1=student("usman rao",23)
print(s1.name,s1.age)
s1.welcom()
print(student.collage_name)

class account():
    def __init__(self,acc_no,acc_pass):
        self.acc_no2=acc_no
        self.acc_pass=acc_pass #private key

acc1=account("12345","abcd")
print(acc1.acc_no2)
print(acc1.acc_pass)

#inheritance
class car:
    @staticmethod
    def start():
      print("start is started")
    @staticmethod
    def start():
        print("start is started") 

class hondacar(car):
    def __init__(self,name,model):
        self.name1=name
        self.models=model

car1=hondacar("civi","2020")
print(car1.name1) 
print(car1.start())   


class person():
    def __init__(self):
        print("constructor are callling")
    name="usman tahir"
    age=23
class student(person):
    gpa=3.33
class teacher(student):
    def __init__(self):
            super().__init__() #super method
            print("constructor are callled")
    salary=120000       

obj=person()
print(obj.age)

obj=teacher()
print(obj.salary)
   #class method 
class student():
    school_name="riphah"
    @classmethod
    def school_change(cls,schoolname):
        cls.school_name=schoolname

student.school_change("allied")
print(student.school_name)                 