class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    singletone1 = Singleton()
    singletone2 = Singleton()
    print(singletone1 is singletone2)