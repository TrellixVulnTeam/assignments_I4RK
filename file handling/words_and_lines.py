f1=open(r"S:\Senior Secondary\fileNames.txt",'r')
s=f1.readlines()
print("Number of lines : ",len(s))
x=f1.read()
l=x.split(' ')
print("Number of Words : ",len(l))