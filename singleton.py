class SingletonClass(object):

    def __new__(cls):        
        if not hasattr(cls, "instance"):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    print("싱글톤")
    singleton1 = SingletonClass()
    print(singleton1)
    singleton2 = SingletonClass()
    print(singleton2)
