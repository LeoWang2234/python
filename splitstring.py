#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
file_object = open('result.txt')
failed = open('failed.txt','w')
not_found = open('not_found.txt','w')
normal = open('normal.txt','w')
try:
    file_content =file_object.read()
finally:
    file_object.close()

# file_content = str(file_content)
#
# print(file_content)

strlist = file_content.split('\n')

failed_num = 0
not_found_num = 0
normal_num = 0
total_num = 0
for value in strlist:
    total_num = total_num + 1
    print(value)
    if '获取标品失败' in value:
        failed.write(value)
        failed.write('\n')
        failed_num = failed_num + 1
        continue
    if '业务方商户未找到' in value:
        not_found.write(value)
        not_found.write('\n')
        not_found_num = not_found_num + 1
        continue

    normal.write(value)
    normal.write('\n')
    normal_num = normal_num + 1

failed.close()
not_found.close()
normal.close()


print(str(failed_num)+'\n')
print(str(not_found_num)+'\n')
print(str(normal_num)+'\n')
print(str(total_num)+'\n')
print(total_num==failed_num+normal_num+not_found_num)