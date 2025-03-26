# 1. Basic Arithmetic Operations

num1= 12
num2= 6 
print("The first number:",num1)
print("The second number:",num2)
add= num1 + num2
sub= num1 - num2 
mult= num1 * num2 
div= num1 / num2 
print("addition:", add )
print("substraction:", sub)
print("multiplication:", mult)
print("division:", div)



# 2. Modulus and Exponentiation
x= 4
print("The number is:",x)
remainder= x % 3
raised= x ** 2 
print("modulus:" ,remainder)
print("exponentiation:" ,raised)

 #3. Odd or Even

number = 25 
print("The number is=" ,number)
if number % 2 == 0 :
    print("The number is even" )
else:
    print("The number is odd")

# 4. Compare Two Numbers 
a= 30
b= 60
print("The first number is:",30)
print("The second number is:",60)
if a > b: 
    print("{a} is greater than {b}")
elif b > a: 
    print("{b} is greater than {a}")
else:
    print("The two are equal")

# 5. Print Numbers 1 to 10 

count= 1
while count <= 10:
    print(count)
    count=count +1 

# 6. Multiplication Table

n= 32
print("The number is:",n)
for i in range (1,11):
    print(f"{n} x {i} = {n * i}")

# 7. FizzBuzz
for t in range (1,21):
    if t % 3==0 and t % 5==0:
        print("FizzBuzz")
    elif t % 3==0:
        print("Fizz")
    elif t % 5==0:
        print("Buzz")
    else:
        print(t)

# 8. Leap year

p=int (input("enter a year:2020"))
if (p % 4==0 and p % 100==0 and p % 400==0 )or( p % 400==0) or (p % 4==0 and p %100!=0):
    print(f"The year is a leap year")
elif p % 100==0 and p % 400 !=0 :
    print(f"The year is not a leap year")
else:
    print(p)



    



