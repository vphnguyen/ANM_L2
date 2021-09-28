

#====================== EXAMPLE 1
s="this is a string"
print(s.find("is"))
newstring =s.replace("this","that")
print(newstring) #
UpperString =s.upper()
print(UpperString) #

print(id(s)) #
print(id(UpperString)) #
a= 'this is string with lot of whitespace at the beginning and at the end'
RemovingWhiteSpace = a.strip()
print(RemovingWhiteSpace) #
print(RemovingWhiteSpace.strip("this")) #
#=====
x,y=10,11
f="this {} is added and thereafter we add {}"
FormattedString = f.format(x,y)
print(FormattedString)
m,n = 10,11
f="this %d is added and thereafter we add %d"
FormattedString = f % (x,y)
print(FormattedString)
#====================== 

print("=============================================")
#====================== OPEN
infile =open ('a.txt','r')
#====================== ONE LINE FINDING
sample= input("Nội dung mà bạn cần tìm (trong 1 dòng) là:")
amount =0
for line in infile:
	while line.find(sample) >= 0:
		print(line.strip())
		amount +=1
		line=line[line.find(sample)+len(sample):]
if amount !=0:
	print("Noi dung can tim ton tai: ",amount)
else:
	print("Noi dung can tim khong ton tai")


#==========================================	

sample= input("Nội dung mà bạn cần tìm (trong 1 dòng) là:")
amount =0
for line in infile:
	while line.find(sample) >= 0:
		print(line.strip())
		amount +=1
		line=line[line.find(sample)+len(sample):]
if amount !=0:
	print("Noi dung can tim ton tai: ",amount)
else:
	print("Noi dung can tim khong ton tai")










#====================== CLOSE
infile.close()
