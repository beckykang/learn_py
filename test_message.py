"""s="test1,test2,test3"
l=s.split(',')
print(l)
          
for i in range(len(l)):
    print(l[i])"""

names=input("Enter names separated by commas: ")
acounts=input("Enter assignment counts separated by commas:  ")
grades=input("Enter grades separated by commas: ")

student_name=names.split(',')
student_counts=acounts.split(',')
student_grade=grades.split(',')

for i in range(len(student_name)):
    print("Hi {},".format(student_name[i]))
    print("This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.".format(int(student_counts[i]),int(student_grade[i]),int(student_grade[i])+int(student_counts[i])))
