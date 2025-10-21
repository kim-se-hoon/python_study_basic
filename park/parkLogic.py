'''
싱글톤을 써서 주차장을 만드시오
주차장 대수는 10대 입니다.
주차시 시각과 차량번호 입력
'''

class SingletonClass(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonClass, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.parkList = []
            self._initialized = True

    def inputCar(self, time, num):
        dic = {}
        dic["time"] = time
        dic["num"] = num
        print(dic)
        self.parkList.append(dic)
        print(self.parkList)