#1. Write a PYTHON program to evaluate the student performance
#
#   If % is >=90 then Excellent performance

#   If % is >=80 then  Very Good performance
#
#   If % is >=70 then Good performance
#
#    If % is >=60 then average performance.

answer = int(input("evaluate your performance:"))
if answer >= 90:
    print("Excellent Performance")
elif answer >= 80:
    print("Very Good Performance")
elif answer >= 70:
    print("Good Performance")
else:
    print("Average Performance")
