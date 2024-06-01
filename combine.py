filename = input("Please enter the filename: ")
fileAname = filename + "-A.txt"
fileBname = filename + "-B.txt"
fileOutName = filename + "-out.txt"

file1 = open(fileAname, "rt")
file2 = open(fileBname, "rt")
fileout = open(fileOutName, "wt")


oddLine = file1.readline()
evenLine = file2.readline()

while oddLine or evenLine:
    if (oddLine):
        print(oddLine, end = "")
        fileout.write(oddLine)
        oddLine = file1.readline()
    if (evenLine):
        print(evenLine, end = "")
        fileout.write(evenLine)
        evenLine = file2.readline()

file1.close()
file2.close()
fileout.close()
