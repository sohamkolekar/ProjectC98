
#taking file name
file1=input("enter file1 ")
file2=input("enter file2 ")

#func to swap the files
def swapper(path1,path2):
    data_a=open(path1,'r').read()
    data_b=open(path2,'r').read()
    

    open(path1,'w').write(data_b)
    open(path2,'w').write(data_a)
    

swapper(file1,file2)