#def variables
print("type the number of ORDINARY COWS: ")
N = int(input())
print("type the number of CRAZY COWS: ")
C = int(input())

sections_list = []
sections_num = N

if (C > N or N<=2 or C<=2):
    print ("Well that is not correct, because according to task blablablabla")
else:
    print("Type sections numbers (", N, ")")
    for x in range(N):
        sections_list.append(int(input()))
    sections_list.sort()
    print("Available space: ", sections_list)
 
