robot_status = "idle"

def calculate_battery(remaining_energy, consumed_energy):
    remaining_energy = remaining_energy - consumed_energy
    return remaining_energy

def update_robot_status(new_status):
    global robot_status
    robot_status = new_status

    return robot_status

def main():
    # print(calculate_battery(100, 30))
    # print(calculate_battery(50, 20))

    status = update_robot_status("working")
    print(status)
    print(robot_status)

if __name__ == "__main__":
    main()
    