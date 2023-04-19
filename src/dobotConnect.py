from serial.tools import list_ports

import pydobot


class RobotControl:
    def __init__(self):
        available_ports = list_ports.comports()
        print(f'available ports: {[x.device for x in available_ports]}')
        port_for_bot = available_ports[1].device
        print(f'port we are using: {port_for_bot}')
        port = port_for_bot
        self.device = pydobot.Dobot(port=port, verbose=True)

    def turn_off(self):
        self.device.close()

    def move_arm(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
        self.device.move_to(x + 20, y, z, r, wait=False)
        self.device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing

    def close_coffee_machine(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
        self.device.move_to(40, -220, 140, r, wait=False)
        self.device.move_to(50, -270, 120, r, wait=True)
        self.device.move_to(40, -220, 140, r, wait=True)
        self.device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing

    def close_hand(self):
        self.device.grip(True)

    def open_hand(self):
        self.device.grip(False)



## Notes:
## z upper bound: ~160