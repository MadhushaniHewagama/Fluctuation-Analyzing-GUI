from tkinter import *
import pandas as pd
import csv
from datetime import *
import gc
import numpy as np
import pandas as pd
import xlrd
from tkinter.filedialog import askopenfile
import tkinter.messagebox
def create_window():
    root = Tk()
    root.geometry("%dx%d+0+0" % (1000,500))
    root.title("Graphical visualisation for fluctuation time frames")

    lbl1 =Label(root, text="Total high counts:",bg="dark orange",fg="black",font=('times', 16),borderwidth=3)
    lbl1.place(x=10,y=10)

    h = StringVar()
    label = Message( root, textvariable=h, width=300,bg="Snow4",fg="black",font=('times', 16),relief=RAISED)
    label.place(x=200,y=10)

    lbl2 =Label(root, text="Total low counts:",bg="SeaGreen1",fg="black",font=('times', 16),borderwidth=3)
    lbl2.place(x=10,y=50)

    l = StringVar()
    label = Message( root, textvariable=l, width=300,bg="Snow4",fg="black",font=('times', 16),relief=RAISED)
    label.place(x=200,y=50)

    t = StringVar()
    label = Message( root, textvariable=t, width=500,bg="Snow4",fg="black",font=('times', 24),relief=RAISED)
    label.place(x=300,y=250)

    label2=Label(root, text="Worning flags:",bg="Red",fg="black",font=('times', 14),borderwidth=3)
    label2.place(x=10,y=100)
    flagList=Listbox(root)
    flagList.place(x=10,y=150)
    flagList.insert(END,"no flags")    


    def getSummary(ans):
        def create_grid(event=None):
            w = c.winfo_width() # Get current width of canvas
            h = c.winfo_height() # Get current height of canvas
            c.delete('grid_line') # Will only remove the grid_line

            c.create_text(500,100,font="Times 24  underline",
                    text="Summary Report")

            x=60
            y=110
            lbl=['',"Value flucturation","Time start","Time stop","Difference in value","Count"]
            for i in range(len(lbl)):
                a=c.create_rectangle(x, y+20, x+200, y+60, fill="khaki2")
                txt=c.create_text(x+70,y+40,font="Times 10",text=lbl[i])
                x=x+200
            k=0
            y=y+40
            
            for i in ans:
                x=60
                k=k+1
                a=c.create_rectangle(x, y+20, x+200, y+60,fill="pale green")
                txt=c.create_text(x+70,y+30,font="Times 10",text=k)
                x=x+200
                a=c.create_rectangle(x, y+20, x+200, y+60,fill="bisque2")
                txt=c.create_text(x+70,y+30,font="Times 10",text=str(i[0])+'-->'+str(i[1]))
                x=x+200
                a=c.create_rectangle(x, y+20, x+200, y+60,fill="ivory2")
                txt=c.create_text(x+70,y+30,font="Times 10",text=i[2])
                x=x+200
                a=c.create_rectangle(x, y+20, x+200, y+60,fill="wheat1")
                txt=c.create_text(x+70,y+30,font="Times 10",text=i[3])
                x=x+200
                a=c.create_rectangle(x, y+20, x+200, y+60,fill="thistle1")
                txt=c.create_text(x+70,y+30,font="Times 10",text=abs(float(i[0])-float(i[1])))
                x=x+200
                
                if(i[4]=='High'):
                    a=c.create_rectangle(x, y+20, x+200, y+60, fill="red")
                    txt=c.create_text(x+70,y+30,font="Times 10",text=i[4])
                else:
                    a=c.create_rectangle(x, y+20, x+200, y+60, fill="green")
                    txt=c.create_text(x+70,y+30,font="Times 10",text=i[4])
                x=x+200
                y=y+40
        # root.destroy()
        root1=Tk()
        root1.title("Summary Report")
        w, h = root1.winfo_screenwidth(), root1.winfo_screenheight()
        root1.geometry("%dx%d+0+0" % (w, h))
        c = Canvas(root1, height=h, width=w, bg='white',scrollregion=(0,0,w,10000))
        c.pack(side=LEFT,expand=True,fill=BOTH)

        scrollbar = Scrollbar(c)
        scrollbar.pack( side = RIGHT, fill = Y )
        scrollbar.config(command=c.yview)
        c.config(yscrollcommand=scrollbar.set)
        c.bind('<Configure>', create_grid)     
        c.update()
        root1.mainloop()

    def getSummaryFlag(all_flag_lst):
        def create_grid(event=None):
            w = c.winfo_width() # Get current width of canvas
            h = c.winfo_height() # Get current height of canvas
            c.delete('grid_line') # Will only remove the grid_line

            c.create_text(500,100,font="Times 24  underline",
                    text="Summary Flag Report")
            x=60
            y=110
            lbl=['',"Time start","Time stop","Flag"]
            for i in range(len(lbl)):
                a=c.create_rectangle(x, y+20, x+300, y+60, fill="khaki2")
                txt=c.create_text(x+70,y+40,font="Times 10",text=lbl[i])
                x=x+300
            k=0
            y=y+40
            for i in all_flag_lst:
                x=60
                k=k+1
                # print(i)
                a=c.create_rectangle(x, y+20, x+300, y+60,fill="linen")
                txt=c.create_text(x+70,y+30,font="Times 10",text=k)
                x=x+300
                a=c.create_rectangle(x, y+20, x+300, y+60,fill="pale green")
                txt=c.create_text(x+70,y+30,font="Times 10",text=i[0])
                x=x+300
                a=c.create_rectangle(x, y+20, x+300, y+60,fill="snow2")
                txt=c.create_text(x+70,y+30,font="Times 10",text=i[1])
                x=x+300
                if(i[2]=="5 or more high counts"):
                    a=c.create_rectangle(x, y+20, x+300, y+60,fill="SteelBlue1")
                    txt=c.create_text(x+70,y+30,font="Times 10",text=i[2])
                elif(i[2]=="7 or more low counts"):
                    a=c.create_rectangle(x, y+20, x+300, y+60,fill="DarkSlategray1")
                    txt=c.create_text(x+70,y+30,font="Times 10",text=i[2])
                elif(i[2]=="High counts >=3 & Low counts >= 2"):
                    a=c.create_rectangle(x, y+20, x+300, y+60,fill="RosyBrown1")
                    txt=c.create_text(x+70,y+30,font="Times 10",text=i[2])
                elif(i[2]=="High counts >=2 & low counts >= 3"):
                    a=c.create_rectangle(x, y+20, x+300, y+60,fill="khaki")
                    txt=c.create_text(x+70,y+30,font="Times 10",text=i[2])
                elif(i[2]=="High count >= 1 & low count >= 5"):
                    a=c.create_rectangle(x, y+20, x+300, y+60,fill="OliveDrab1")
                    txt=c.create_text(x+70,y+30,font="Times 10",text=i[2])
                x=x+300
                y=y+40

        root2=Tk()
        root2.title("Summary Flag Report")
        w, h = root2.winfo_screenwidth(), root2.winfo_screenheight()
        root2.geometry("%dx%d+0+0" % (w, h))
        c = Canvas(root2, height=h, width=w, bg='white',scrollregion=(0,0,w,10000))
        c.pack(side=LEFT,expand=True,fill=BOTH)

        scrollbar = Scrollbar(c)
        scrollbar.pack( side = RIGHT, fill = Y )
        scrollbar.config(command=c.yview)
        c.config(yscrollcommand=scrollbar.set)
        c.bind('<Configure>', create_grid)     
        c.update()
        root2.mainloop()

    

    def read_csv(file):
        c_t=None
        s_t=None    
        prev_dt = None
        prev=None
        start_flag=True
        ans=[]
        all_flag_lst=[]
        h_count=0
        l_count=0
        k=0
        t_name=input("Enter time feild name(Case sensitive) default: Hour:min:sec.msec : ")
        v_name = input ("Enter value feild (Case sensitive) default: : Value ")
        s=len(open(file.name).readlines())
        with open(file.name) as csvfile:            
            reader = csv.DictReader(csvfile)
            for row in reader:
                k=k+1
                null_feild=False
                
                if(t_name==""):
                    t_name="Hour:min:sec.msec"
                if(v_name==""):
                   v_name= "Value"                    
                time=row[t_name]
                value=row[v_name]    
                dt = datetime.strptime(time, '%H:%M:%S.%f')           
                c_t=dt
                if(start_flag):
                    s_t=c_t
                    prev=value
                    start_flag=False
                prev_dt = dt
            
                if((c_t-s_t).total_seconds()<=10):
                    fluctuate=abs(float(value)-float(prev) )
                    if(fluctuate>=132):
                        h_count=h_count+1
                        ans.append([prev,value,s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),'High'])
                    if(66<=fluctuate and fluctuate<132):
                        l_count=l_count+1
                        ans.append([prev,value,s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),'Low'])
                if((c_t-s_t).total_seconds()>10 or s==k+1):
                    h.set(h_count)
                    l.set(l_count)
                    t.set(c_t.strftime("%H:%M:%S.%f"))
                    flagList=Listbox(root)
                    flagList.place(x=10,y=150)
                    if(h_count>=5):
                        flagList.insert(END,"5 or more high counts") 
                        all_flag_lst.append([s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),"5 or more high counts"])                  
                    elif(l_count>=7):
                        flagList.insert(END,"7 or more low counts")
                        all_flag_lst.append([s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),"7 or more low counts"])
                    elif(h_count>=3 and l_count>=2):
                        flagList.insert(END,"High counts >=3 & Low counts >= 2")
                        all_flag_lst.append([s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),"High counts >=3 & Low counts >= 2"])
                    elif(h_count>=2 and l_count>=3):
                        flagList.insert(END,"High counts >=2 & low counts >= 3")
                        f_lst.append([s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),"High counts >=2 & low counts >= 3"])
                    elif(h_count>=1 and l_count>=5):
                        flagList.insert(END,"High count >= 1 & low count >= 5")
                        all_flag_lst.append([s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),"High count >= 1 & low count >= 5"])
                    else:
                        flagList.insert(END,"no flags")
                    root.update()
                    s_t=c_t
                    h_count=0
                    l_count=0   
                prev=value
       
        search_btn = Button(root, text="Get summary", command=lambda:getSummary(ans), bg="light blue", width=25,height=3,font=('times', 14))
        search_btn.place(x=700,y=200)
        search_btn = Button(root, text="Get Flag summary", command=lambda:getSummaryFlag(all_flag_lst), bg="light green", width=25,height=3,font=('times', 14))
        search_btn.place(x=700,y=300)

    def read_xlsx(file):
        c_t=None
        s_t=None    
        prev_dt = None
        prev=None
        start_flag=True
        i=0
        ans=[]
        all_flag_lst=[]
        h_count=0
        l_count=0
        df = pd.read_excel(file.name, sheet_name = 0)
        columns = len(df.columns)
        rows = len(df)     
        k=0
        t_i=0
        v_i=1
        t_i=int(input("Enter time feild column number  :"))-1
        v_i=int(input("Enter value feild column number  :"))-1
        for row in range(rows):
            k=k+1
            time=(df.loc[row][t_i])
            value=(df.loc[row][v_i])
            null_feild=False
            dt = datetime.strptime(time, '%H:%M:%S.%f')
            c_t=dt
            if(start_flag):
                s_t=c_t
                prev=value
                start_flag=False
            prev_dt = dt
            # print(k,rows)
            if((c_t-s_t).total_seconds()<=10):
                fluctuate=abs(float(value)-float(prev) )
                if(fluctuate>=132):
                    h_count=h_count+1
                    ans.append([prev,value,s_t.strftime("%H:%M:%S.%f"),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),'High'])
                if(66<=fluctuate and fluctuate<132):
                    l_count=l_count+1
                    ans.append([prev,value,s_t.strftime('%H:%M:%S.%f'),(s_t+timedelta(seconds=10)).strftime("%H:%M:%S.%f"),'Low'])
            if((c_t-s_t).total_seconds()>10 or rows==k):
                h.set(h_count)
                l.set(l_count)
                t.set(c_t.strftime('%H:%M:%S.%f'))
                flagList=Listbox(root)
                flagList.place(x=10,y=150)                    
                if(h_count>=5):
                    flagList.insert(END,"5 or more high counts") 
                    all_flag_lst.append([s_t.strftime('%H:%M:%S.%f'),(s_t+timedelta(seconds=10)).strftime('%H:%M:%S.%f'),"5 or more high counts"])                  
                elif(l_count>=7):
                    flagList.insert(END,"7 or more low counts")
                    all_flag_lst.append([s_t.strftime('%H:%M:%S.%f'),(s_t+timedelta(seconds=10)).strftime('%H:%M:%S.%f'),"7 or more low counts"])
                elif(h_count>=3 and l_count>=2):
                    flagList.insert(END,"High counts >=3 & Low counts >= 2")
                    all_flag_lst.append([s_t.strftime('%H:%M:%S.%f'),(s_t+timedelta(seconds=10)).strftime('%H:%M:%S.%f'),"High counts >=3 & Low counts >= 2"])
                elif(h_count>=2 and l_count>=3):
                    flagList.insert(END,"High counts >=2 & low counts >= 3")
                    f_lst.append([s_t.strftime('%H:%M:%S.%f'),(s_t+timedelta(seconds=10)).strftime('%H:%M:%S.%f'),"High counts >=2 & low counts >= 3"])
                elif(h_count>=1 and l_count>=5):
                    flagList.insert(END,"High count >= 1 & low count >= 5")
                    all_flag_lst.append([s_t.strftime('%H:%M:%S.%f'),(s_t+timedelta(seconds=10)).strftime('%H:%M:%S.%f'),"High count >= 1 & low count >= 5"])
                else:
                    flagList.insert(END,"no flags")
                root.update()
                s_t=c_t
                h_count=0
                l_count=0   
            prev=value
       
        search_btn = Button(root, text="Get summary", command=lambda:getSummary(ans), bg="light blue", width=25,height=3,font=('times', 14))
        search_btn.place(x=700,y=200)
        search_btn = Button(root, text="Get Flag summary", command=lambda:getSummaryFlag(all_flag_lst), bg="light green",width=25,height=3,font=('times', 14))
        search_btn.place(x=700,y=300)


    
    def open_file(): 
        file = askopenfile(mode ='r') 
        file_type=file.name.split(".")[-1] 
        if(file_type=='csv'):
            read_csv(file)
        elif(file_type=='xlsx'):
            read_xlsx(file)
    
    def err():
        tkinter.messagebox.showerror("Error", "Please first select .csv or .xlsx file")

        
    brows_btn = Button(root, text="Select file", bg="sky blue",fg="black",font=('times', 14),command =open_file, width=25,height=3)
    brows_btn.place(x=700,y=100)
    search_btn = Button(root, text="Get summary", command=lambda:err(), bg="light blue", width=25,height=3,font=('times', 14))
    search_btn.place(x=700,y=200)
    search_btn = Button(root, text="Get Flag summary", command=lambda:err(), bg="light green", width=25,height=3,font=('times', 14))
    search_btn.place(x=700,y=300)



    root.mainloop() 

if __name__=="__main__":
    create_window()

gc.collect()


