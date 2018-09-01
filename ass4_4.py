s=str(input("enter sentence:"))
w=str(input("enter word:"))
a=len(s)
s1=s.split()
for each in s1:
    if each==w:
        counter=s1.count(each)
density=counter/a
print("Density:",density)
