''' 클래스 '''

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1)
print(cal2)

print(cal1.add(10))
print(cal1.add(100))
print(cal1.add(200))
print()
print(cal2.add(100))
print()
print(cal1.add(90))
print(cal2.add(100))

class Mystatus:
    def __init__(self, name, id, pw, age):
        self.name = name
        self.id = id
        self.pw = pw
        self.age = age
        self.height = 0

    def print_name(self):
        print(self.name)

    def print_my(self):
        print(self.name)
        print(self.id)
        print(self.pw)
        print(self.age)

    def take_age(self, age):
        self.age += age

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

auth = Mystatus("gildong", "gildong1212", "1234", 18)
auth.print_name()
auth.print_my()
print()
auth.take_age(10)
auth.print_my()

print()
auth.setHeight(180)
print(auth.height)
print(auth.getHeight())

print()
class Move:
    def __init__(self):
        self.phone = ""
        self.address = ""
        self.houseSize = ""
        self.wishPayClient = ""
        self.wishPayCompany = ""
        self.companyPhone = ""
        print("부모 생성됨")

    def addClient(self, phone, address, houseSize, wishPayClient):
        self.phone = phone
        self.address = address
        self.houseSize = houseSize
        self.wishPayClient = wishPayClient

    def printMove(self):
        print("연락처:", self.phone)
        print("이사주소:", self.address)
        print("이사평수:", self.houseSize)
        print("희망가격:", self.wishPayClient)
        print("의뢰 가격:", self.wishPayCompany)
        print("업체 연락처:", self.companyPhone)

    def applyCompanyPay(self, wishPayCompany, companyPhone):
        self.wishPayCompany = wishPayCompany
        self.companyPhone = companyPhone
        print("업체 의뢰 완료")

class ChildMove(Move):
    def __init__(self):
        print("자식 생성됨.")
        super().__init__()

    def childPrint(self):
        print("hihi")

    def printMove(self):
        print("메소드 오버라이딩")
        print("재정의")

child = ChildMove()
child.childPrint()
child.addClient("1", "1", "1", "1")
child.printMove()



