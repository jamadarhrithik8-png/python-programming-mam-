import os.path
import sys
fname = input("Enter the filename to sort:")#input file
if not os.path.isfile(fname):
    print("File", fname, "does not exist.")
    sys.exit()
    infile = open(fname, "r")#read mode
    lines = infile.readlines()#list of lines from file
    infile.close() #close the input file
    lineList = []#Empty List
    for line in lines:
        lineList.sort()#sort the list
        outfile = open("sorted.txt","w+")#write and read mode
        if not os.path.isfile(fname):
            print("Not able to create sorted.txt")
            sys.exit(0)
            for line in lineList:
                outfile.write(line + "\n")
                outfile.seek(0,0)
                fstr=outfile.read()
                print("Sorted.txt content:",len(lineList), "lines")
                outfile.close()