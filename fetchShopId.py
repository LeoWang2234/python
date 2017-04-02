
import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

FILE_PATH = '/Users/leo/PycharmProjects/splitstring/not_found.txt'

# failed = open('responses.txt','w')
def main():
    with open(FILE_PATH, 'r') as f:
        for num in f:
            # first = line.split(":")[0]
            # num = first[1:-1]
            num = num.split(':')[0][1:-1]
            print(num)

if __name__ == '__main__':
    main()
