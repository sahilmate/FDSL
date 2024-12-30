"""Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Display the list of students who were absent for the test
d) Display mark with highest frequency
"""

Total_student=int(input("How many students are in Class?-->"))
S=[]
for i in range(Total_student):
    names = input(f"Name of student {i+1} is: ")
    S.append(names)
print("Students in class:",S)
marks_scored=[]
absent_student=[]
total=0
for i in S:
    marks = int(input(f"Marks scored by student {i} in FDS test is: (put -1 for absent students): "))
    if marks==-1:
        absent_student.append(i)
    else:
        marks_scored.append(marks)
        total+=marks
def avg():
    Average=total/(len(marks_scored))
    print("Average of Score of the class :",Average)
#2..To print highest and lowest Score
def maxi():
    max_score=marks_scored[0]
    for mark in marks_scored:
        if max_score<mark:
            max_score=mark
    print("Highest score of class is:",max_score)
def mini():
    min_score=marks_scored[0]
    for mark in marks_scored:
        if mark<min_score:
            min_score=mark
    print("Lowest score of class is:",min_score)

#mark with highest frequency
def freq():
    max_frequency = 0
    print("\nMarks\t|\tFrequency")
    
    for i in range(len(marks_scored)):
        if marks_scored[i] != -1:
            frequency = 1  # Initialize frequency for the current mark
            for j in range(i + 1, len(marks_scored)):
                if marks_scored[j] == marks_scored[i]:
                    frequency += 1  # Increment frequency for matching marks

            if frequency > max_frequency:
                max_frequency = frequency
                most_common_mark = marks_scored[i]

            print(f"{marks_scored[i]}\t|\t{frequency}")

    print("\nScore", most_common_mark, "is with the highest frequency", max_frequency)

'''def freq():   
    max = j = 0
    print("\nMarks\t|\tFrequency")
    for i in marks_scored:
        if(marks_scored.index(i)==j):
            print(i,"\t|\t",marks_scored.count(i))
            if(max<marks_scored.count(i)):
                max = marks_scored.count(i)
                mark = i
        j += 1
    print("\nScore",mark,"is with highest frequency",max)'''

while(1):
    print("\nEnter\n1.Average\n2.High score\n3.Lowest Score\n4.Higest Frequency\n5.No. of Absent Students\n6.Name of the Absent students \n7.Exit")
    ch=input()
    if ch=='1':
        avg()
    elif ch=='2':
        maxi()
    elif ch=='3':
        mini()
    elif ch=='4':
        freq()
    elif ch=='5':
        print("No. of students absent for FDS test:",len(absent_student))
    elif ch=='6':
        print("Name of students who were absent for the test are: ",absent_student)
    elif ch=='7':
        print("Exiting, thank you")   
        break 
'''
scores = []
absent_students = []
while True:
    score = input("Enter a score (or 'done' to finish)(if student is absent, i/p -1): ")
    if score == 'done':
        break
    try:
        score = int(score)
        if score > 100:
            print("Invalid input. Please enter a score between 0 and 100.")
        else:
            scores.append(score)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# A. Average score of the class
total_score = 0
for score in scores:
    total_score += score
average_score = total_score / len(scores)
print("A. Average score of the class:", average_score)

# B. Highest and lowest score of the class
highest_score = scores[0]
lowest_score = float ('inf')
for score in scores:
    if score > highest_score:
        highest_score = score
    if score < lowest_score and score >= 0:
        lowest_score = score
           
print("B. Highest score of class B:", highest_score)
print("   Lowest score of class B:", lowest_score)

# C. Count of students who were absent for the test
absent_count = 0
for score in scores:
    if score == -1:
        absent_count += 1
for student in absent_students:
    absent_count += 1
print("C. Count of students who were absent for the test:", absent_count)

# D. Mark with highest frequency
most_common_score = None
most_common_score_count = 0
for score in scores:
    count = 0
    for s in scores:
        if s == score:
            count += 1
    if count > most_common_score_count:
        most_common_score = score
        most_common_score_count = count
print("D. Mark with highest frequency:", most_common_score)        
'''







