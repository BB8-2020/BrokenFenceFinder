# -*- coding: UTF-8 -*-

import olympe
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing

DRONE_IP = "192.168.42.1"

olympe.log.update_config({"loggers": {"olympe": {"level": "INFO"}}})


def main():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    drone.disconnect()


if __name__ == "__main__":
    main()