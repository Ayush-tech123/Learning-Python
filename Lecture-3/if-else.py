num = int(input("Enter a number in range 0-50 : "))

if num<50 and num>0:
    print("Number lies in the asked range of 0-50: ")
    if num<30:
        print("Number is less than 30")
    else:
        print("Number is greater than 30 and less than 50")
else:
    print("Please provide number in the required range")

