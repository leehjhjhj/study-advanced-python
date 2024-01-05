"""
일급함수(일급 객체)
클로저 기초
외부에서 호출된 함수의 변수값, 상태 복사 후 저장 -> 후에 접근(엑세스) 가능
"""

# Clousure 사용

def closure_ex1():
    # Free variable
    # 클로저 영역#
    series = []
    ############
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()
print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
'''
inner >> [10] / 1
10.0
inner >> [10, 30] / 2
20.0
inner >> [10, 30, 50] / 3
30.0
'''

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars) # ('series',) 가 출력된다.
print(avg_closure1.__closure__[0].cell_contents) # [10, 30, 50] 출력

# 잘못된 클로저 사용

def closure_ex2():
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10))
# UnboundLocalError: local variable 'cnt' referenced before assignment

def closure_ex3():
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total # 추가, 이제 프리 변수가 된다.
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

