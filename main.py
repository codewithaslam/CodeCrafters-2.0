"""
print("Hello World")

#Static Datatype
a: int=10
b: float=45.6
c: str="Hloo"
d: bool=True

#Dynamic Datatype
a=10
b=45.6
c="Hloo"
d=True


name: str=input("Enter ur name: ") ; print("The name is ",name)
print(f"The name is {name}")


num_1: int=int(input("Enter a number: "))
num_2: int=int(input("Enter another number: "))

if num_1 == num_2:
    print("The numbers are same")
elif num_1 > num_2:
    print(f"{num_1} is greater") 
else:
    print(f"{num_2} is greater")   

"""


num_1: float=float(input("Enter the number: "))
num_2: float=float(input("Enter another number: "))
print("1: Addition")
print("2: Substraction")
print("3: Division")
print("4: Multipication")
print("5: Modulas")
print("6: Floor Division")
print("7: Exponential")

ch=int(input("Enter your choice(1-7): "))
if ch==1:
    Sum=num_1 + num_2
    print(Sum)

elif ch==2:
    Sub=num_1 - num_2
    print(Sub) 

elif ch==3:
    Div=num_1/num_2
    print(Div) 

elif ch==4:
    Mul=num_1 * num_2
    print(Mul) 

elif ch==5:
    Mod=num_1 % num_2
    print(Mod)     

elif ch==6:
    Flo=num_1 // num_2
    print(Flo)

elif ch==7:
    Expo=num_1 ** num_2
    print(Expo)

else:
    print("INVALID CHOICE")                    