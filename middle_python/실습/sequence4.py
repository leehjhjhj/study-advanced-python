"""
시퀀스형
해시 테이블: 적은 리소스로 많은 데이터를 효율적으로 관리
Dict -> key 중복 허용 x, Set -> 중복 허용 x
"""

# Immutable Dict (읽기 전용)

from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only

d_frozen = MappingProxyType(d)
print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 불가
# d_frozen['key2'] = 'value2'
# TypeError: 'mappingproxy' object does not support item assignment

# 수정 가능
d['key2'] = 'value2'
print(d)

print()

s1 = {'Apple', 'Apple', 'Orange', 'kiwi'}
s2 = set(['Apple', 'Apple', 'Orange', 'kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Apple', 'Orange', 'kiwi'})

s1.add('Melon')
print(s1)
# s5.add('Melon') AttributeError: 'frozenset' object has no attribute 'add'
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
# 집합은 s3 처럼 선언해라!

# 지능형 집합(comprehending Set)
from unicodedata import name
print('------')
print({name(chr(i), '') for i in range(0, 256)})
