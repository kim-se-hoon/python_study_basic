'''
1. 스마트팜 등록
2. 상태확인
3. 전체 조회
4. 상태 변경
입력: 1

위치: 서면역
채소: 상추
rgb : 레드
온도: 18
등록 완료

입력: 2
위치: 서면역(입력)
출력
채소: 상추
rgb : 레드
온도: 18

입력: 3
업체에서 본 이사리스트 처럼 다 보여주기

입력:4
위치: 서면역
rgb: 보라색
온도: 16
변경 완료
'''
class SmartFarm:
    def __init__(self, location, race, rgb, temp):
        self.location = location
        self.race = race
        self.rgb = rgb
        self.temp = temp

    def printStatus(self):
        print("위치:", self.location)
        print("품종:", self.race)
        print("rgb:", self.rgb)
        print("온도:", self.temp)
    
    def modifyRgbAndTemp(self, rgb, temp):
        self.rgb = rgb
        self.temp = temp
        print("수정 완료")

smartFarmList = []

while True:
    print("1. 스마트팜 등록")
    print("2. 상태확인")
    print("3. 전체 조회")
    print("4. 상태 변경")
    select = input("입력: ")
    if select == "1":
        location = input("위치: ")
        race = input("품종: ")
        rgb = input("rgb: ")
        temp = int(input("온도: "))
        newSmartFarm = SmartFarm(location, race, rgb, temp)
        smartFarmList.append(newSmartFarm)
    elif select == "2":
        findLocation = input("위치: ")
        findCheck = False
        for i in range(len(smartFarmList)):
            if smartFarmList[i].location == findLocation:
                smartFarmList[i].printStatus()
                findCheck = True
                break
        if not findCheck:
            print("조회 대상 없음")

    elif select == "3":
        for i in range(len(smartFarmList)):
            smartFarmList[i].printStatus()
    elif select == "4":
        findLocation = input("위치: ")
        findCheck = False
        for i in range(len(smartFarmList)):
            if smartFarmList[i].location == findLocation:
                modifyRGB = input("rgb: ")
                modifyTemp = int(input("온도: "))
                smartFarmList[i].modifyRgbAndTemp(modifyRGB, modifyTemp)
                findCheck = True
                break
        if not findCheck:
            print("조회 대상 없음")












