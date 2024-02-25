from tkinter import *
import os

# window = Tk()
# window.geometry('1920x1080')
# window.title("Project")

# canvas = Canvas(window, width=1920, height=1080)
# canvas.pack()

# canvas.create_rectangle(250, 100, 1920, 1080, fill="gray")

class MyGUI:
    def __init__(self, canvas):
        self.canvas=canvas
        self.buttons = []
        self.arrows = []
        self.skip_lst = []
        self.retrace_lst = []
        self.window_title="project"
        self.files = [
            "design_init.txt", "SanityChecks_prefloor.txt", 'Floorplan.txt',
            "Pre_placement.txt", "SanityChecks_preplacement.txt", "Placement.txt",
            "PreCTSOpt.txt", "SanityChecks_prects.txt", "CTS.txt",
            "PostCTSOpt.txt", "SanityChecks_preRoute.txt", "Route.txt",
            "PostPostOpt.txt", "SignOff.txt", "GDSOASIS.txt"
        ]
        self.lst = ["Design_Init", "Sanity Checks-1", 'Floorplan', "Pre placement",
                    "Sanity Checks-2", "Placement", "Pre CTS Opt", "Sanity Checks-3", "CTS",
                    "Post CTS Opt", "Sanity Checks-4", "Route", "Post Post Opt", "SignOff", "GDS/OASIS"]
        self.stages = {0: [0, 1], 2: [2, 3, 4], 5: [5, 6, 7], 8: [8, 9, 10], 11: [11, 12], 13: [13, 14]}
        self.arrow_stages = {0: [0], 2: [2, 3], 5: [5, 6], 8: [8, 9], 11: [11], 13: [13]}
        self.widgets = []  # Store widgets of this tab

    def display_widgets(self): 
        synth = Button(self.canvas, text="Sythesized Netlist", bg="DeepSkyBlue2", fg="white", width=20, height=1,font=('Arial',10))
        synth.place(x=550, y=110)
        self.widgets.append(synth)
        line=self.canvas.create_line(650,135,650,190)
        self.arrows.append(line)
        line=self.canvas.create_line(650,190,850,190,arrow=LAST)
        self.arrows.append(line)
        
 

        des = Button(self.canvas, text="Design Constraints", bg="DeepSkyBlue2", fg="white", width=20, height=1,font=('Arial',10))
        des.place(x=750, y=110)   
        self.widgets.append(des)

        line=self.canvas.create_line(900,135,900,180, arrow=LAST)
        self.arrows.append(line)


        std = Button(self.canvas, text="Std. Cell Library", bg="DeepSkyBlue2",fg="white", width=20, height=1,font=('Arial',10))
        std.place(x=950, y=110)
        self.widgets.append(std)
        line=self.canvas.create_line(980,135,980,180, arrow=LAST)
        self.arrows.append(line)


        other = Button(self.canvas, text="Other files", bg="DeepSkyBlue2",fg="white", width=20, height=1,font=('Arial',10))
        other.place(x=1150, y=110)
        self.widgets.append(other)
        line=self.canvas.create_line(1250,135,1250,190)
        self.arrows.append(line)
        line=self.canvas.create_line(1250,190,1020,190,arrow=LAST)  
        self.arrows.append(line)

        for i in range(len(self.lst)):
            btn = Button(self.canvas, text=f"{self.lst[i]}", bg="white", fg="black", width=20, height=1, font=('Arial', 10))
            btn.place(x=850, y=180 + 40 * i)
            btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id))
            self.buttons.append(btn)
            self.widgets.append(btn)

            if i < len(self.lst) - 1:
                line = self.canvas.create_line(935, 190 + i * 40, 935, 220 + i * 40, arrow=LAST)
                self.arrows.append(line)

    def clear_widgets(self):
        for widget in self.widgets:
            widget.destroy()
        for arrow in self.arrows:
            self.canvas.delete(arrow)  # Delete arrows
        self.widgets = []
        self.arrows = [] 
        
        
    def on_single_click(self,event,button_id):
        # window.title(f"{self.lst[button_id]}")
        
        self.window_title=self.lst[button_id]
        for j in range(len(self.lst)):
            self.buttons[j].config(bg="white")
        function(self,button_id) 
        
        # return button_id
    
def function(self,button_id): 
#    print(button_id)
    directory = "/home/lingareddy/project"
    for i in range(button_id+1):
        file_name=self.files[i]
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            self.buttons[i].config(bg="green")
            if i in self.skip_lst:
                self.buttons[i].config(bg="yellow")  
        else:
            self.buttons[i].config(bg="red")
    # arrow_color(self,button_id)


class Tab2:
    lst = [1, 2, 3, 4]
    
    def __init__(self, canvas):
        self.canvas=canvas
        self.buttons = []
        self.widgets = []  # Store widgets of this tab

    def display_widgets(self):

        for i in range(len(self.lst)):
            btn = Button(self.canvas, text=f"{self.lst[i]}", bg="white", fg="black", width=20, height=1, font=('Arial', 10))
            btn.place(x=850, y=180 + 40 * i)
            btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id))
            self.buttons.append(btn)
            self.widgets.append(btn)

    def clear_widgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = [] 
        
    def on_single_click(self,event,button_id):
        for j in range(len(self.lst)):
            self.buttons[j].config(bg="white")
        self.buttons[button_id].config(bg="green")
        # function(self,button_id) 




# my_gui = MyGUI(canvas)
# tab2 = Tab2(canvas)

# current_tab = my_gui

# def show_my_gui():
#     global current_tab
#     if current_tab != my_gui:
#         current_tab.clear_widgets()  # Clear widgets of the current tab
#         current_tab = my_gui
#         current_tab.display_widgets()

# def show_tab2():
#     global current_tab
#     if current_tab != tab2:
#         current_tab.clear_widgets()  # Clear widgets of the current tab
#         current_tab = tab2
#         current_tab.display_widgets()

# my_gui.display_widgets()

# my_gui_button = Button(canvas, text="Show My GUI", command=show_my_gui)
# my_gui_button.place(x=20, y=20)

# tab2_button = Button(canvas, text="Show Tab2", command=show_tab2)
# tab2_button.place(x=140, y=20)

# window.mainloop()
