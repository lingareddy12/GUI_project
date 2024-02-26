from tkinter import * 

from gui_design import MyGUI,Tab2,window

import os
import subprocess
from tkinter import ttk



#window = Tk()

#window.geometry('1920x1080')

#window.title("Project")







# Create an instance of MyGUI





canvas = Canvas(window, width=1920, height=1080)

canvas.pack()



canvas.create_rectangle(250,80, 1920, 1080, fill="gray")



level1_lst=['Console','Project',"Node","Tools","Help"]

level1_btn=[]



for i in range(len(level1_lst)): 

    if(i==len(level1_lst)-1):

        btn = Button(canvas, text=f"{level1_lst[i]}", bg="white",fg="black", width=10, height=1,font=('Arial',10))

        btn.place(x=1830, y=0)  

        level1_btn.append(btn)

    else:   

        btn = Button(canvas, text=f"{level1_lst[i]}", bg="white",fg="black", width=10, height=1,font=('Arial',10))

        btn.place(x=10+90*i, y=0)  

        level1_btn.append(btn)

        

#level2_lst=['Console','Project','Slaves','Sets','View',"Node"]

#level2_btn=[]

#for i in range(len(level2_lst)): 

#    btn = Button(canvas, text=f"{level2_lst[i]}", bg="green",fg="black", width=25, height=1,font=('Arial',10))

#    btn.place(x=10+200*i, y=30)  

#    level2_btn.append(btn)

    



#level3_lst=['Sets',"Directories"]

#level3_btn=[]

#for i in range(len(level3_lst)): 

#    btn = Button(canvas, text=f"{level3_lst[i]}", bg="blue",fg="black", width=25, height=1,font=('Arial',10))

#    btn.place(x=10+200*i, y=60)  

#    level3_btn.append(btn)







    

def function(self,button_id): 

    #print(button_id)

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

#     arrow_color(self,button_id) 

    

file_name=["run_init.tcl", "run_floor_planning.tcl", "run_power_planning.tcl", "run_placement.tcl", "run_cts.tcl", "run_route.tcl"]
files=["run_init", "run_floor_planning", "run_power_planning", "run_placement", "run_cts", "run_route"]


#def change_color():

 
def run(self,block_name):
    print(self.window_title)
    try:
        button_id=self.lst.index(block_name)
    except ValueError:
        button_id = -1 
    
    directory="/home/lavbok/work/cdns/designs/Quest_INV_Proj_1/Innovus_IEEE1801/FB_GUI"
    print(self.files)
    for i in range(button_id+1):
        filename=self.files[i]
        path=os.path.join(directory,filename)
        if len(self.retrace_lst)!=0 and i>=self.retrace_lst[0] and i<=button_id :
            if  os.path.exists(path)==False:
                pass
            else:
                os.system(f"rm {self.files[i]}")
                print(f"removed {self.files[i]}")
                     
 
        if i not in self.skip_lst:
            if  os.path.exists(path)==False:
                print(path)
                print(f"........executed {filename} ......... ") 
                if i==0:
                    #result=subprocess.Popen(f"innovus -no_gui -log LOG/{files[i]}.log -files ../SCRIPTS/{file_name[i]} &", cwd=directory, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
                    output, err= result.communicate()
                    print(f"this is result ")
                    print(output)
   
 
                else: 
                    prev=self.files[i-1]
                    prev_path=os.path.join(directory,prev)
                    if os.path.exists(prev_path)==True and i!=0:
                       print(f"........executed ......... ")
                       result=subprocess.Popen(f"innovus -no_gui -log LOG/{files[i]}.log -files ../SCRIPTS/{file_name[i]} &", cwd=directory, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE ) 
                       output, err= result.communicate() 
            else:
                pass    
        else:
            print(f"........skipped {filename}.........")
    self.retrace_lst=[] 
    function(self,button_id) 
    treeview.delete(*treeview.get_children())
    update_tree()





def arrow_color(self,button_id):          

    for i in range(len(self.lst)):

        if i<button_id: 

            canvas.itemconfig(self.arrows[i],fill="blue")

        elif i<len(self.lst)-1:

            canvas.itemconfig(self.arrows[i],fill="black")        





