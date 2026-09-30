from tkinter import *
import psutil

window = Tk()

image2 = PhotoImage(file='icons8-c-драйв-2-48.gif')
image3 = PhotoImage(file='icons8-жесткий-диск-48.gif')
image4 = PhotoImage(file='icons8-слот-памяти-48.gif')

Label(window, image=image2).place(x=20, y=20)
Label(window, image=image3).place(x=20, y=60)
Label(window, image=image4).place(x=20, y=100)

def refresh_data():
    label = Label(window, text=f'CPU load: {psutil.cpu_percent()} %').place(x=80, y=20)    
    labe2 = Label(window, text=f'Memory load: {psutil.virtual_memory().percent} %').place(x=80, y=60)
    labe3 = Label(window, text=f'Disk usage: {psutil.disk_usage("/").used // 1000000000} GB').place(x=80, y=100)   
    # Повторяем вызов этой же функции через 1000 миллисекунд (1 секунду)
    window.after(1000, refresh_data)
    

refresh_data()
    
mainloop()
