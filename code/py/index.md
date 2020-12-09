# Index
---
# 1. Module,pip,comment
- save with file extension `file.py`
- __Output__ => `print("output")`
- __Execute__ => `python file.py`

## a. PIP
+ module for python package
    __version__ => `pip -V || -version`
    __Install__ => `pip install <package>`
    __Install_version__ => `pip show <package>`
    __Uninstall__ => `pip uninstall  <package>`
    __List__ => `pip list`
    __search__ => `pip search <package>`
    __help__ =>`pip help`

## b. Comment
Ignored by compiler
    __Single-line__ => `#Comment`
    __Multi-line__ => `'''Comment'''`

---
# 2. Variable & Data-type
+ __Memory-location__ => `var=value`
    - _Variable_ : Contao=iner to store value
    - _Keyword_ : Reserverd word in python
    - _Identifiers_ : class/funtion/variable_name
+ __Data-type__ =>
    - _Integers_ : `int = 3`
    - _Float_ : `float = 3.2`
    - _String_ : `str="String"`
    - _Boolean_ : `bool=True/False`
+ __Operators__
    1. Arithmetic -> + - * /
    2. Assignment -> = += -= /= *=
    3. Comparison -> == > < <= >= !=
    4. Logical -> and or not === && || !

## a. Inbuilt Function 
__Type__ : `type(var) // class<int>` if integer
    - _Integer_ : int("69") => 69
    - _String_ str(69) => "69"
    - _float_ : float(69) => 69.0
    - _input_ : input("Enter ou input")
    - _print_ : print("Output of program")

---
# 3. String
"Which are under quotes" -> str = "Harry"
    + Splicing
        - str[0] => H
        - str[-1] => y
        - str[0:3]/[:3] => Har
        - str[1:4] => arr
        - str[3:] => ry
        - str[0:0:2]/[::2] => Hry
    + Function
        - len(var) => 5
        - str.endswith("ry") => True
        - str.count("r") => 2
        - str.capitalize() => HARRY
        - str.find("H") => 0
        - str.replace("r","l") => Hally

# 4. List & Tupel
list of Data-type : var = ["String",0,["nested",7],True]
    + Slicing :
        - var[0] => "string"
        - var[-1] => True
    + Function : var = [1,8,2,7]
        - var.sort() => [1,2,7,8]
        - var.reverse() => [7,2,8,1]
        - var.append(10) => [1,8,2,7,10]
        - var.insert(2,10) => [1,8,10,2,7]
        - var.pop(`value`) => [1,8,2] || var.pop(8) => [1,2,7]
        - var.remove(1) => [1,2,7]
        - Tuple : tup=(1,6,3)
# 5. Dictonary
just like objects : 
    + Syntax : var = {"key":value,...}
        - var["key"] => value
    + Function
        - var.items() => {[(key:value),(key:value)]}
        - var.keys() => [key-1,key-2,...]
        - var.update({key:new_Value})
        - var.get('key') => value
## a. Sets
collection of non-repetitive element :
    + Syntax : s=set()
        - var.add(`value`) => {`value`}
        - len(s) => 1
        - s.remove(`value`)
        - s.pop() => return remove valued
        - s.clear => Clear the set
        - s.union
        - s.interaction

# 6. Conditional
if `cond-1`:
    True-1-Exp
elif `cond-2`:
    True-2-Exp
else:
    All-False-Exp

# 7. Loop
Repetable task till condition is true:
+ While Loop
    - while `cond`:
    #Repeat_code
    - eg:
```py
i=0
while i<=10:
    i=i+1
    print(i)
```
+ For Loop
```py
#number
for x in range(1,10,2):#start,stop,skip
    print(x)#1/3/5/7/9
#array
arr=[2,5,1]
for x in arr:
    print(x)#2/5/1
#else
x=0
for x in range(1,5):
    print(x)
else :
    print("Done")#1/2/3/4/Done
#Break-get_out_of_loop
for x in range(1,10):
    print(x)
    if x>=7:
        break#1/2/3/4/5/6/7
#Continue-get_directly_in_loop||no_need_to_go_further
for x in range(1,7):
    print(x)
    if x>=4:
        continue
    print(x)#1/1/ 2/2/ 3/3/ 4/5/6
#pass-To_Do_Nothing
for x in range(1,7):
    print(x)
    if x>=4:
        pass
```

## Function & Recursion
- Function
```py
def function_name():
    pass
function_name()#calling
```
- Calling Function
```py
def function_name(parameter):
    pass
function_name(argument)#giving input
```
- Default parameter
```py
def function(var=value):
    pass
```
- Recursion-calling itself : (input to 10)
```python
def f(a):
    print(a)
    if a<10:
        a+=1
        f(a)#agin calling funtion
f(2)#input
```

---

## File I/O
+ mode
    - Mode: r->Reading / w->writting / a->appending / t->updating
    - Mode: rb->read in binary mode / rt->read in text mode
- syntax
```py
with open("./file",'mod') as f:
    #code
    f.close()
```
- Read
```py
with open(file,'r') as f:
    rd=f.read()#read file
    #rd_2_line=f.read(2)#Read 2 line
    #rd=f.readline()#red one line
    print(rd)
    f.close()
```
- Write
```py
with open(file,'w') as f:
    rd=f.write("overwite things")
    print(rd)
    f.close()
```

---

# OOP
__class__=>Blueprints for creating objects
```py
class ClassName(object):
    """docstring for ClassName"""
```
__Modllling Prblems__:
_noun_ -> class -> Employee
_Adjective_ -> attribute -> name,age,salary
_Verb_ -> Method -> getSalary(),increment()
eg:
```python
class students:
    school="St.Lawrence"
    def marks(para):
        print("Pass the exam")

piyu=stdents()#Object instance
print(piyu.school)#ST.Lawrence
students.school="RJ Thakur"#Changing class attribute
print(piyu.school)#RJ Thakur
piyu.marks()#Pass the Exam


```