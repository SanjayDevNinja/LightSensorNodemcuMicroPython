#A. Working with Dictionaries

# a)

courseDict = {}

courseDict.update({
    'COMP100' : 'PROGRAMMING 1',
    'COMP228' : 'JAVA PROGRAMMING',
    'COMP237' : 'INTRO. TO AI',
    'COMP246' : 'SOFTWARE SYSTEMS DESIGN',
    'COMP257' : 'UNSUPERVISED LEARNING',
    'COMP258' : 'NEURAL NETWORKS',
    'COMP387' : 'IT SOLUTIONS'
})

print(courseDict)

# b)

#ternary operator to print key if it exists
print("Value Exists, the Key is:", list(courseDict.keys()) [list(courseDict.values()).index('NEURAL NETWORKS')]) \
if 'NEURAL NETWORKS' in courseDict.values() else print("Value NEURAL NETWORKS does not exist")

# c)
print(courseDict.get('COMP237'))

# d)
del courseDict["COMP387"]
courseDict.pop('COMP246')
print(courseDict)

# e)
sortedCourseDict = {}

#create sorted dictionary
for x in sorted(courseDict.values()):
    sortedCourseDict.update({list(courseDict.keys()) [list(courseDict.values()).index(x)] : x})

print(sortedCourseDict)


#B. Working with Strings

#1.
Course = "Python"

print(Course[2:-1])

#2
for c in Course:
    print(c, end="")

#3
# Error if your try to change string, immutable  

#Course[0] = 'R' #error

#4
String = "centennial college courses"
print("\n",String.upper())
print(String.lower())
print(String.swapcase())
print(String.title())
print(String.capitalize())

#5
String2 = "Sanjay"

print(String2 * 5)
print(String2 + " Mahabir")

#C Working with Functions

#1. 
def func1(x, y, z):
    print(f"Actual Arguments for (x,y,z) are ({x}, {y}, {z})")

func1(55, 77, 88)    

#2
def func2(**kwargs):
  print(f"Id is {kwargs['id']}, qualification is {kwargs['qualification']}, name is {kwargs['name']}")

func2(id=77898, qualification='PhD', name='Grace')

#3
def shop(items, amount = 5):
    print(f"Item is {items}, the amount is ${amount}")
    
shop("purse", 35)   
shop("bag", 70)
shop("pen") 
