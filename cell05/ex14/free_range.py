import sys
if len(sys.argv) < 2 :
    print("none")
elif len(sys.argv) == 3 :
    result = []
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    for i in range (start,end+1):
        result.append(i)
    print(result)