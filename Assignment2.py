print ("Task 1")
str_1 = "Hello, Python World"
print(str_1 )

print ("Task 2")
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

sum = x + y
print("Addition" , sum)

sub = x - y
print("Substraction" , sub)

multiply = x * y 
print("Multiplication", multiply)

div = x / y
print("Division", div)

print ("Task 3")
str_1 = "Hello"
str_2 = "World"
str_3 = str_1 + " " + str_2

print(str_3)
print("The length is:", len(str_3)) 

print ("Task 4")
p = int(input("Is it even or odd: "))
if x % 2 == 0:
    print("even")
else:
    print("odd")

print ("Task 5")
u = 1 

while u <= 10:
    print(u)
    u += 1

print ("Task 6")
m = int(input("Is it positive or negative: "))

if m > 0:
    print("Positive")
elif m < 0:
    print("Negative")
else:
    print("Zero")

print ("Task 7")
v = range(1,11)
for i in v:
    if i % 2 == 0:
        print(i)

print ("Task 8")
n = int(input("Sum till the number: "))
sum = 0
for i in range(n): 
    i+= 1
    sum = sum + i
print("Sum:", sum)

print ("Task 9")
c = 10 

while c > 0:
    print(c)
    c -= 1

print ("Task 10")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    if i == 7:
        break
