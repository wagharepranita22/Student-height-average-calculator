print("Welcome to the student height average calculator")
student = int(input("Give the number of student "))
height = []
for i in  range(student):
    heights= int(input("GIve the student height : "))
    height.append(heights)

sum = 0
for i in height:
    sum+=i

print(f"{sum} total of the height")
average = sum//student
print(f"Average of student height : {average}")

max_height =0
for i in height:
    if max_height < i:
        max_height = i

print("maximum height of class : ",max_height)
