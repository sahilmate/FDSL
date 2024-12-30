"""Write a Python program to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using
a) Selection Sort b) Bubble sort and display top five scores"""

def Selection_Sort(Score_list):
    for i in range(len(Score_list)-1):
        min_score=i
        for j in range(i+1,len(Score_list)):
            if Score_list[min_score]>Score_list[j]:
                min_score=j 
        Score_list[i],Score_list[min_score]=Score_list[min_score],Score_list[i]
        
def Bubble_sort(Score_list):
    for i in range(len(Score_list)):
        for j in range(len(Score_list)-1):
            if Score_list[j]>Score_list[j+1]:
                Score_list[j],Score_list[j+1]=Score_list[j+1],Score_list[j]

def reverse_sort(Score_list):
    for i in range(len(Score_list)):
        min_score=i 
        for j in range(i+1,len(Score_list)):
            Score_list[j]>min_score
            min_score=j
            Score_list[i],Score_list[min_score]=Score_list[min_score],Score_list[i]
    
def top_five(Score_list):
    Selection_Sort(Score_list)
    reverse_sort(Score_list)

    temp=[]
    for i in range(5):
        temp=Score_list[i]
        print(temp)
    
#main 
n=int(input("Enter the no. of students present in the class:"))
print("Enter the scores:(in float point)")
Score_list=[]
for i in range(n):
    data=float(input())
    Score_list.append(data)
print("Unsorted Score:",Score_list)

while(1):

    print("\nEnter \n 1.Selection Sort \n 2.Bubble Sort \n 3.Display Top Five Scores")
    ch=input("Enter option:")

    if ch=="1":
        Selection_Sort(Score_list)
        print("Sorted Scores:",Score_list)

    elif ch=="2":
            Bubble_sort(Score_list)
            print("Sorted Scores:",Score_list)
            
    elif ch=="3":
        Selection_Sort(Score_list)
        print("Sorted Scores:",Score_list)
        print("Top Five Scores are:")
        top_five(Score_list)
   


    




