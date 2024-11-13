'''
population = ['Seoul',9765,'Busan',3441,'Inchen',2954]
print("서울 인구:",population[1])
print("인천 인구:",population[-1])
print("도시 리스트:",population[::2])
print("인구의 합:",sum(population[1::2]))

L=['A','B','C','D','E','F']

if'c'in L:
    L.remove('c')
print(L)


if'D'in L:
    L.remove('D')
    
L=['A','B','C','D','E','F']
print(L)

L.pop()
print(L)
l=L.pop()

print(l)
print(L)

l=L.pop(2)
print(l)
print(L)

numbers = [9,6,7,1,8,4,5,3,2]
numbers.sort(reverse=True)
print(numbers)

s=['D','C','a','A','F','e']
s.sort()
print(s)
'''
import random

quotes=[]
quotes.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.")
quotes.append("언제나 현재에 집중할수 있다면 행복할것이다..")
quotes.append("고생없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")              
quotes.append("사람은 사랑할 때 누구나 시인이 된다.")              
quotes.append("시작이 반이다.")



print("################################")
print("#       오늘의 명언            #")
print("################################")
print("")
print(random.choice(quotes))







