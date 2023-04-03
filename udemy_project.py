st = "print only the words that start with s in this sentence"
word = st.split()
for i in st.split():
    if i[0] == "s":
        print(i)

# use range to print even numbers from 1 to 10.
a = list(range(0, 11, ))
for i in a:
    if i % 2 == 0:
        print(i)

# use a list to create a list of numbers divisible by 3 from 1 to 50.
x = list(range(1, 51))
for i in x:
    if i % 3 == 0:
        print(i)

# print even if the length of the word is even
st = "print every word in this sentence that has an even number of letters"
for a in st.split():
    if len(a) % 2 == 0:
        print(a)

# write from 1 to 100. For multiple of three print "fizz".For multiple of 5 print"buzz".for multiple of 5 and 3 print
# "FizzBizz"


for i in (range(1, 101)):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# use list to create list of first letters of the string.

st = "Create a list of the first letters of every word in this list"
for word in st.split():
    a = word[0]
    print(a)

for a in range(0, 21, -1):
    print( a)


i = 1
while i <= 10:
    print(i)
    i = i + 5


# writing a function  for a condition which returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def even_and_odd(a, c):
    if a % 2 == 0 and c % 2 == 0:
        print(min(a, c))
    else:
        print(max(a, c))

# Write a function takes a two-word string and returns True if both words begin with same lette


def string_problem(text):
    a = text.split(text)
    if a[0] == a[1]:
        return True
    else:
        return False


# making a function that if Given two integers, return True if the sum of the integers is 20 or if one of the
# integers is 20. If not, return False

def integers_problem(a, b):
    return a + b == 20 or a == 20 or b == 20:


 # Write a function that capitalizes the first and fourth letters of a name


def capitalize_name(name):
    if len(name) >= 4:
        capitalized_name = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    else:
        capitalized_name = "try something other name instead"
    print(capitalized_name)


# Given a sentence, return a sentence with the words reversed


def master_yoda(text):
    print(" ".join(text.split()[::-1]))


master_yoda(text="i will die tomorrow")