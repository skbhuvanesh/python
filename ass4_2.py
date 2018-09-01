s=str(input("enter sentence:"))
w=str(input("enter word:"))
s1=s.split()
for each in s1:
    if each==w:
        c=s1.count(each)
print(w,":",c)
