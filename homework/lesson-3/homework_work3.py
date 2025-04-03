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
input1=input("enter number:")
converted_input1=int(input1)
input2=input("enter number :")
converted_input2=int(input2)
print("The first number is:",converted_input1)
print("The second number is:",converted_input2)
if converted_input1 > converted_input2: 
    print("{converted_input1} is greater than {converted_input2}")
elif converted_input2 > converted_input1: 
    print("{converted_input2} is greater than {converted_input1}")
else:
    print("The two are equal")

# 5. Print Numbers 1 to 10 

print("5. Print Numbers 1 to 10")
count= 1
while count <= 10:
    print(count)
    count=count +1.5



# 6. Multiplication Table

input6=input("a multiplication table")
converted_input6=int(input6)
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
print("Leap  Year")
input10=input("enter an year")
converted_input10=int(input10)
if (converted_input10 % 100==0 and converted_input10 % 400==0 ):
    print(converted_input10,"The year is a leap year")
elif converted_input10 % 4==0 and converted_input10 % 100 !=0 :
    print(converted_input10,"The year is  a leap year")
else:
    print(converted_input10,"The year is not a leap year")



    



