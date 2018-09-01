s=str(input("enter sentence:"))
ew=str(input("enter excluded words:"))
s1=s.split()
for each in s1:
    if each==ew:
        co=s1.count(each)
print(co)

