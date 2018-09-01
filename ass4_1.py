s="we are learning python"
a=s.split()
lw=''
for each in a:
    if len(lw)<len(each):
        lw=each
print(lw)
