"""
병행성(Concurrency)
이터레이터, 제네레이터
Iterator, Generator

파이썬 반복 가능한 타입
collections, text file, list, Dict, Set, Tuple, unpacking, *args ..: Iterable
"""
# 반복 가능한 이유 -> 내부적으로 iter(x)가 호출이 되었다.
t = "ABCD"
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인
print(hasattr(t, '__iter__')) # True

from collections import abc
print(isinstance(t, abc.Iterable))

print()
print()

# 넥스트 패턴

class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration
        self._idx += 1
        return word
    
    def __repr__(self) -> str:
        return 'WordSplit({})'.format(self._text)
    
wi = WordSplitter('Do today what you could do tommorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합을 만들어낼 수 있다.
#   데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동
# 3. 작은 메모리 조각을 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word #제너레이터

        return
    
    def __repr__(self) -> str:
        return 'WordSplitGenerator({})'.format(self._text)
    
wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)
print(wt, wg)

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

print()
print()