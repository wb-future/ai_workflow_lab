def main():
    # devices = ["motor", "sensor", "camera"]

    # devices[1] = "lidar"

    # print(devices)

    # devices = ["motor", "sensor", "camera", "sensor"]

    # devices.remove("sensor")

    # print(devices)
    # print(len(devices))

    # devices = ["motor", "sensor", "camera"]

    # removed_device = devices.pop(1)

    # print(removed_device)
    # print(devices)

    # devices = ["motor", "sensor", "camera", "lidar"]

    # devices.reverse()
    # print(devices)

    # devices = ["motor", "sensor", "camera", "lidar"]

    # devices.append("gripper")
    # devices.remove("sensor")
    # removed_device = devices.pop(1)
    # devices.sort()
    # devices.reverse()

    # print(removed_device)
    # print(devices)
    # print(len(devices))

    # robot_position = (10, 20, 30, 40, 50)

    # # robot_position[1] = 25

    # print(robot_position[4])
    # print(len(robot_position))

    # devices = ("motor", "sensor", "camera")

    # print("lidar" not in devices)
    # print("motor" not in devices)
    # print("camera" in devices)

    # D06 Dictionary practice

    # robot = {
    #     "name": "robot_arm",
    #     "joints": 6
    #     }

    # robot["status"] = "working"
    # robot["battery"] = 85

    # print(robot)
    # print(robot["battery"])
    # print(len(robot))

    # devices = {"motor", "sensor", "camera"}

    # removed = devices.pop()

    # print(removed)
    # print(removed in devices)
    # print(len(devices))

    # devices_a = {"motor", "sensor", "camera"}
    # devices_b = {"sensor", "lidar"}

    # devices_a.add("gripper")
    # devices_a.discard("camera")

    # devices_a.remove("motor")

    # all_devices = devices_a | devices_b
    # common_devices = devices_a & devices_b
    # unique_devices = devices_a - devices_b

    # print(len(devices_a))
    # print(len(all_devices))
    # print(len(common_devices))
    # print("gripper" in unique_devices)

    joint_angles = [10, 20, 30]
    joint_angles[1] = 25

    joint_position = (10, 20, 30)
    print(joint_position[1])

    robot = {
        "name": "practice_arm",
        "joints": 6,
        "status": "ready"
    }
    print(robot["status"])

    activated_devices = {"camera", "sensor", "lidar", "sensor"}

    print(joint_angles)
    print(joint_position)
    print(robot)
    print(activated_devices)

if __name__ == "__main__":
    main()