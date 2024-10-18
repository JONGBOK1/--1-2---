'''
heights = [178,173,166,164,176]

smallest = heights[0]
for item in heights:
    if item < smallest:
        smallest = item
        
print('리스트 원소들:',heights)
print('이 중에서 가장 작은 값은 :',smallest)


heights = [178,173,166,164,176]

largest = heights[0]
for item in heights:
    if item > largest:
        largest = item
        
print('리스트 원소들:',heights)
print('이 중에서 가장 큰 값은 :',largest)

heights = [178,173,166,164,176]
print('이 중에서 가장 작은 값은 :',min(heights))
print('이 중에서 가장 큰 값은 :',max(heights))

heights = [178,173,166,164,176]
heights.sort()
print('이 중에서 가장 작은 값은 :',heights[0])
print('이 중에서 가장 큰 값은 :',heights[-1])

a=[1,2,3]
b=a
b[0]=0
id(a),id(b)
c=list(a)
c[0]=1
print(a)
print(b)
print(c)

a=[x**2 for x in [1,2,3,4,5]]
print(a)

s =[]
for x in [1,2,3,4,5]:
    s.append(x**2)

[x for x in range(10)]

[x* x for x in range(10)]

st = 'Hello World'
[x.upper() for x in st]

a = ['welcom','to','the','python','world']
first_a = [x[0].upper() for x in a]
print(first_a)

a=[x for x in range(10) if x %2 ==0]
print(a)

b=[x**2 for x in range(10) if x %2 ==0]
print(b)

s = ['Hello','12345','World','67890']
numbers = [x for x in s if x.isdigit()]
print(numbers)

[int(x) for x in input('정수를 여러 개 입력하세요 : '),split()]
[int(x) for x in input('정수를 여러 개 입력하세요 : '),split() if x.isdigit()]

[(x,y) for x in [1,2,3] for y in [3,1,4]]
[(x,y) for x in [1,2,3] for y in [3,1,4] if x !=  y]
























