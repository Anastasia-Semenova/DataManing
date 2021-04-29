from random import randint

F_0 = 0
F_1 = 0
F_2 = 0
numbers_of_repeat = {}
nodes = []
vars100 = []
vars500 = []


class X:
    def __init__(self, index):
        self.value = 0
        self.element = -1
        self.index = index


class DataStream:
    @staticmethod
    def start_stream():
        for i in range(1000000):
            # time.sleep(0.2)
            random_int = randint(1, 1000)
            DataStream.count_the_number_of_repeat(random_int)
            DataStream.count_X_for_AMS_for_100_vars(value=random_int, i=i)
            DataStream.count_X_for_AMS_for_500_vars(value=random_int, i=i)
        DataStream.count_the_moments(F_1=F_1, F_2=F_2)
        DataStream.show_F_2_by_vars100()
        DataStream.show_F_2_by_vars500()

    @staticmethod
    def count_the_number_of_repeat(number):
        if numbers_of_repeat.get(number) is None:
            numbers_of_repeat[number] = 1
        else:
            numbers_of_repeat[number] =  numbers_of_repeat[number] + 1

    @staticmethod
    def count_the_moments(F_1, F_2):
        F_0 = len(numbers_of_repeat.values())
        print("F_0: " + str(F_0))
        for value in numbers_of_repeat.values():
            F_1 = F_1 + value
            F_2 = F_2 + value * value
        print("F_1: " + str(F_1))
        print("F_2(simple computation): " + str(F_2))

    @staticmethod
    def count_X_for_AMS_for_100_vars(value, i):
        for var in vars100:
            if var.index == i:
                var.element = value
                var.value = 1
            else:
                if var.index < i:
                    if var.element == value:
                        var.value += 1

    @staticmethod
    def count_X_for_AMS_for_500_vars(value, i):
        for var in vars500:
            if var.index == i:
                var.element = value
                var.value = 1
            else:
                if var.index < i:
                    if var.element == value:
                        var.value += 1

    @staticmethod
    def show_F_2_by_vars100():
        F_2_by_vars100 = 0
        for var in vars100:
            F_2_by_vars100 = F_2_by_vars100 + (2 * var.value - 1)
        F_2_by_vars100 = F_2_by_vars100 * 1000000 / 100
        print("F_2(by 100 vars): " + str(F_2_by_vars100))

    @staticmethod
    def show_F_2_by_vars500():
        F_2_by_vars500 = 0
        for var in vars500:
            F_2_by_vars500 = F_2_by_vars500 + (2 * var.value - 1)
        F_2_by_vars500 = F_2_by_vars500 * 1000000 / 500
        print("F_2(by 500 vars): " + str(F_2_by_vars500))


def fill_vars100():
    for i in range(100):
        vars100.append(X(index=randint(1, 1000000)))


def fill_vars500():
    for i in range(500):
        vars500.append(X(index=randint(1, 1000000)))


if __name__ == '__main__':
    fill_vars100()
    fill_vars500()
    DataStream.start_stream()
