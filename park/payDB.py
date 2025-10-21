'''
싱글톤으로 디비를 구성하시오
주차장이 지금까지 번돈 계속 축적 하십시오

'''

class PayDB(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PayDB, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.totalMoney = 0
            self._initialized = True

    def payMoney(self, money):
        self.totalMoney += money