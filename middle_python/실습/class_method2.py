# Chapter 1-2

class Car:
    """
    Car class
    인프런 파이썬 중급 강의 코드이다.
    """

    # 클래스 변수
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self) -> str:
        return f'str: {self._company} - {self._details}'

    def __repr__(self) -> str:
        return f'repr: {self._company} - {self._details}'

    def detail_info(self):
        print(f'Current Id: {id(self)}')
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))
    
    def __del__(self):
        Car.car_count -= 1
# self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})

# ID 확인, 각자 고유의 값을 가지고 있다. 자기 인스턴스 안에 있는 애트리뷰트를 따로따로 관리를 한다.
print(id(car1))
print(id(car2))

print(car1.__dict__)
# __doc__는 클래스의 설명을 보여준다.
print(car1.__doc__)

print(car1.detail_info())

# 클래스는 하나이기 때문에 True이다. 같은 클래스 부모를 사용한다
print(car1.__class__ is car2.__class__)

# 이러면 인자가 없어서 에러가 난다.
#Car.detail_info()

# 이렇게 하면 에러가 나지 않는다.
Car.detail_info(car1)

# 클래스 변수는 모든 인스턴스가 공유한다.
print(car1.car_count) # 2 출력
print(car2.car_count) # 2 출력

# 접근
print(car1.car_count)
print(Car.car_count)

del car2
print(Car.car_count) # 1출력

# 인스턴스 검색 후 -> 클래스 변수를 찾는다. 따라서 동일한 변수를 놓아도 된다.
# 인스턴스가 먼저다. 이것이 포인트이다.