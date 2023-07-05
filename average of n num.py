# n=given numbers
# s=sum
# a=average
# x=each numbers


n = int(input("Enter the total number you want to enter:"))
s = 0
for i in range(n):
    x = int(input("Enter the number:"))
    s = s + x
a = s / n
print("Average=", a)