'''
Calculate The Top Score in The Class
'''
student_scores = list( map(int,input("Enter Student Scores :\n").split()))

print(student_scores)

top_score = -1
for score in student_scores:
    top_score = score if top_score < score else top_score

print(f"The Highest score is  : {top_score}")