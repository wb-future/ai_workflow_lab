def main():
    # for joint_id in range(1,8):
    #     print("检查关节：", joint_id)

    # devices = ["motor", "sensor", "camera", "gripper", "lidar"]

    # for device in devices:
    #     print("正在检查设备：", device)


    # devices = ["motor", "sensor", "camera", "gripper", "lidar"]

    # print("===== 机器人设备筛选 =====")

    # for device in devices:
    #     if device != "sensor":
    #         print("可用设备：", device)

    # print("===== 筛选完成 =====")


    joint_angles = [10, 20, 30, 40, 50, 60, 70]
    num = 0
    total = 0
    for joint_angle in joint_angles:
        num = num + 1
        print(f"关节编号：{num}，角度：{joint_angle}")
        total = total + joint_angle
    
    print("关节总数：", num)
    print("关节角度总和：", total)
    print("关节角度平均值：", total / num)

if __name__ == "__main__":
    main()