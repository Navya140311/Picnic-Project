from tkinter import *
import random 

root= Tk()
root.title('Picnic Bag')
root.geometry('400x400')
root.configure(background='yellow')   

item_label= Label(root)
random_no_label= Label(root)

picnic_list=["Bottle","Tiffin","ID Card","Chocolates","Chips","Tickets","Hanky"]
item_label["text"]= "Listed Items : " + str(picnic_list) + " "

def random_func() :
    random_no = random.randint(0, 6)
    random_no_label["text"]="Put Item no " + str(random_no) + " in bag"
    
button= Button(root, text= "Which item shall I put in the bag?", command=random_func)
button.place(relx=0.5, rely=0.4 ,anchor=CENTER)

item_label.place(relx=0.5, rely=0.5, anchor= CENTER)
random_no_label.place(relx=0.5, rely=0.6, anchor= CENTER)

root.mainloop()