from tkinter import * 
from gui_design import MyGUI,Tab2
import os
from tkinter import ttk

window = Tk()
window.geometry('1920x1080')
window.title("Project")



# Create an instance of MyGUI


canvas = Canvas(window, width=1920, height=1080)
canvas.pack()

canvas.create_rectangle(250,100, 1920, 1080, fill="gray")

level1_lst=['Console','Project','Slaves','Sets','View',"Node","Trace","Tools","Help"]
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
        
level2_lst=['Console','Project','Slaves','Sets','View',"Node"]
level2_btn=[]
for i in range(len(level2_lst)): 
    btn = Button(canvas, text=f"{level2_lst[i]}", bg="green",fg="black", width=25, height=1,font=('Arial',10))
    btn.place(x=10+200*i, y=30)  
    level2_btn.append(btn)
    

level3_lst=['Sets',"Directories"]
level3_btn=[]
for i in range(len(level3_lst)): 
    btn = Button(canvas, text=f"{level3_lst[i]}", bg="blue",fg="black", width=25, height=1,font=('Arial',10))
    btn.place(x=10+200*i, y=60)  
    level3_btn.append(btn)



    
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
    arrow_color(self,button_id)
    

def run(self,block_name):
    print(self.window_title)
    try:
        button_id=self.lst.index(block_name)
    except ValueError:
        button_id = -1 
    
    directory="/home/lingareddy/project"
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
                print(f"........executed {filename} ......... ")
                os.system(f"touch {filename}")     
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



# def skip(block_name):
#     try:
#         button_id=lst.index(block_name)
#     except ValueError:
#         button_id = -1 
#     skip_lst.append(button_id)
#     filename=f"/home/lingareddy/project/{files[button_id]}"
#     os.system(f"touch {filename}")
#     function(button_id)
    

# def retrace(self,block_name): 
#     try:
#         button_id=self.lst.index(block_name)
#     except ValueError:
#         button_id = -1 
#     self.retrace_lst.append(button_id)

flowchart = MyGUI(canvas)
tab2 = Tab2(canvas)

current_tab = flowchart

def show_my_gui():
    global current_tab
    # flowchart = MyGUI(canvas)
    if current_tab != flowchart:
        current_tab.clear_widgets()  # Clear widgets of the current tab
        # del current_tab 
        current_tab = flowchart
        current_tab.display_widgets()

def show_tab2():
    global current_tab
    # tab2 = Tab2(canvas)
    if current_tab != tab2:
        current_tab.clear_widgets()  # Clear widgets of the current tab 
        # del current_tab
        current_tab = tab2
        current_tab.display_widgets()

current_tab.display_widgets()




my_gui_button = Button(canvas, text="Show My GUI", command=show_my_gui)

my_gui_button.place(x=450, y=60)

tab2_button = Button(canvas, text="Show Tab2", command=show_tab2)
tab2_button.place(x=550, y=60)   

def change_title():
    window.title(current_tab.window_title)

change_button = Button(canvas, text="change title", command=change_title)
change_button.place(x=650, y=60) 


def on_single_click(self,event,button_id):
    window.title(f"{self.lst[button_id]}")
        
    self.window_title=self.lst[button_id]
    for j in range(len(self.lst)):
        self.buttons[j].config(bg="white")
    # function(self,button_id) 




run_image = PhotoImage(file=os.path.join('gifs', 'run.gif'))  
run_image = run_image.subsample(5)  # Increase the value to make it smaller or decrease to make it larger
run_btn = Button(window, image=run_image, command=lambda:run(current_tab,current_tab.window_title))
run_btn.place(x=1260,y=60)   # change to 1760 in linux

skip_image = PhotoImage(file="gifs/skip.gif")  
skip_image = skip_image.subsample(7)  
skip_btn = Button(window, image=skip_image) #command=lambda:skip(window.title())
skip_btn.place(x=1300,y=60)

retrace_image = PhotoImage(file="gifs/retrace.gif")  
retrace_image = retrace_image.subsample(7) 
retrace_btn = Button(window, image=retrace_image) #command=lambda:retrace(window.title())
retrace_btn.place(x=1340,y=60)

stop_image = PhotoImage(file="gifs/stop.gif")  
stop_image = stop_image.subsample(7)  
stop_btn = Button(window, image=stop_image, command=lambda: print("Button clicked"))
stop_btn.place(x=1380,y=60)






# Create a frame to contain the Treeview and scrollbar
frame = Frame(window)  
frame.place(x=10, y=100)

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

directory_path = r"c:\\Users\\linga\\OneDrive\\Desktop\\GUI_Project\\"   # Replace with the directory path you want to create the structur 

def update_tree():
    data = create_directory_structure(directory_path) 
    # print(data)
    insert_tree('', data)
    treeview.bind('<ButtonRelease-1>', on_item_click)  # Bind a click event

update_tree()

treeview.column("#0", width=250)


window.mainloop()
