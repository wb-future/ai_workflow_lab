import sys
from datetime import datetime


def main():
    # 输出欢迎信息和当前 Python 版本。
    print("欢迎来到 Python 编程练习！")
    print(f"当前 Python 版本：{sys.version.split()[0]}")
    # 获取并格式化本机当前日期和时间。
    now = datetime.now()
    print(f"当前日期和时间：{now:%Y-%m-%d %H:%M:%S}")
    print(f"当前日期和时间：{now:%d/%m/%Y %H:%M}")
    print("当前日期和时间：",now.strftime('%Y-%m-%d %H:%M:%S'))
    robot_name = "practice_arm"
    print("机器人名称:",robot_name)
    print("变量类型:",type(robot_name))
    joint_count = 7
    joint_angle = 1.57
    print("关节数量：",joint_count,"变量类型：",type(joint_count))
    print("关节角度：",joint_angle,"变量类型：",type(joint_angle))
    gripper_closed = False
    print("夹爪是否闭合：",gripper_closed,"变量类型：",type(gripper_closed))
    gripper_closed = True
    print("夹爪是否闭合：",gripper_closed,"变量类型：",type(gripper_closed))
    joint_count_text = "7"
    print("关节数量文本：",joint_count_text,"变量类型：",type(joint_count_text))
    joint_count_number = int(joint_count_text)
    print("关节数量文本转换为整数：",joint_count_number,"变量类型：",type(joint_count_number))
    joint_count_number = joint_count_number + 2
    print(joint_count_number)

if __name__ == "__main__":
    main()
