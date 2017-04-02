

def inner():
    print('inner' + str(a))
    # print('inner')

def outer(inner):
    inner()
    print('outer')

def main():
    for a in range(1,5):
        outer(inner)

# for a in range(1,6):
#     outer(inner)

if __name__ == "__main__":
    main()
