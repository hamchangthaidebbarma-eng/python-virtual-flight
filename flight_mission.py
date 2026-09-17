import os
import time

from pysimverse import Drone


def create_drone():
    """Create a PySimVerse drone using environment-configurable endpoints."""
    return Drone(
        host=os.getenv("PYSIMVERSE_HOST", "*"),
        cmd_port=int(os.getenv("PYSIMVERSE_COMMAND_PORT", "5550")),
        state_port=int(os.getenv("PYSIMVERSE_STATE_PORT", "5556")),
        video_port=int(os.getenv("PYSIMVERSE_VIDEO_PORT", "5557")),
    )


def main():
    print("================================")
    print("   PYSIMVERSE DRONE MISSION")
    print("================================")

    # Create drone
    drone = create_drone()

    try:
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
    finally:
        drone.shutdown()

    print("================================")
    print("       MISSION COMPLETE")
    print("================================")


if __name__ == "__main__":
    main()