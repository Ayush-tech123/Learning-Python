def sqr():
    a = int(input("First Number :- "))
    b = int(input("Second Number :- "))
    c = a * b
    c = str(c)
    print("----------------------------------")
    print("Product is " +c)

start = int(input("To multiply press 1\n"))

if(start == 1):
    sqr()
else:
    print("Invalid Input")
    