a =[1,2,3,4,5]

uIn = int(input("Enter a number to find in array : "))

if uIn in a:
    print("Yes!! your input number " + str(uIn) + " on the array list.")
else:
    print("Sorry!! your numbers not on the list.....")

max_a = max(a)
print("The max number of a is " + str(max_a))
