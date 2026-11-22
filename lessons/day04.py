def main():
    # temperature = 25

    # if temperature > 30:
    #     print("温度过高")
    # else:
    #     print("温度正常")
    
    # joint_count = 6

    # print(joint_count == 7)
    # print(joint_count != 7)
    # print(joint_count > 6)
    # print(joint_count < 6)
    # print(joint_count >= 7)
    # print(joint_count <= 6)

    temperature = 25
    battery_level = 80
    emergency_stop = False

    if temperature < 40:
        if battery_level >=20:
            if not emergency_stop:
                print("机器人允许运行")
            else:
                print("急停已启动，禁止运行")
        else:
            print("电量不足，禁止运行")
    else:
        print("温度过高，禁止运行")

if __name__ == "__main__":
    main()