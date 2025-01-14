'''
Calculate Students Average Heights
'''
student_heights = list( map(int,input("Enter Student Heights :\n").split()))

print(student_heights)

sum = 0
len = 0
for height in student_heights:
    sum+=height
    len+=1

print(f"The Average Of student heights is : {sum/len}")