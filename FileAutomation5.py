from sys import *
import os
import time

def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
         DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)

    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current Directory name :",foldername)

        for fname in filename:
            print(fname, " : ",os.path.getsize(foldername+"/"+fname), " Bytes")

    else:
         print("Invalid Path")
        
def main():
    print("-------Automation Script---------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
            print("This automation script is used to perform File Automation")
            exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name of Script First Argument")
            print("Example : Demo.py Marvellous")
            exit()
   
    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as : ",endtime - starttime, "Seconds")
          
if __name__ == "__main__":
    main()