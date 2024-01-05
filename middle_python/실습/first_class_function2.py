"""
일급함수(일급 객체)
클로저 기초
"""

# 파이썬 변수 범위(scope)

from typing import Any


def func_v1(a):
    print(a)
    print(b)

#func_v1(10)
########################
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)
#########################
c = 30

def func_v3(a):
    print(a)
    print(c)

c = 40
# func_v3(10)
# UnboundLocalError: local variable 'c' referenced before assignment
# 로컬 변수로 먼저 인식한다, 쓰고 싶으면 global로 사용하라

print()
print()

# Closure() 사용 이유
# 서버 프로그래밍 -> 동시성 제어 -> 같은 메모리 공간에 여러 자원이 접근 -> 교착 상태
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 파이썬 클로저는 공유하되 변경되지 않는(Immutable) 적극적으로 사용
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드 프로그래밍에 강점
    
a = 100
print(a + 100)
print(a + 1000)

# 결과 누적 함수
print(sum(range(1, 51)))

# 클래스 이용
class Averager:
    def __init__(self) -> None:
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)
    
# 인스턴스, 상태를 기억하고 있다.
averager_cls = Averager()
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
'''
inner >> [10] / 1
10.0
inner >> [10, 30] / 2
20.0
inner >> [10, 30, 50] / 3
30.0
'''

