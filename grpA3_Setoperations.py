"""3. In Second year Computer Engineering class of M students, set A of students play cricket and
set B of students play badminton. Write python program to find and display-
A. Set of students who play either cricket or badminton or not both
B. Set of students who play both cricket and badminton
C. Set of students who play only cricket
D. Set of students who play only badminton
E. Number of students who play neither cricket nor badminton"""

#####students in whole class######
C=[]
n=int(input("Enter the no. of students in class:"))
print("Enter the Students in class and press enter:")
for i in range(n):
    data=input()
    C.append(data)
print("Students in whole class:",C)
##############Students who play cricket ****************
A=[]
n1=int(input("Enter the No. of students who play Cricket: "))
print("Enter the Students Name who play Cricket:")
for i in range(n1):
    data=input()
    A.append(data)
j=[x for x in A if(x in C)]
print("Students who play cricket from class:", j)
#****************#Students who play badminton********************
B=[]
n2=int(input("Enter the no. of students who play badminton"))
print("Enter the students name who play Badminton")
for i in range(n2):
    data=input()
    B.append(data)
f=[x for x in B if(x in C)]
print("Students who play badminton from class:",f)
#############Students who play either Cricket or badminton but not both##########################3
c=[x for x in f if(x not in j)]
d=[x for x in j if(x not in f)]
cd=c+d
print("Students who play either cricket or badminton but not both:",cd)
print()
#############list of students who play both Cricket and Badminton################
print()
cb=[x for x in f if x in j]
print("Students who play both cricket and badminton",cb)
print()
#############Students who play only Cricket###########
s=[x for x in j if(x not in f)]
print("Students who play only Cricket:",s)
##########Students who play only Badminton###############33
m=[x for x in f if(x not in j)]
print("Students who play only Badminton:",m)
###############No. of students who play neither cricket nor badminton############
y=[]
for i in C:
    if i not in j:
        y.append(i)
y_=[]
for j in C:
    if j not in f:
        y_.append(j)
    a=[x for x in y if x in y_]
print ("No. of students who play neither cricket nor badminton:",len(a))
print()

'''
# Initialize lists for different sports groups
GroupA = []
GroupB = []
GroupC = []

# Input the number of students who play cricket
n = int(input("Enter the number of students who play cricket: "))
print("Enter the names of", n, "students who play cricket:")
for i in range(n):
    crc = input()
    GroupA.append(crc)
print("Original list of students who play cricket is: " + str(GroupA))

# Input the number of students who play badminton
n = int(input("Enter the number of students who play badminton: "))
print("Enter the names of", n, "students who play badminton:")
for i in range(n):
    bad = input()
    GroupB.append(bad)
print("Original list of students who play badminton is: " + str(GroupB))

# Input the number of students who play football
n = int(input("Enter the number of students who play football: "))
print("Enter the names of", n, "students who play football:")
for i in range(n):
    good = input()
    GroupC.append(good)
print("Original list of students who play football is: " + str(GroupC))

# Calculate the lengths of the lists
lena = len(GroupA)
lenb = len(GroupB)
lenc = len(GroupC)

# List of students who play both CRICKET and BADMINTON
print("\n List of students who play both CRICKET and BADMINTON:")
listCB = []

for i in range(lena):
    for j in range(lenb):
        if GroupA[i] == GroupB[j]:
            listCB.append(GroupA[i])

print(listCB)

# List of students who play either CRICKET or BADMINTON but not BOTH
print("\n List of students who play either CRICKET or BADMINTON but not BOTH:")
listCBNB = []
flag = 0

for i in range (lenb):
    for j in range(lena):
        if GroupB[i] == GroupA[j]:
            flag = 1
    if flag == 0:
        listCBNB.append(GroupB[i])
    flag = 0

for i in range(lena):
    for j in range(lenb):
        if GroupA[i] == GroupB[j]:
            flag = 1
    if flag == 0:
        listCBNB.append(GroupA[i])
    flag = 0

print(listCBNB)

# No of students who play neither CRICKET nor BADMINTON
print("\n No of students who play neither CRICKET nor BADMINTON:")
listNCNB = []

for i in range(lenc):
    for j in range(lena):
        if GroupC[i] == GroupA[j]:
            flag = 1
            break
    for var in range(lenb):
        if GroupC[i] == GroupB[var]:
            flag = 1
            break
    if flag == 0:
        listNCNB.append(GroupC[i])
    flag = 0

lenNCNB = len(listNCNB)
print(lenNCNB)
print(listNCNB)

# List of students who play CRICKET and FOOTBALL but not BADMINTON
print("\n List of students who play CRICKET and FOOTBALL but not BADMINTON:")
listCF = []

for i in range(lenc):
    for j in range(lena):
        if GroupC[i] == GroupA[j]:
            listCF.append(GroupC[i])
            break

print(listCF)
lenCF = len(listCF)
print(lenCF)
'''





