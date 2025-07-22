#if the file is there
try :
    file1=open("sample.txt","r")
    read= file1.read()
    print(read)
    file1.close()
#if the file isn't there
except FileNotFoundError:
    print("Error: the file does not exist")


