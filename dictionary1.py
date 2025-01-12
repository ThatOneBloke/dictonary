student_score1 = {"name":"xavier", "maths":"95", "science":"93", "english":"90"}
print(student_score1)
print(student_score1.keys())
print(student_score1.values())
print(student_score1.items())

student_score2 = {"name":["xavier", "james", "gabriel", "samantha", "jordan"], "maths":[95, 81, 97, 64, 39], "science":[93, 72, 81, 95, 85], "english":[90, 84, 76, 59, 94]}
print(student_score2)
for i in student_score2:
    print(student_score2[i])

print("xavier" in student_score2)
#you need to add ".values" if you want to check if there is something in a value
print("xavier" in student_score2.values())