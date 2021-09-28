
import fileinput
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

print("=======================ONE LINE======================")
#====================== OPEN
infile =open ('a.txt','r')
#====================== ONE LINE FINDING
sample= input("Nội dung mà bạn cần tìm (trong 1 dòng) là:")
amount =0
linenum=1
for line in infile:
	while line.find(sample) >= 0:
		print("Dong thu "+str(linenum)+" :"+line.strip())
		amount +=1
		line=line[line.find(sample)+len(sample):]
	linenum+=1
if amount !=0:
	print("Noi dung can tim ton tai: ",amount)
else:
	print("Noi dung can tim khong ton tai")

infile.close()
#==========================================	

print("=====================TWO LINE==================")
infile =open ('a.txt','r')
#====================== TWO LINE FINDING
sample= input("Nội dung mà bạn cần tìm (trong 2 dòng) là:")
amount =0
linenum=1
last_line=""
for line in infile:
	line=line.strip()
	#ghep last line voi phan dau cua line moi co chieu dai bang sample. last line (lenght) =[ Sample | Sample ]
	last_line+=line[0:len(sample)+1]
	# Tim thoi nao, tim duoc thi loai bo de tim cai phia sau.
	while last_line.find(sample) >= 0:
		print("Tim thay sample trong 2 dong rieng biet: "+str(linenum-1)+" va "+str(linenum))
		last_line=last_line[last_line.find(sample)+len(sample):]
		amount+=1
	# INLINE
	while line.find(sample) >= 0:
		print("Dong thu "+str(linenum)+" :"+line.strip())
		amount +=1
		line=line[line.find(sample)+len(sample):]
	linenum+=1
	#Lay doan sau co chieu dai = sample cho vao last line de tim vong sau
	last_line=line[ len(line)-len(sample)    :    len(line)   ]

if amount !=0:
	print("Noi dung can tim ton tai: ",amount)
else:
	print("Noi dung can tim khong ton tai")
infile.close()


sample1= input("Thay thế: ")

sample2= input("Bằng nội dung: ")

with fileinput.FileInput("a.txt", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(sample1, sample2), end='')





#====================== CLOSE

