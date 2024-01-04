"""
시퀀스형
컨테이너(Container): 서로 다른 자료형(list, tuple, collections.deque)
플랫(Flat): 한개의 자료형(str, bytes, bytearray, array.array, memoryview)
가변(list, bytearray, array, memoryview, deque)
불변(tuple, str, bytes)
"""

# tuple advance
# Unpacking

print(divmod(100 ,9))
print(divmod(*(100 ,9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

"""
출력
0 1 [2, 3, 4, 5, 6, 7, 8, 9]
0 1 []
1 2 [3, 4, 5]
"""

# Mutable vs Immuatable

m = [15, 20, 25]
i = (15, 20, 25)

print(m, id(m))
print(i, id(i))

m = m * 2
i = i * 2

print(m, id(m))
print(i, id(i))

m *= 2
i *= 2

print(m, id(m))
print(i, id(i))

"""
[15, 20, 25] 4382396992
(15, 20, 25) 4382336448
[15, 20, 25, 15, 20, 25] 4382391616
(15, 20, 25, 15, 20, 25) 4377738496
[15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 4382391616
(15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 4377764480

튜플은 계속 새로운 객체 생성, 리스트는 연산에 따라서 재할당
"""

# sort vs sorted
# reverse, key=Len, key=str.Lower, key=func ...

# sorted: 정렬 후 새로운 객체 반환

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print(f_list)
print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True))
print('sorted -', sorted(f_list, key=len))
print('sorted -', sorted(f_list, key=lambda x: x[-1]))
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True))
"""
sorted - ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']
sorted - ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']
sorted - ['apple', 'mango', 'lemon', 'orange', 'papaya', 'coconut', 'strawberry']
sorted - ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry']
sorted - ['strawberry', 'coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya']
"""
# sort: 정렬 후 객체 직접 변경
# 반환 값 확인 (None)

print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
"""
sort - None ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']
sort - None ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']
sort - None ['mango', 'lemon', 'apple', 'papaya', 'orange', 'coconut', 'strawberry']
sort - None ['papaya', 'apple', 'orange', 'lemon', 'mango', 'coconut', 'strawberry']
sort - None ['strawberry', 'coconut', 'mango', 'lemon', 'apple', 'orange', 'papaya']
원본이 직접 수정되어서 None!
"""

# List vs Array 적합 한 사용법 설명
# 리스트 기반: 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반: Array(리스트와 거의 호환), 머신러닝, 딥러닝..


