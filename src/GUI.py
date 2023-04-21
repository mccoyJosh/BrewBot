import tkinter as tk
import tkinter.font as tk_font
import dobotConnect as dC


class GUI:
    def __init__(self, root):
        self.robot = dC.RobotControl()

        # setting title
        root.title("Brew Bot Window")
        # setting window size
        width = 600
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        request_label = tk.Label(root)
        request_label["bg"] = "#009688"
        ft = tk_font.Font(family='Times', size=10)
        request_label["font"] = ft
        request_label["fg"] = "#333333"
        request_label["justify"] = "center"
        request_label["text"] = "Please enter name and select brew"
        request_label.place(x=190, y=50, width=200, height=25)

        jamaican_button = tk.Button(root)
        jamaican_button["bg"] = "#90ee90"
        ft = tk_font.Font(family='Times', size=10)
        jamaican_button["font"] = ft
        jamaican_button["fg"] = "#000000"
        jamaican_button["justify"] = "center"
        jamaican_button["text"] = "Jamacian me crazy"
        jamaican_button.place(x=240, y=130, width=100, height=25)
        jamaican_button["command"] = self.j_button_command

        test_button = tk.Button(root)
        test_button["bg"] = "#90ee90"
        ft = tk_font.Font(family='Times', size=10)
        test_button["font"] = ft
        test_button["fg"] = "#000000"
        test_button["justify"] = "center"
        test_button["text"] = "TEST in"
        test_button.place(x=400, y=260, width=60, height=25)
        test_button["command"] = self.test_command_in

        test_button = tk.Button(root)
        test_button["bg"] = "#90ee90"
        ft = tk_font.Font(family='Times', size=10)
        test_button["font"] = ft
        test_button["fg"] = "#000000"
        test_button["justify"] = "center"
        test_button["text"] = "TEST out"
        test_button.place(x=400, y=220, width=60, height=25)
        test_button["command"] = self.test_command_out

        colombian_button = tk.Button(root)
        colombian_button["bg"] = "#90ee90"
        ft = tk_font.Font(family='Times', size=10)
        colombian_button["font"] = ft
        colombian_button["fg"] = "#000000"
        colombian_button["justify"] = "center"
        colombian_button["text"] = "Colombian"
        colombian_button.place(x=240, y=170, width=100, height=25)
        colombian_button["command"] = self.c_button_command

        tea_button = tk.Button(root)
        tea_button["bg"] = "#90ee90"
        ft = tk_font.Font(family='Times', size=10)
        tea_button["font"] = ft
        tea_button["fg"] = "#000000"
        tea_button["justify"] = "center"
        tea_button["text"] = "Tea"
        tea_button.place(x=240, y=210, width=100, height=25)
        tea_button["command"] = self.t_button_command

        close_button = tk.Button(root)
        close_button["bg"] = "#90ee90"
        ft = tk_font.Font(family='Times', size=10)
        close_button["font"] = ft
        close_button["fg"] = "#000000"
        close_button["justify"] = "center"
        close_button["text"] = "Close Window"
        close_button.place(x=240, y=260, width=100, height=25)
        close_button["command"] = self.close_command

        text_field = tk.Entry(root)
        text_field["borderwidth"] = "1px"
        ft = tk_font.Font(family='Times', size=10)
        text_field["font"] = ft
        text_field["fg"] = "#333333"
        text_field["justify"] = "center"
        text_field["text"] = "Entry"
        text_field.place(x=190, y=90, width=200, height=25)

        title = tk.Label(root)
        ft = tk_font.Font(family='Times', size=16)
        title["font"] = ft
        title["fg"] = "#333333"
        title["justify"] = "center"
        title["text"] = "BrewBot: An Expresso Synthesizing Machine"
        title.place(x=100, y=10, width=400, height=25)

        self.root = root

    def j_button_command(self):
        self.robot.go_home()
        self.robot.get_drink_jmc()
        self.robot.go_home()

    def test_command_in(self):
        self.robot.go_home()
        self.robot.put_cart_in()
        self.robot.go_home()

    def test_command_out(self):
        self.robot.go_home()
        # self.robot.pull_cart_out()
        # self.robot.open_single_serve()
        self.robot.get_to_right()
        self.robot.get_to_left_not_home()
        self.robot.go_home()

    def c_button_command(self):
        self.robot.go_home()
        self.robot.get_drink_columbian()
        self.robot.go_home()

    def t_button_command(self):
        self.robot.go_home()
        self.robot.get_drink_tea()
        self.robot.go_home()

    def close_command(self):
        self.robot.turn_off()
        self.root.destroy()
