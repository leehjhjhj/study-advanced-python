# Chapter 1-1
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details
    # 비공식적인(프린트문으로 사용자 입장)
    def __str__(self) -> str:
        return f'str: {self._company} - {self._details}'
    # 객체를 그대로 표현할 때는 repr를 사용한다. 개발자 레벨이다.
    def __repr__(self) -> str:
        return f'repr: {self._company} - {self._details}'

car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})

print(car1)
print(car2)

# 애트립류트 값을 모두 알려주는 __dict__
print(car1.__dict__)
print(car2.__dict__)

# 이미 만들어 둔 매직메소드들을 보여준다.
#print(dir(car1))

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)

# 리스트에서는 repr을 사용한다.
print(car_list)

# 프린트에서는 str을 사용한다.
for i in car_list:
    print(i)
