from tkinter import *
from excute_Process import Excute
from Process_Model import Process

app = Tk()
app.title("OS")
width = int(app.winfo_screenwidth())
height = int(app.winfo_screenheight())
right_left = str(int(((width + width // 2) / 2)))
top_down = str(int(((height - 200) / 2) - 50))
app.resizable(width=FALSE, height=FALSE)
app.geometry(f"+{right_left}+{top_down}")
app.attributes('-topmost', True)
app.update()



process_list = []
process_list.append(Process(1, 1, 3))
process_list.append(Process(4, 0, 3))
process_list.append(Process(3, 2, 3))
process_list.append(Process(2, 2, 3))

X = Excute(process_list)

# X.show_process()
# X.calculate_FCFS
# X.show_process()

# X.calculate_SJF
# X.show_process()

# X.show_process()
# X.calculate_SRT
# X.show_process()

# X.c_cpu = 4
# X.calculate_MCPU
# X.show_process()

# X.qtime = 2
# X.cn_switch = 0
# X.calculate_RR
# X.show_process()
