import os

# open a file as append text mode
file = open("test.txt", 'at')

file.write("\nadd new content at the end of the file")
file.close()

print(os.listdir("."))

if(not os.path.exists("test-data")):
    os.mkdir("test-data")

if(not os.path.exists("test-data/testfile.txt")):
    testfile = open("test-data/testfile.txt", "at")
    testfile.write("Hey, I am a test file")
    testfile.close()