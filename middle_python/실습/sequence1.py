"""
시퀀스형
컨테이너(Container): 서로 다른 자료형(list, tuple, collections.deque)
플랫(Flat): 한개의 자료형(str, bytes, bytearray, array.array, memoryview)
가변(list, bytearray, array, memoryview, deque)
불변(tuple, str, bytes)
"""
# 리스트 및 튜플 고급
# 지능형 리스트(comprehending Lists)

chars = '+_)(*&^%$#@!)'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# 지능형 리스트

code_list2 = [
   ord(s) for s in chars
]

print(code_list2)

# comprehending Lists + Map, Filter
code_list3 = [
    ord(s) for s in chars if ord(s) > 40
]

print(code_list3)

code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list4)

print([chr(s) for s in code_list1])

# Generator는 한번에 한 개의 항목을 생성(메모리 유지 x)
# Generator 생성
import array

# () 로 해주면 아직 다 만든 상태가 아님
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(next(tuple_g))
print(array_g.tolist())

print(('%s' % c + str(n) 
       for c in ['A', 'B', 'C', 'D']
       for n in range(1, 21)))

for s in ('{}'.format(c) + str(n) 
       for c in ['A', 'B', 'C', 'D']
       for n in range(1, 21)):
    print(s)

# 리스트 주의!!
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4
print(marks1)
print(marks2)

marks1[0][1] = 'x'
marks2[0][1] = 'x'

print(marks1)
# [['~', 'x', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks2)
# [['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~']]

print([id(i) for i in marks1])
print([id(i) for i in marks2])
#[4314311104, 4314310976, 4314310912, 4314310784]
#[4314310720, 4314310720, 4314310720, 4314310720]