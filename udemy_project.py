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
