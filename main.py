import customtkinter
from tkinter import messagebox
from plyer import notification
import time

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Notifier")
root.geometry("500x300")
root.resizable(False, False)


def get_details():
    try:
        title = entry_1.get()
        msg = entry_2.get()
        time_1 = entry_3.get()

        if title == "" or msg == "" or time_1 == "":
            messagebox.showerror('Notifier',"All fields required")
        else:
            int_time = int(float(time_1))
            time_to_sec = int_time * 3600

            time.sleep(time_to_sec)
            root.destroy()

            notification.notify(title=title,
                                message=msg,
                                app_name="Notifier",
                                app_icon="C:/Users/Hp/Downloads/notification_bell_icon_178938.ico",
                                timeout=10)
    except ValueError:
        messagebox.showerror('Notifier','Fill Numbers Only')

#FRAME1
frame_1  = customtkinter.CTkFrame(master=root,height=300,width=200)
frame_1.pack(fill='both',expand=True)

#LABEL
label = customtkinter.CTkLabel(master=frame_1,text="Notifier",font=("helvetica",40))
label.pack(padx=10,pady=15)

# LABEL1
label_1 = customtkinter.CTkLabel(master=frame_1,text="Title")
label_1.place(x=12, y=70)

# ENTRY1
entry_1 = customtkinter.CTkEntry(master=frame_1,width=300,placeholder_text="Title")
entry_1.place(x=123, y=78)

# LABEL2
label_2 = customtkinter.CTkLabel(master=frame_1,text="Display Message")
label_2.place(x=12, y=120)

# ENTRY2
entry_2 = customtkinter.CTkEntry(master=frame_1,width=300,placeholder_text="Display Message")
entry_2.place(x=123, y=120)

# LABEL3
label_3 = customtkinter.CTkLabel(master=frame_1,text="Time")
label_3.place(x=12, y=165)

# ENTRY3
entry_3 = customtkinter.CTkEntry(master=frame_1,width=300,placeholder_text="Time")
entry_3.place(x=123, y=165)

# BUTTON1
button_1 = customtkinter.CTkButton(master=frame_1,text="Set Notification", command=get_details,
                                   width=20)
button_1.place(x=200, y=230)

#LABEL4
label_4 = customtkinter.CTkLabel(master=frame_1,text="Hours")
label_4.place(x=430,y=170)






root.mainloop()

