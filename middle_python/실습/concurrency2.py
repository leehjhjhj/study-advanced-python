"""
병행성(Concurrency): 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
병렬성(Parallelism): 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도
"""

# Generator Ex1

def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')

temp = iter(generator_ex1())

print(next(temp))
print(next(temp))
"""
Start
A Point
Continue
B Point
End
Traceback (most recent call last):
  File "/Users/leehyunje/inflern/middle_python/실습/concurrency2.py", line 19, in <module>
    print(next(temp))
StopIteration
"""

for v in generator_ex1():
    #print(v)
    pass

# Generator ex2
# temp2 = [x * 3 for x in generator_ex1()]

temp3 = (x * 3 for x in generator_ex1())

for i in temp3:
    print(i)

print()
print()

# Gnerator Ex3(중요함수))
# count, takewhile, filterfalse, accumulate, chain, product, groupby

import itertools

gen1 = itertools.count(1, 2.5)

# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# ... 무한 1 3.5 6.0 8.5 11.0

# 조건

gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    #print(v)

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    #print(v)
    # 3, 4, 5만 호출
    pass

gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    #print(v)
    pass

# 연결 1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5)) # ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

# 연결 2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6)) # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7)) # [('A',), ('B',), ('C',), ('D',), ('E',)]

# 연산 (경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D'), ('D', 'E'), ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'), ('E', 'E')]

# 그뤃봐

gen9 = itertools.groupby('AAABBBCCCDDD')
#print(list(gen9))
for chr, group in gen9:
    print(f"{chr}: {list(group)}")

"""
A: ['A', 'A', 'A']
B: ['B', 'B', 'B']
C: ['C', 'C', 'C']
D: ['D', 'D', 'D']
"""