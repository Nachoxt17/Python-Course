#(0)-In order to Execute Python in the Console, we need to use the
# Python Extension of V.S. Code and press "Run".
#(1)-How to *Console.log("...")* in Python:
print("Hello World")

#(2)-Variables in Python. They can be both Un-Typed and Typed:
#(2.1)-Declaring Un-Typed Variables:
age = 23 # Integer Number.
price = 14.55 # Decimal Number.
firstName = "Edward" # String.
isOnline = False # Boolean.

print("#(2.2)-Receiving Inputs from an User in Python:")

secondName = input("What is your name?: ")
print("Hello " + secondName)

print("#(2.3)-Convert the Type of Variables:")

birthYear = input("Enter your birth year: ")
print("#By Default, this Input is taken as a String.")
age = 2020 - int(birthYear)#This the way to Convert a Value to an Integer Number.
print("Your age is: " + str(age))

float("2020")#This the way to Convert a Value to a Decimal Number.
bool("false")#This the way to Convert a Value to a Boolean.
str(2024)#This the way to Convert a Value to a String.

print("#(3)-Calculator Exercise:")

firstNumber = input("#1: ")
secondNumber = input("#2: ")
sum = float(firstNumber) + float(secondNumber)#NOT *int(secondNumber)*
#-Mathematical Operations between Integer and Decimal(Floating) Numbers are Incompatible in Python.
print("Sum Result: " + str(sum))
#-Concatenations between Strings and other Types are Incompatible in Python.

#-This is a Better way of doing it:
firstNumber = float(input("#1: "))
secondNumber = float(input("#2: "))
sum = firstNumber + secondNumber#NOT *int(secondNumber)*

print("#(4)-Methods(Pre-Defined Functions of the Programming language) and Objects in Python:")

course = "Python for Beginners"
print(course.upper())#-".upper()" Is a Method of Python; this one is used to Transform all the letters
# of this String into UpperCase.
print(course.lower())#-Converts into LowerCase.
print(course.find("B"))#-Returns the Index of the Specified Value in the String/Object (If it cannot find it, it will return "-1").
print(course.replace("for", "4"))#-Replaces the Specified Value for the Desired one in the String/Object.

print("#-The ''In'' Operator answers with a Boolean if the Specified Value is in the String/Object:")
print("Python" in course)

print("#(5)-Arithmetic Operators in Python:")
print(8 + 5)#-Addition.
print(8 - 5)#-Subtraction.
print(8 * 5)#-Multiplication.
print(8 / 5)#-Decimal(Floating) Division.
print(8 // 5)#-Integer Division.
print(8 % 5)#-Modulus(Returns the Remained Number of the Integer Division, in this case == 3).
print(8 ** 5)#-Exponent Operator.

#(5.1)-Two Different ways to Update a Variable:
x = 10
x = x + 3 #-1st way.
x += 3 #-2nd way.
#-Subtraction and Multiplication are also Compatible:
x -= 4
x *= 4

#(5.2)-Equal to Real Life Mathematics, "*" and "/" are Operated 1st in an Operation in Python:
y = 10 + 3 * 5 #-Is going to be read by default as:
y = 10 + (3 * 5) #-In order to Control that, we must add Parenthesis:
y = (10 + 3) * 5

#(6)-Comparison and Logical Operators:
z = 3 > 2 #-3 is Greater Than 2.


price = 25
#-The ''And'' Operator:
print(price > 26 and price < 30)#-Returns "True" because both Conditions are Met.
#-The ''Or'' Operator:
print(price > 26 or price < 30)#-Returns "True" because AT LEAST ONE of the Conditions is Met.
#-The ''Not'' Operator:
print(not price > 30)#-Returns "True" because the Condition is NOT Met.

#(7)-If Statements:
if price > 11:
    print("Too Expensive!")
#-In order to define a Block of code in Python for a Function or Similar, we use the 4x Space like this: "    ".
elif price < 11: #-"elif" is the abbreviation of "else if".
    print("Very Cheap!")
elif price == 11:
    print("Fair price")
print("Done")

#(7)-While Loops in Python:

i = 1
while i <= 100:
    print(i * '*')
    i += 1

#(8.1)-Lists(Arrays) in Python:
names = ["Max", "Peter", "Jan", "Alex"]
print(names[0])
print(names[1])
print(names[-1])#-"-1" Returns the last Item in the List.
print(names[-2])#-"-2" Returns the pre-last Item in the List.
print(names[1:3])#-Prints Item 1 to 3 in the List.

#-Editing the List Values:
names[0] = "Piotr"

#(8.2)-Methods of Lists(Arrays) in Python:

names.append("Dzimitry")#-Adds a new Item at the end of the List.
names.insert(2, "Vladimir")#-Adds a new Item in the Specified Index(in this case "2") of the List.
print(len(names))#-Returns the Length of Items in the List.

#(9)-For Loops in Python:
for item in names:
    print(item)#-This will Print each Item on a Separated Line.

#-Another different way of doing it is using the *range("Start","End", "Step")* Method:
range(8)#-Returns 1 to 8.
range(4, 12)#-Returns 4 to 11.
range(4, 12, 2)#-Returns 4, 6, 8 and 10.

#(10)-Tuples(Data Structures) in Python:
numbers = (1, 2, 3, 4)#-They are written similar to Lists but using "(...)" instead of "[...]".
#-TUPLES ARE IMMUTABLE; their Values CANNOT be re-assigned.

