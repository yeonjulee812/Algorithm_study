a, b, c = map(int, input().split())
import math

if b == c:
    print(-1)
elif math.ceil(a/(c-b))>0:
    if math.ceil(a/(c-b)) == a/(c-b):
        print(int(a/(c-b)+1))
    else:
        print(int(math.ceil(a/(c-b))))
else:
    print(-1)