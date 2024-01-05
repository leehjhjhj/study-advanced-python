"""
일급함수(일급 객체)
파이썬 함수 특징
1. 런타임 초기화
2. 변수 할당 가능
3. 함수 인수 전달 가능
4. 함수 결과 반환(return)
"""

# 함수 객체

def factorial(n):
    '''
    Factorial function -> n: int
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
# {'__qualname__', '__annotations__', '__kwdefaults__', '__globals__', '__defaults__', '__call__', '__code__', '__get__', '__closure__', '__name__'}

print()
print()

var_function = factorial
print(var_function(5))
print(list(map(var_function, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce

print(list(map(var_function, filter(lambda x: x % 2, range(1, 6)))))
print([var_function(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11))) # 근데 이게 더 좋다

# 익명함수
# 가급적 주석을 작성해라
# 가급적 일반 함수
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1, 11)))

print()
print()

# callable: 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print(callable(str), callable(A), callable(list), callable(var_function))

# partial 사용법: 인수고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(100, 100))

# 인수 고정
five = partial(mul, 5)
print(five(10)) # 50

six = partial(five, 6)
print(six())
print([five(i) for i in range(1, 11)]) # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
