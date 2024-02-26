from tkinter import *

import os



window = Tk()

window.geometry('1400x810')

window.title("Project")





# canvas = Canvas(window, width=1920, height=1080)

# canvas.pack()



# canvas.create_rectangle(250, 100, 1920, 1080, fill="gray")



class MyGUI:

    def __init__(self,canvas):

        self.canvas=canvas

        self.window_title="project"

        self.buttons = []

        self.arrows = []

        self.skip_lst = []

        self.retrace_lst = [] 

        self.floorplan_lst=["FP Rules Check","Base BRC Check","ZWLM Timing"] 
        self.floorplan_buttons=[] 

        self.placement_lst=["check place","place flat sta"]
        self.floorplan_buttons=[]  

        self.cts_lst=["CTS Flat Sta","CTS QOR report"]
        self.cts_buttons=[]

        self

        self.files = [
            "run_init_Done", 'run_floor_planning_Done', "run_power_planning_Done",
            "run_placement_Done",
            "run_cts_Done",
            "run_route_Done"
            
        ]
        self.lst = ["DesignInit", 'Floorplan' , "Powerplan", 
                     "Placement",   "CTS","CTS Hold",
                     "Route","Route Opt","IR DROP","PhyV DRC/LVS","ReRoute STA"]

        self.stages = {0: [0, 1], 2: [2, 3, 4], 5: [5, 6, 7], 8: [8, 9, 10], 11: [11, 12], 13: [13, 14]}

        self.arrow_stages = {0: [0], 2: [2, 3], 5: [5, 6], 8: [8, 9], 11: [11], 13: [13]}

        self.widgets = []  # Store widgets of this tab



    def display_widgets(self): 

        #synth = Button(self.canvas, text="Sythesized Netlist", bg="DeepSkyBlue2", fg="white", width=20, height=1,font=('Arial',10))

        #synth.place(x=550, y=110)

        #self.widgets.append(synth)

        #line=self.canvas.create_line(650,135,650,190)

        #self.arrows.append(line)

        #line=self.canvas.create_line(650,190,850,190,arrow=LAST)

        #self.arrows.append(line)

        

 



        #des = Button(self.canvas, text="Design Constraints", bg="DeepSkyBlue2", fg="white", width=20, height=1,font=('Arial',10))

        #des.place(x=750, y=110)   

        #self.widgets.append(des)



        #line=self.canvas.create_line(900,135,900,180, arrow=LAST)

        #self.arrows.append(line)





        #std = Button(self.canvas, text="Std. Cell Library", bg="DeepSkyBlue2",fg="white", width=20, height=1,font=('Arial',10))

        #std.place(x=950, y=110)

        #self.widgets.append(std)

        #line=self.canvas.create_line(980,135,980,180, arrow=LAST)

        #self.arrows.append(line)





        #other = Button(self.canvas, text="Other files", bg="DeepSkyBlue2",fg="white", width=20, height=1,font=('Arial',10))

        #other.place(x=1150, y=110)

        #self.widgets.append(other)

        #line=self.canvas.create_line(1250,135,1250,190)

        #self.arrows.append(line)

        #line=self.canvas.create_line(1250,190,1020,190,arrow=LAST)  

        #self.arrows.append(line)



        for i in range(len(self.lst)): 
            if i>=8:
                btn = Button(self.canvas, text=f"{self.lst[i]}", bg="white", fg="black", width=15, height=1, font=('Arial', 10))
                btn.place(x=500+(i-8)*250, y=680)

                btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id))
                self.widgets.append(btn)
            else:

                btn = Button(self.canvas, text=f"{self.lst[i]}", bg="white", fg="black", width=15, height=1, font=('Arial', 10))

                btn.place(x=750, y=120 + 70 * i)

                btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id))

                self.buttons.append(btn)

                self.widgets.append(btn)



            if i < len(self.lst) - 3:

                line = self.canvas.create_line(810, 120+30*i, 810, 190+70*i, arrow=LAST)  #(x1,y1) (x2,y2)

                self.arrows.append(line)    
            else:
            	line = self.canvas.create_line(810, 655, 560,655)  #(x1,y1) (x2,y2)
            	self.arrows.append(line)  
            	line = self.canvas.create_line(560, 655, 560,680, arrow=LAST)  #(x1,y1) (x2,y2)

            	self.arrows.append(line)  

            	line = self.canvas.create_line(810, 655, 1050,655)  #(x1,y1) (x2,y2)

            	self.arrows.append(line)  

            	line = self.canvas.create_line(1050, 655, 1050,680, arrow=LAST)  #(x1,y1) (x2,y2)

            	self.arrows.append(line) 
        

        for i in range(len(self.floorplan_lst)): 
            line = self.canvas.create_line(810, 230, 440,230)  #(x1,y1) (x2,y2)

            self.arrows.append(line)  

            line = self.canvas.create_line(440, 230, 440,250, arrow=LAST)  #(x1,y1) (x2,y2)

            self.arrows.append(line)  

            line = self.canvas.create_line(600, 230, 600,250, arrow=LAST)  #(x1,y1) (x2,y2)

            self.arrows.append(line)  

            line = self.canvas.create_line(810, 230, 1040,230)  #(x1,y1) (x2,y2)

            self.arrows.append(line) 

            line = self.canvas.create_line(1040, 230, 1040,250, arrow=LAST)  #(x1,y1) (x2,y2)

            self.arrows.append(line) 

            if i<2:
                btn = Button(self.canvas, text=f"{self.floorplan_lst[i]}", bg="white", fg="black", width=15, height=1, font=('Arial', 10))
                btn.place(x=400+i*150, y=250)

                #btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id)) 
            else:
                btn = Button(self.canvas, text=f"{self.floorplan_lst[i]}", bg="white", fg="black", width=15, height=1, font=('Arial', 10))
                btn.place(x=960, y=250)

                #btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id))
            self.widgets.append(btn)


        for i in range(len(self.placement_lst)):

            line = self.canvas.create_line(810, 370, 640,370)  #(x1,y1) (x2,y2)

            self.arrows.append(line)  

            line = self.canvas.create_line(640, 370, 640,390, arrow=LAST)  #(x1,y1) (x2,y2)

            self.arrows.append(line)  

            line = self.canvas.create_line(810,370, 1040,370)  #(x1,y1) (x2,y2)

            self.arrows.append(line) 

            line = self.canvas.create_line(1040, 370, 1040,390, arrow=LAST)  #(x1,y1) (x2,y2)

            self.arrows.append(line) 

            if i==0:
                btn = Button(self.canvas, text=f"{self.placement_lst[i]}", bg="white", fg="black", width=15, height=1, font=('Arial', 10))
                btn.place(x=550, y=390)

                #btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id)) 
            else:
                btn = Button(self.canvas, text=f"{self.placement_lst[i]}", bg="white", fg="black", width=15, height=1, font=('Arial', 10))
                btn.place(x=960, y=390)

                #btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id))
            self.widgets.append(btn)

        for i in range(len(self.cts_lst)):

            line = self.canvas.create_line(810,510, 1170,510)  #(x1,y1) (x2,y2)

            self.arrows.append(line) 

            line = self.canvas.create_line(1020, 510, 1020,530, arrow=LAST)  #(x1,y1) (x2,y2)

            self.arrows.append(line) 

            line = self.canvas.create_line(1170, 510, 1170,530, arrow=LAST)  #(x1,y1) (x2,y2)

            self.arrows.append(line) 

            btn = Button(self.canvas, text=f"{self.cts_lst[i]}", bg="white", fg="black", width=15, height=1, font=('Arial', 10))
            btn.place(x=960+i*150, y=530)
            self.widgets.append(btn)

                #btn.bind("<Button-1>",lambda event,button_id=i: self.on_single_click(event,button_id)) 

  
       



    def clear_widgets(self):

        for widget in self.widgets:

            widget.destroy()

        for arrow in self.arrows:

            self.canvas.delete(arrow)  # Delete arrows

        self.widgets = []

        self.arrows = [] 

        

        

    def on_single_click(self,event,button_id):

        self.window_title=f"{self.lst[button_id]}"  

        window.title(self.window_title)

        print(self.window_title)

        for j in range(len(self.lst)):

            self.buttons[j].config(bg="white")

        function(self,button_id)

    

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

            btn.bind("<Button-1>")

            self.buttons.append(btn)

            self.widgets.append(btn)



    def clear_widgets(self):

        for widget in self.widgets:

            widget.destroy()

        self.widgets = [] 









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
