"""
병행성(Concurrency): 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
병렬성(Parallelism): 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도
코루틴(Coroutine)

코루틴: 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
쓰레드: OS에서 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티 스레드
yield, send: 메인 <-> 서브 루틴이 상호작용
코루틴 제어, 상태, 양방향 전송

서브루틴: 메인 루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
코루틴: 루틴을 실행 중 중지 -> 동시성 프로그래밍
코루틴 장점: 쓰레드에 비해 오버헤드 감소
쓰레드: 싱글쓰레드 -> 멀티 쓰레드 -> 복잡, 공유되는 자원 때문에 데드락 발생, 컨텍스트 스위칭 비용이 크다. 자원 소비 가능성 증가
def -> async, yield -> await
"""

# 코루틴 ex1

def coroutine1():
    print('>>> coroutine start')
    i = yield
    print('>>> coroutine received: {}'.format(i))

# 메인 루틴
# 제너레이터 선언1
cr1 = coroutine1()
print(cr1, type(cr1)) # <generator object coroutine1 at 0x1005c2820> <class 'generator'>

# yield 지점까지 서브루틴 수행
#next(cr1)

# 기본 전달 값 None 이다.
# 값 전송(100)
#cr1.send(100)
'''
>>> coroutine start
>>> coroutine received: 100
Traceback (most recent call last):
  File "/Users/leehyunje/inflern/middle_python/실습/concurrency3.py", line 31, in <module>
    cr1.send(100)
StopIteration
'''

# 잘못된 사용
cr2 = coroutine1()
#cr2.send(100) TypeError: can't send non-None value to a just-started generator

# 코루틴 ex2
# GEN_CREATED: 처음 대기 상태
# GEN_RUNNING: 실행 상태
# GEN_SUSPEND: Yield 대기 상태 -> 이때 send 가능
# GEN_CLOSED: 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine start : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y # 서버루틴에서 나에게 준 것은 x + y, 메인에서 준 것은 z
    print('>>> coroutine start : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(next(cr3))
print(getgeneratorstate(cr3)) # GEN_SUSPENDED
cr3.send(100)
print(getgeneratorstate(cr3)) # GEN_SUSPENDED

print()
print()

# 코루틴 ex3
# StopIteration 자동처리
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
#print(next(t1))

print()
print()

def generator2():
    yield from 'AB'
    yield from range(1, 4)

t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))