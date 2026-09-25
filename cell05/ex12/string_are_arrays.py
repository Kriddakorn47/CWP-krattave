import sys

if len(sys.argv) != 2 or 'z' not in sys.argv[1]:
    print("none")
else:
    for i in sys.argv[1]:
        if i == 'z':
            print(i)