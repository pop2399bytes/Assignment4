a=input("Write something: ")
file2= open('output.txt','w')
write=file2.write(a+'\n')
file2.close()

b=input("Write something else: ")
file2=open('output.txt','a')
append=file2.write(b+'\n')
file2.close()

file2=open('output.txt','r')
read=file2.read()
print(read)
file2.close()
