from pysimverse import Drone
import time


def main():
    print("================================")
    print("   PYSIMVERSE DRONE MISSION")
    print("================================")

    # Create drone
    drone = Drone()

    print("[1] Connecting to PySimVerse...")
    drone.connect()
    print("[OK] Connected")

    # -----------------------------
    # TAKEOFF
    # -----------------------------
    print("[2] Taking off...")
    drone.take_off()
    time.sleep(3)

    # -----------------------------
    # ALTITUDE / HOVER
    # -----------------------------
    print("[3] Stabilizing / hovering...")
    time.sleep(3)

    # -----------------------------
    # BASIC MANEUVERS
    # -----------------------------
    print("[4] Moving forward...")
    drone.move_forward(100)
    time.sleep(2)

    print("[5] Moving right...")
    drone.move_right(100)
    time.sleep(2)

    print("[6] Moving backward...")
    drone.move_backward(100)
    time.sleep(2)

    print("[7] Moving left...")
    drone.move_left(100)
    time.sleep(2)

    # -----------------------------
    # YAW ROTATION
    # -----------------------------
    print("[8] Performing yaw rotation...")
    drone.rotate(90)
    time.sleep(2)

    # -----------------------------
    # HOVER
    # -----------------------------
    print("[9] Hovering...")
    time.sleep(3)

    # -----------------------------
    # LAND
    # -----------------------------
    print("[10] Landing...")
    drone.land()

    print("================================")
    print("       MISSION COMPLETE")
    print("================================")


if __name__ == "__main__":
    main()