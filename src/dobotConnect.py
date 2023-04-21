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

    def go_home(self):
        self.device.move_to(166, 0, 38, 77, wait=True)

    def put_pod_in_machine(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(230, -55, 165, r, wait=True)
        self.device.move_to(222, -86, 164, r, wait=True)
        self.device.move_to(222, -104, 164, r, wait=True)
        self.device.move_to(220, -126, 161, r, wait=True)
        self.device.move_to(226, -138, 155, r, wait=True)
        self.device.move_to(230, -156, 147, r, wait=True)
        self.device.move_to(220, -126, 161, r, wait=True)
        self.device.move_to(227, -16, 138, r, wait=True)

    def get_drink_columbian(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(205, 206, 28, r, wait=True)
        self.device.move_to(63, 231, -100, r, wait=True)
        self.device.move_to(63, 231, -132, r, wait=True)
        self.device.suck(True)
        self.device.move_to(63, 231, -100, r, wait=True)
        self.device.move_to(205, 206, 28, r, wait=True)
        self.device.suck(False)

    def get_drink_jmc(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(205, 206, 28, r, wait=True)
        self.device.move_to(-14, 231, -100, r, wait=True)
        self.device.move_to(-14, 231, -132, r, wait=True)
        self.device.move_to(-14, 231, -100, r, wait=True)
        self.device.move_to(205, 206, 28, r, wait=True)


    def get_drink_tea(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(205, 206, 28, r, wait=True)
        self.device.move_to(-102, 231, -100, r, wait=True)
        self.device.move_to(-102, 231, -130, r, wait=True)
        self.device.move_to(-102, 231, -100, r, wait=True)
        self.device.move_to(205, 206, 28, r, wait=True)



    def close_hand(self):
        self.device.grip(True)

    def open_hand(self):
        self.device.grip(False)


'''
Notes:
z upper bound: ~160
----------------------------
Important positions
    Base Place: X:166 Y:0 Z:38
    
    Coffee Machine:
        
        Over lip w/ pod: Z:164
        Over lip  alone: Z:126
        
        Preloc: 230, -55, 165
        Lip Loca: X: 222 Y:-86  Z: 164
        Mid1: 222, -104, 164
        Mid2: 220, -126, 161
        Mid3: 226, -138, 155
        Drop Pod: X: 230 Y:-156 Z: 147
        out:  227 -16 138











'''
