'''
street="서울시 종로구"
st="아파트"
number_of_rooms= 3
price = 100000000

print("############################")
print("#                          #")
print("# 부동산 매물 광고         #")
print("#                          #")
print("############################")

print(street,"에 위치한 아주 좋은",st,"가 매물로 나왔습니다. 이",st,"는",number_of_rooms,"개의 방을 가지고 있으며 가격은",price,"입니다.")



heights = [178.9, 173.5, 166.1, 164.3, 176.4]
heights
[178.9, 173.5, 166.1, 164.3, 176.4]
type(heights)
<class 'list'>
heights[0]
178.9
heights[-1]
176.4
heights[4]
176.4
heights[5-1]
176.4
bts
           
['V']
bts = ['Jungkook']
           
bts
           
['Jungkook']
bts = bts+['V','RM','Jin']
           
bts
           
['Jungkook', 'V', 'RM', 'Jin']

list(range(0,10,1))
           
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(0,10))
           
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10))
           
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(2,11,2))
           
[2, 4, 6, 8, 10]


list('python')
           
['p', 'y', 't', 'h', 'o', 'n']
bts=['Suga']+['V','RM','Jin']
           
bts
           
['Suga', 'V', 'RM', 'Jin']
x=[1,2,3,]+[4,5,6]
           
x
           
[1, 2, 3, 4, 5, 6]
x=[1,2,3] *5
           
x
           
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
bts=['Suga','V', 'RM', 'Jin',]
           
bts
           
['Suga', 'V', 'RM', 'Jin']
'V' in bts
           
True
'V' not in bts
           
False
'Jimin' in bts
student_list=[['Kim',178.9],['Park',173.5],['Lee',176.1]]
              
student_list
              
[['Kim', 178.9], ['Park', 173.5], ['Lee', 176.1]]
n_list = [200, 700, 500, 300, 400]
              
len(n_list)
              
5
max(n_list)
              
700
min(n_list)
              
200
sum(n_list)
              
2100
sum(n_list) / len(n_list)
              
420.0
t_list = list((10,20,30))
              
t_list
              
[10, 20, 30]
t_list.append(40)
              
t_list
              
[10, 20, 30, 40]
a_list = [10,20,30]
              
b_list = [0,10,20,30]
              
c_list = [0,'']
              
any(a_list),any(b_list),any(c_list)
              
(True, True, False)
all(a_list),all(b_list),any(c_list)
              
(True, False, False)


fruits = []

name = input('좋아하는 과일 이름을 입력하시오: ')
fruits.append(name)
name = input('좋아하는 과일 이름을 입력하시오: ')
fruits.append(name)
name = input('좋아하는 과일 이름을 입력하시오: ')
fruits.append(name)

name = input('과일의 이름을 입력하세요: ')

if name in fruits:
    print('이 과일은 당신이 좋아하는 과일입니다.')
else:
    print('이 과일은 당신이 좋아하는 과일이 아닙니다.')
'''
fruits = []

fruits.append(input('좋아하는 과일 이름을 입력하시오: '))
fruits.append(input('좋아하는 과일 이름을 입력하시오: '))
fruits.append(input('좋아하는 과일 이름을 입력하시오: '))
print('')
name= input('>>>과일의 이름을 입력하세요: ')
if name in fruits:
    print('==> 좋아하는 과일입니다!!~')
else:
    print('==> 좋아하는 과일이 아닙니다!!~')
    



#print(fruits)





