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


print("\n\t\t\t CALCULATOR SIMULATOR")
print("\t\t\t ********************\n")
print("\t\t\t  1: Addition")
print("\t\t\t  2: Substraction")
print("\t\t\t  3: Division")
print("\t\t\t  4: Multipication")
print("\t\t\t  5: Modulas")
print("\t\t\t  6: Floor Division")
print("\t\t\t  7: Exponential\n")


while True: 
        ch=int(input("Enter your choice(1-7): "))
        num_1: float=float(input("Enter the number: "))
        num_2: float=float(input("Enter another number: "))  
        

        if ch==1:
            Sum=num_1 + num_2
            print(f"\n{num_1} + {num_2} = {Sum}\n")
        
            
        elif ch==2:
            Sub=num_1 - num_2
            print(f"\n{num_1} - {num_2} = {Sub}\n") 
        

        elif ch==3:
            Div=num_1/num_2
            print(f"\n{num_1} / {num_2} = {Div}\n")
        

        elif ch==4:
            Mul=num_1 * num_2
            print(f"\n{num_1} * {num_2} = {Mul}\n") 
        
        elif ch==5:
            Mod=num_1 % num_2
            print(f"\n{num_1} % {num_2} = {Mod}\n")  
        

        elif ch==6:
            Flo=num_1 // num_2
            print(f"\n{num_1} // {num_2} = {Flo}\n")
        

        elif ch==7:
            Expo=num_1 ** num_2
            print(f"\n{num_1} ** {num_2} = {Expo}\n")
        
        else:
            print("\n\t\t\t!!!!!ERROR!!!!!")  
            break                  

        