def skip(self,block_name):

    try:

        button_id=self.lst.index(block_name)

    except ValueError:

        button_id = -1 

    

    self.skip_lst.append(button_id)

    filename=f"/home/lingareddy/project/{self.files[button_id]}"

    os.system(f"touch {filename}")

    function(self,button_id) 

    treeview.delete(*treeview.get_children())

    update_tree()

    



def retrace(self,block_name): 

    try:

        button_id=self.lst.index(block_name)

    except ValueError:

        button_id = -1 

    self.retrace_lst.append(button_id)

    treeview.delete(*treeview.get_children())

    update_tree()



flowchart = MyGUI(canvas)

tab2 = Tab2(canvas)



current_tab = flowchart



def show_my_gui():

    global current_tab

    flowchart = MyGUI(canvas)

    if current_tab != flowchart:

        current_tab.clear_widgets()  # Clear widgets of the current tab

        del current_tab

        current_tab = flowchart

        current_tab.display_widgets()



print(current_tab.window_title)



def show_tab2():

    global current_tab

    tab2 = Tab2(canvas)

    if current_tab != tab2:

        current_tab.clear_widgets()  # Clear widgets of the current tab 

        del current_tab

        current_tab = tab2

        current_tab.display_widgets()



current_tab.display_widgets()



my_gui_button = Button(canvas, text="Show My GUI", command=show_my_gui,height=2)



my_gui_button.place(x=200, y=30)



tab2_button = Button(canvas, text="Show Tab2", command=show_tab2,height=2)

tab2_button.place(x=300, y=30)   







run_image = PhotoImage(file=os.path.join('gifs', 'run.gif'))  

run_image = run_image.subsample(5)  # Increase the value to make it smaller or decrease to make it larger

run_btn = Button(window, image=run_image, command=lambda:run(current_tab,current_tab.window_title))

run_btn.place(x=10,y=30)   # change to 1760 in linux



skip_image = PhotoImage(file="gifs/skip.gif")  

skip_image = skip_image.subsample(7)  

skip_btn = Button(window, image=skip_image,command=lambda:skip(current_tab,current_tab.window_title)) 

skip_btn.place(x=50,y=30)



retrace_image = PhotoImage(file="gifs/retrace.gif")  

retrace_image = retrace_image.subsample(7) 

retrace_btn = Button(window, image=retrace_image,command=lambda:retrace(current_tab,current_tab.window_title)) #

retrace_btn.place(x=90,y=30)



stop_image = PhotoImage(file="gifs/stop.gif")  

stop_image = stop_image.subsample(7)  

stop_btn = Button(window, image=stop_image, command=lambda: print("Button clicked"))

stop_btn.place(x=120,y=30)




quest_image = PhotoImage(file="gifs/quest.gif")  

quest_image = quest_image.subsample(7)  

quest_btn = Button(window, image=quest_image, command=lambda: print("Button clicked"))

quest_btn.place(x=1290,y=25)













# Create a frame to contain the Treeview and scrollbar

frame = Frame(window)  

frame.place(x=10, y=80)



# Create a vertical scrollbar 

scrollbar = ttk.Scrollbar(frame, orient="vertical")

scrollbar.pack(side="right", fill="y")



# Create a Treeview with the yscrollcommand set to the scrollbar

treeview = ttk.Treeview(frame, yscrollcommand=scrollbar.set)

treeview.config(height=40)

treeview.pack(side="right")



# Attach the scrollbar to the Treeview

scrollbar.config(command=treeview.yview)



def create_directory_structure(path):

    structure = {}

    for item in os.listdir(path):

        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):

            structure[item] = create_directory_structure(item_path)

        else:

            structure[item] = None

    return structure



def insert_tree(parent, item):

    if item is None:

        return

    for key, value in item.items():

        node = treeview.insert(parent, 'end', text=key)

        insert_tree(node, value)



def on_item_click(event):

    item = treeview.selection()

    if item:

        text = treeview.item(item, 'text')

        print(f"Clicked on: {text}")



directory_path = "/home/lingareddy/project"   # Replace with the directory path you want to create the structur 



def update_tree():

    data = create_directory_structure(directory_path)

    insert_tree('', data)

    treeview.bind('<ButtonRelease-1>', on_item_click)  # Bind a click event



update_tree()



treeview.column("#0", width=250)





window.mainloop()
