class student:
    @staticmethod #decorator
    #without any object reference we can access methods
    def hello():
        print("hello world")
s=student()
s.hello()