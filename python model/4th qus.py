
string=input("Please enter a string:")
alphabets,num,special,space=0,0,0,0;
a=[]
d=[]
spl=[]
for i in range(len(string)):
 if(string[i].isalpha()):
   alphabets+=1
   a.append(string[i])
 elif(string[i].isdigit()):
   num+=1
   d.append(string[i])
 elif(string[i].isspace()):
   space+=1
else:
   special+=1
   spl.append(string[i])
print("Alpabets letters:",alphabets, a)
print("\nnumbers:",num, d)
print("\nSpace:",space)
print("\nSpecial characters:",special, spl)
