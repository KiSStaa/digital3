# davaleba1

def eando():
    start= int(input("Enter the lowest number in the range: "))
    end= int(input("Enter the highest number in the range: "))
    answer = input("please enter even or odd: ")

    odd = []
    even = []

    for num in range(start,end):
        if num % 2 == 0:
            even.append(num)
        else : 
            odd.append(num)

    if answer == "even":
        print(f"This numbers in this range is even {even}")
    elif answer == "odd":  
        print(f"This numbers in this range is odd {odd}")


eando()

# davaleba 2

pal = input("Enter the value: ")

reverse = pal[::-1]

if( pal == reverse):
    print("Yes,it is palindrome")
else:
    print("No, it is not palindrome")    

# davaleba3    

def calc(a,b):
    return a + b,a - b, a * b, a / b
   

num1 = int(input("Enter The First Number: "))    
num2 = int(input("Enter The second Number: "))    

add, sub, mult, div = calc(num1,num2)

print(f"Add of the two numbers is: {add}")
print(f"Subtract of the two numbers is: {sub}")
print(f"Multiply of the two numbers is: {mult}")
print(f"Divide of the two numbers is: {div}")

# davaleba 4

n = int(input("Enter the number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i
print(fact)    

# davaleba 5

nu = int(input("Enter The Number: "))

for i in range(1,11):
    print(nu,"*",i,"=",nu*i)