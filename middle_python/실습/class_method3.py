# Chapter 1-3

class Car:
    """
    Car class
    인프런 파이썬 중급 강의 코드이다.
    class, static, Instace Method
    """
    # 클래스 변수
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self) -> str:
        return f'str: {self._company} - {self._details}'

    def __repr__(self) -> str:
        return f'repr: {self._company} - {self._details}'
    
    # 인스턴스 메소드
    # self가 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current Id: {id(self)}')
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price: {}'.format(self._company, self._details.get('price'))

    def get_price_calculate(self):
        return 'After Car Price -> company : {}, price: {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # cls는 Car이다!! Car.price_per_raise와 같음
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Plz Enter 1 or more')
            return
        cls.price_per_raise = per
        print('Success!')

    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'Ok! This is {}'.format(inst._company)
        else:
            return 'No! This is {}'.format(inst._company)

car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 직접 조회는 피해라
print(car1._details.get('price'))

# 인상 전
print(car1.get_price())

# 인상 후
#Car.price_per_raise = 1.4 # <- 이것도 직접 접근이다. 밑처럼 클래스 메소드를 만들어라.
Car.raise_price(1.5)
print(car1.get_price_calculate())
#After Car Price -> company : Ferrari, price: 11200.0 출력

# 이렇게 두가지로 호출할 수 있다.
print(car1.is_bmw(car1))
print(Car.is_bmw(car2))