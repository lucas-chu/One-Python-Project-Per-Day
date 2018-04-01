class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        super().spam()


A().spam()
B().spam()