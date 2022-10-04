def main():
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        x = int(input('Введите X: '))
        if x < 7:
            y = (x * x + a * a + b * b) / (a + b)
        else:
            y = x * x * x * (a * a + 2 * a * b + b * b)
        print("y = %.1f" % y)
    except ValueError:
        print("Неверные входные данные!")
    except:
        print("Возникла ошибка!")
    input("Нажмите Enter для выхода")


if __name__ == '__main__':
    main()
