def main():
    # a = 9
    # b = 4
    # print(a / b)
    # print(a // b)
    # a = -9
    # print(a / b)
    # print(a // b)
    # print(9 % 4)
    # print(-9 % 4)
    # print(3 ** 4)
    # print((-3) ** 2)
    a = int(input("请输入一个整数："))
    b = int(input("请输入另一个整数："))
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("除数不能为零")
    # length_cm = float(input("请输入长度（厘米）："))
    # length_m = length_cm / 100
    # print(f"{length_cm} 厘米 = {length_m:.2f} 米")
    # print(length_m)
    # print(int("7") + 2)

if __name__ == "__main__":
    main()
    