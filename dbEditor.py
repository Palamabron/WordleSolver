import re

with open("D:\\Programming\\wordleSolver\\dbCopy.txt") as file:
    lines = file.read()
lines = lines.split('\n')
file1 = open("dbFinal.txt", "w")
for line in lines:
    line = re.sub('[^a-z]', '', line)
    file1.write(line + "\n")

file1.close()
