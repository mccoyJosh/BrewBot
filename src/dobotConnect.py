from serial.tools import list_ports

import pydobot


class RobotControl:
    def __init__(self):
        available_ports = list_ports.comports()
        print(f'available ports: {[x.device for x in available_ports]}')
        port_for_bot = available_ports[0].device
        print(f'port we are using: {port_for_bot}')
        port = port_for_bot
        self.device = pydobot.Dobot(port=port, verbose=True)

    def turn_off(self):
        self.device.close()

    def go_home(self):
        self.device.move_to(166, 0, 38, 77, wait=True)

    def pull_cart_out(self):
        self.device.move_to(218, -59, -79, 77, wait=True)
        self.device.move_to(218, -59, -112, 77, wait=True)
        self.device.suck(True)
        self.device.move_to(218, -59, -105, 77, wait=True)
        self.device.move_to(234, 174, -105, 77, wait=True)
        self.device.suck(False)
        self.device.move_to(234, 174, 9, 77, wait=True)

    def put_cart_in(self):
        self.device.move_to(234, 174, 9, 77, wait=True)
        self.device.move_to(234, 174, -110, 77, wait=True)
        self.device.suck(True)
        self.device.move_to(234, 174, -105, 77, wait=True)
        self.device.move_to(218, -59, -105, 77, wait=True)
        self.device.suck(False)
        self.device.move_to(218, -59, -79, 77, wait=True)

    def put_pod_in_machine(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(205, -47, 63, r, wait=True)
        self.device.move_to(223, -71, 162, r, wait=True)
        self.device.move_to(227, -107, 162, r, wait=True)
        self.device.move_to(221, -124, 155, r, wait=True)
        self.device.move_to(230, -162, 136, r, wait=True)
        self.device.move_to(234, -169, 136, r, wait=True)
        self.device.suck(False)

    def get_drink_columbian(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(205, 206, 28, r, wait=True)
        self.device.move_to(63, 231, -100, r, wait=True)
        self.device.move_to(63, 231, -133, r, wait=True)
        self.device.suck(True)
        self.device.move_to(63, 231, -100, r, wait=True)
        self.device.move_to(205, 206, 28, r, wait=True)

    def get_drink_jmc(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(205, 206, 28, r, wait=True)
        self.device.move_to(-14, 231, -100, r, wait=True)
        self.device.move_to(-14, 231, -133, r, wait=True)
        self.device.suck(True)
        self.device.move_to(-14, 231, -100, r, wait=True)
        self.device.move_to(205, 206, 28, r, wait=True)

    def get_drink_tea(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(205, 206, 28, r, wait=True)
        self.device.move_to(-102, 231, -100, r, wait=True)
        self.device.move_to(-102, 231, -130, r, wait=True)
        self.device.suck(True)
        self.device.move_to(-102, 231, -100, r, wait=True)
        self.device.move_to(205, 206, 28, r, wait=True)

    def open_single_serve(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(136, -73, -31, r, wait=True)
        self.device.move_to(132, -93, -31, r, wait=True)
        self.device.move_to(138, -109, -31, r, wait=True)
        self.device.move_to(138, -109, 20, r, wait=True)
        self.device.move_to(138, -109, -31, r, wait=True)
        self.device.move_to(132, -93, -31, r, wait=True)
        self.device.move_to(136, -73, -31, r, wait=True)

    def close_single_serve(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(136, -73, -31, r, wait=True)
        # TODO finish implementing

    def place_pod_in_single_serve(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(230, 0, 38, r, wait=True)
        self.device.move_to(230, -40, 32, r, wait=True)
        self.device.move_to(230, -40, 127, r, wait=False)
        self.device.move_to(234, -67, 162, r, wait=True)
        self.device.move_to(231, -99, 162, r, wait=True)
        self.device.move_to(231, -111, 160, r, wait=True)
        self.device.move_to(231, -127, 157, r, wait=True)
        self.device.move_to(230, -151, 147, r, wait=True)
        self.device.move_to(218, -160, 137, r, wait=False)
        #self.device.move_to(240, -160, 137, r, wait=True)
        self.device.move_to(240, -165, 134, r, wait=True)
        self.device.suck(False)
        self.device.move_to(218, 0, 137, r, wait=True)
        self.device.move_to(218, 0, 38, r, wait=True)

    def turn_on_machine(self):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(195, -47, 38, r, wait=True)
        self.device.move_to(186, -65, 38, r, wait=True)
        self.device.move_to(186, -65, -48, r, wait=True)
        self.device.move_to(144, -73, -48, r, wait=True)
        self.device.move_to(136, -73, -31, r, wait=True)
        self.device.move_to(132, -93, -31, r, wait=True)
        self.device.move_to(150, -93, -31, r, wait=True)
        self.device.move_to(132, -93, -31, r, wait=True)
        self.device.move_to(132, -74, -32, r, wait=True)
        self.device.move_to(157, -78, -32, r, wait=True)
        self.device.move_to(132, -74, -32, r, wait=True)
        self.device.move_to(152, -63, -32, r, wait=True)
        self.device.move_to(166, -57, -32, r, wait=True)
        self.device.move_to(166, 0, -32, r, wait=True)


'''
Notes:
z upper bound: ~160
----------------------------
Important positions
    Base Place: X:166 Y:0 Z:38
    
    Cart Pull: Z: -108
    
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
