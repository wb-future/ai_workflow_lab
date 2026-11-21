def main():
    # name = "robot"
    # print(name[0])
    # print(name[-1])
    # print(name[-3])
    # line = " python 3.12.3 WSL Ubuntu "
    # parts = line.split()
    # print(parts)
    # print(type(parts))
    # print(parts[0])

    # csv_line = "robot,7,1.57"
    # fields = csv_line.split(",")
    # print(fields)
    # print(type(fields[1]))

    # raw = " robot, 7, 1.57 "
    # clean = raw.strip()
    # fields = clean.split(",")
    # fields = [field.strip() for field in fields]
    # print(f"[{clean}]")
    # print(fields)

    # name = "robot"
    # speed = 1.57

    # # print(f"机器人名称：{name}")
    # # print(f"运行速度：{speed}")
    # # print(f"速度翻倍：{speed * 2}")
    # robot_name = "practice_arm"
    # joint_count = 7
    # speed = 1.57
    # print(f"机器人名称：{robot_name}，关节数量：{joint_count}，运行速度翻倍：{speed * 2}")
    # a = [1, 2]
    # a.extend("34")

    # print(a)

    # robot = ["motor", "sensor", "camera", "gripper"]

    # a = robot.pop(1)
    # b = robot.pop()

    # print(robot)
    # print(a)
    # print(b)
    # devices = ["motor", "sensor"]
    # devices.append("camera")
    # devices.extend(["gripper", "lidar"])
    # devices.insert(1, "controller")
    # devices.remove("sensor")
    # removed_device = devices.pop()

    # print(devices)
    # print(removed_device)
    # print(type(devices))
    # print(type(removed_device))

    robot = input("请输入机器人信息：")
    robot = robot.strip()
    robot_info = robot.split(",")
    robot_info = [f.strip() for f in robot_info]
    print("字段数量：", len(robot_info))
    if len(robot_info) == 3:
        try:
            joint_count = int(robot_info[1])
            speed = float(robot_info[2])
        except ValueError:
            print("机器人信息格式错误")
        else:
            robot_info[1] = joint_count
            robot_info[2] = speed
            print("=====机器人运行日志=====")
            print(f"机器人名称：{robot_info[0]}")
            print(f"机器人关节数量：{robot_info[1]}")
            print(f"机器人运行速度：{robot_info[2]}")
            print("==========================")
    else:
        print("机器人信息格式错误")

if __name__ == "__main__":
    main()
