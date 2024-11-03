year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 == 0:
#       print("Leap Year")
#     else:
#       print("Not Leap Year")
# else:
#     print("Not Leap Year")



if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
