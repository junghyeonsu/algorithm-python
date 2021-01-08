class Car:
    # 생성자
    def __init__(self, name, color):
        self.name = name # 클래스의 멤버
        self.color = name # 클래스의 멤버

    #클래스의 메소드
    def show_info(self):
        print("이름 :", self.name, " 색상 :", self.color)


# 객체 생성
car1 = Car("소나타", "빨간색")
# 객체에 대한 메소드 실행
car1.show_info()


# 상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아서 사용하는 기법
# 부모와 자식 관계가 존재한다.

# 부모 클래스 정의
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다.", self.power, "의 데미지를 입혔습니다.")
    

# 자식
class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type


# 자식 클래스에 attack 함수가 없지만 부모클래스에 있기 때문에
# 상속받아서 사용 가능
duck = Monster("슬라임", 6, "몬스터")
duck.attack()