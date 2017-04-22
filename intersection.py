file1 = open('result1.txt')
file2 = open('result2.txt')

try:
    with:
        file1read = file1.read()
        file2read = file2.read()
finally:
    file1.close()
    file2.close()


file1_list = file1read.split(',')
file2_list = file2read.split(',')

intersection = list(set(file1_list).intersection(file2_list))
print(intersection)

