from tkinter import *
from tkinter.ttk import *
try:
    from Process.excute_Process import Excute
    from Process.Process_Model import Process
except:
    from excute_Process import Excute
    from Process_Model import Process

# Define Process List Shown On Grid View
process_list = []


app = Tk()
app.title("OS")
width = int(app.winfo_screenwidth())
height = int(app.winfo_screenheight())
right_left = str((int(width) - 800) // 2)
top_down = str((int(height) - 600) // 2)
app.resizable(width=True, height=True)
app.geometry(f"+{right_left}+{top_down}")
app.attributes('-topmost', True)
app.maxsize(800,  600)
app.minsize(700,  350)
app.update()


# Pack
layer_0 = Frame(app)
layer_0.pack(side='top', fill='both', padx=5, pady=5, expand=True)

layer_0_1 = Frame(layer_0)
layer_0_1.pack(side='left', fill='both', padx=5, pady=5, expand=True)
layer_0_2 = Frame(layer_0)
layer_0_2.pack(side='left', fill='both', padx=5, pady=5, expand=True)
layer_0_3 = Frame(layer_0)
layer_0_3.pack(side='left', fill='both', padx=5, pady=5, expand=True)

layer_1 = Frame(app)
layer_1.pack(side='top', fill='both', padx=5, pady=5, expand=True)

layer_2 = Frame(app)
layer_2.pack(side='top', fill='both', padx=5, pady=5, expand=True)

layer_2_left = Frame(layer_2)
layer_2_left.pack(side='left', fill='both', padx=5, pady=5, expand=True)

layer_2_right = Frame(layer_2)
layer_2_right.pack(side='right', fill='both', padx=5, pady=5, expand=True)
layer_2_right_0 = Frame(layer_2_right)
layer_2_right_0.pack(side='right', fill='both', padx=5, pady=5, expand=True)
layer_2_right_1 = Frame(layer_2_right)
layer_2_right_1.pack(side='right', fill='both', padx=5, pady=5, expand=True)

layer_3 = Frame(app)
layer_3.pack(side='top', fill='both', padx=5, pady=5, expand=True)

layer_3_left = Frame(layer_3)
layer_3_left.pack(side='left', fill='both', padx=5, pady=5, expand=True)

layer_3_right = Frame(layer_3)
layer_3_right.pack(side='right', fill='both', padx=5, pady=5, expand=True)

layer_3_left_0 = Frame(layer_3_left)
layer_3_left_0.pack(side='top', fill='both', padx=5, pady=5, expand=True)

layer_3_left_1 = Frame(layer_3_left)
layer_3_left_1.pack(side='top', fill='both', padx=5, pady=5, expand=True)

layer_3_left_1_right = Frame(layer_3_left_1)
layer_3_left_1_right.pack(side='left', fill='both', padx=5, pady=5, expand=True)

layer_3_left_1_left = Frame(layer_3_left_1)
layer_3_left_1_left.pack(side='right', fill='both', padx=5, pady=5, expand=True)

layer_3_left_2 = Frame(layer_3_left)
layer_3_left_2.pack(side='top', fill='both', padx=5, pady=5, expand=True)

layer_3_left_2_right = Frame(layer_3_left_2)
layer_3_left_2_right.pack(side='left', fill='both', padx=5, pady=5, expand=True)

layer_3_left_2_left = Frame(layer_3_left_2)
layer_3_left_2_left.pack(side='right', fill='both', padx=5, pady=5, expand=True)

def callback(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False


reg = app.register(callback)


# Scrolles
scroll_0 = Scrollbar(layer_3_right)
# scroll_1 = Scrollbar(layer_3_right,orient='horizontal')


# Tables
process_table = Treeview(layer_3_right, yscrollcommand=scroll_0.set)
# process_table = Treeview(layer_3_right, yscrollcommand=scroll_0.set, xscrollcommand =scroll_1.set)
scroll_0.config(command=process_table.yview)
# scroll_1.config(command=process_table.xview)

process_table['columns'] = ('ProcessID', 'ProcessArriveTime',
                            'ProcessServiceTime', 'ProcessWaitingTime', 'ProcessTurnaroundTime')
process_table.column("#0", width=0,  stretch=NO)
process_table.column("ProcessID", anchor=CENTER, width=80)
process_table.column("ProcessArriveTime", anchor=CENTER, width=80)
process_table.column("ProcessServiceTime", anchor=CENTER, width=80)
process_table.column("ProcessWaitingTime", anchor=CENTER, width=80)
process_table.column("ProcessTurnaroundTime", anchor=CENTER, width=80)

process_table.heading("#0", text="", anchor=CENTER)
process_table.heading("ProcessID", text="پردازه", anchor=CENTER)
process_table.heading("ProcessArriveTime", text="زمان رسیدن", anchor=CENTER)
process_table.heading("ProcessServiceTime", text="زمان سرویس", anchor=CENTER)
process_table.heading("ProcessWaitingTime", text="زمان انتظار", anchor=CENTER)
process_table.heading("ProcessTurnaroundTime", text="گردش کار", anchor=CENTER)


# Labels
lbl_qtime = Label(layer_0_1, text='Quantum Time : ')
lbl_cn_switch = Label(layer_0_2, text='Context Switch : ')
lbl_count_cpu = Label(layer_0_3, text='Cpu Count : ')
lbl_ser_time = Label(layer_2_right_0, text='Service Time : ')
lbl_ar_time = Label(layer_2_right_1, text='Arrive Time : ')

##########################################################################
##########################################################################
lbl_TT = Label(layer_3_left_1_right, text="زمان گردش کار : ")          ##
lbl_total_ser_time = Label(layer_3_left_1_left, text="0")               ##
line_0 = Label(layer_3_left_1_left, text="--------")                    ##
lbl_total_ser_time_m = Label(layer_3_left_1_left, text="0")             ##
##########################################################################
lbl_TW = Label(layer_3_left_2_right, text="زمان انتظار : ")            ##
lbl_total_wait_time = Label(layer_3_left_2_left, text="0")              ##
line_1 = Label(layer_3_left_2_left, text="--------")                    ##
lbl_total_wait_time_m = Label(layer_3_left_2_left, text="0")            ##
##########################################################################
##########################################################################

# Variables
text_qtime = StringVar(app)
text_cn_switch = StringVar(app)
text_count_cpu = StringVar(app)
text_ser_time = StringVar(app)
text_ar_time = StringVar(app)

text_qtime.set(1)
text_cn_switch.set(0)
text_count_cpu.set(1)
text_ser_time.set(1)
text_ar_time.set(0)


# Entries
# state : normal, disabled, readonly
txt_qtime = Entry(layer_0_1, state="normal",
                  textvariable=text_qtime, )
txt_qtime.config(validate="key", validatecommand=(reg, '%P'))

txt_cn_switch = Entry(layer_0_2, state="normal",
                      textvariable=text_cn_switch, )
txt_cn_switch.config(validate="key", validatecommand=(reg, '%P'))

txt_count_cpu = Entry(layer_0_3, state="normal",
                      textvariable=text_count_cpu, )
txt_count_cpu.config(validate="key", validatecommand=(reg, '%P'))

txt_ser_time = Entry(layer_2_right_0,
                     state="normal", textvariable=text_ser_time)
txt_ser_time.config(validate="key", validatecommand=(reg, '%P'))

txt_ar_time = Entry(layer_2_right_1,
                    state="normal", textvariable=text_ar_time)
txt_ar_time.config(validate="key", validatecommand=(reg, '%P'))


def process_table_reset():
    global process_list
    # Get all item to Delete
    for row in process_table.get_children():
        process_table.delete(row)
    process_list = []
    text_qtime.set(1)
    text_cn_switch.set(0)
    text_count_cpu.set(1)
    text_ser_time.set(1)
    text_ar_time.set(0)
    lbl_total_ser_time.config(text="0")
    lbl_total_ser_time_m.config(text="0")
    lbl_total_wait_time.config(text="0")
    lbl_total_wait_time_m.config(text="0")


def process_table_add(pro_list:list=[]):
    for i in pro_list:
        process_table.insert(
            parent='', index='end', iid=i[0], text='',
            values=(f"P{i[0]}", i[1], i[2], i[3], i[4])
        )
    lbl_total_ser_time_m.config(text=str(len(pro_list)))
    lbl_total_wait_time_m.config(text=str(len(pro_list)))


def add_process_to_list():
    Ind = len(process_list)
    S_Time = txt_ser_time.get()
    A_Time = txt_ar_time.get()
    if S_Time != "0":
        process_list.append(Process(int(Ind), int(A_Time), int(S_Time)))
        process_table.insert(
            parent='', index='end', iid=Ind, text='',
            values=(f'P{Ind}', A_Time, S_Time, 0, 0)
        )

def Calculate_Process_List(process_list, calc_type="fcfs", q_time=0, cn_switch=0, c_cpu=0) -> Excute:
    # Add Your Process Here And Use calculate_FCFS, calculate_SJF, calculate_SRT, calculate_MCPU, calculate_RR
    Calculate = Excute(process_list)
    Calculate.qtime = q_time
    Calculate.cn_switch = cn_switch
    Calculate.c_cpu = c_cpu

    if calc_type == "fcfs":
        Calculate.calculate_FCFS
    elif calc_type == "sjf":
        Calculate.calculate_SJF
    elif calc_type == "srt":
        Calculate.calculate_SRT
    elif calc_type == "rr":
        Calculate.calculate_RR
    elif calc_type == "mcpu":
        Calculate.calculate_MCPU

    lbl_total_ser_time.config(text=str(Calculate.total_service_time))
    lbl_total_wait_time.config(text=str(Calculate.total_waiting_time))

    return Calculate


def FCFS():
    if len(process_list) != 0:
        Calculate = Calculate_Process_List(process_list, calc_type="fcfs")
        lst = Calculate.process_to_table_list
        for row in process_table.get_children():
            process_table.delete(row)
        process_table_add(lst)
        Calculate.reset


def SJF():
    if len(process_list) != 0:
        Calculate = Calculate_Process_List(process_list, calc_type="sjf")
        lst = Calculate.process_to_table_list
        for row in process_table.get_children():
            process_table.delete(row)
        process_table_add(lst)
        Calculate.reset


def SRT():
    if len(process_list) != 0:
        Calculate = Calculate_Process_List(process_list, calc_type="srt")
        lst = Calculate.process_to_table_list
        for row in process_table.get_children():
            process_table.delete(row)
        process_table_add(lst)
        Calculate.reset


def RR():
    if len(process_list) != 0:
        cn_switch = int(txt_cn_switch.get())
        q_time = int(txt_qtime.get())
        if q_time != 0:
            Calculate = Calculate_Process_List(process_list, calc_type="rr", q_time=q_time, cn_switch=cn_switch)
            lst = Calculate.process_to_table_list
            for row in process_table.get_children():
                process_table.delete(row)
            process_table_add(lst)
            Calculate.reset


def MCPU():
    if len(process_list) != 0:
        c_cpu = int(txt_count_cpu.get())
        if c_cpu != 0:
            Calculate = Calculate_Process_List(process_list, calc_type="mcpu", c_cpu=c_cpu)
            lst = Calculate.process_to_table_list
            for row in process_table.get_children():
                process_table.delete(row)
            process_table_add(lst)
            Calculate.reset

# Buttons
btn_FCFS = Button(layer_1, text="FCFS", command=FCFS)
btn_SJF = Button(layer_1, text="SJF", command=SJF)
btn_SRT = Button(layer_1, text="SRT", command=SRT)
btn_RR = Button(layer_1, text="RR", command=RR)
btn_MCPU = Button(layer_1, text="MCPU", command=MCPU)

btn_Add_Process = Button(
    layer_2_left, text="Add_Process", command=add_process_to_list)
btn_reset_Process_From_datagridview = Button(
    layer_3_left_0, text="Reset All Process", command=process_table_reset)

# Pack
btn_FCFS.pack(side='left', fill='both', padx=1, expand=True)
btn_SJF.pack(side='left', fill='both', padx=1, expand=True)
btn_SRT.pack(side='left', fill='both', padx=1, expand=True)
btn_RR.pack(side='left', fill='both', padx=1, expand=True)
btn_MCPU.pack(side='left', fill='both', padx=1, expand=True)

btn_Add_Process.pack(side='left', fill='both',)
btn_reset_Process_From_datagridview.pack(side='top', fill=X,)

lbl_qtime.pack(side='left', fill='both', padx=1, pady=3, expand=True)
txt_qtime.pack(side='left', fill='both', padx=1, pady=3, expand=True)
lbl_cn_switch.pack(side='left', fill='both', padx=1, pady=3, expand=True)
txt_cn_switch.pack(side='left', fill='both', padx=1, pady=3, expand=True)
lbl_count_cpu.pack(side='left', fill='both', padx=1, pady=3, expand=True)
txt_count_cpu.pack(side='left', fill='both', padx=1, pady=3, expand=True)

lbl_ser_time.pack(side='left', fill='both', padx=1, pady=3, expand=True)
lbl_ar_time.pack(side='left', fill='both', padx=1, pady=3, expand=True)
txt_ser_time.pack(side='left', fill='both', padx=1, pady=3, expand=True)
txt_ar_time.pack(side='left', fill='both', padx=1, pady=3, expand=True)


lbl_total_ser_time.pack(side='top', fill='both', padx=15, pady=1, expand=True)
line_0.pack(side='top', fill='both', padx=5, pady=1, expand=True)
lbl_total_ser_time_m.pack(side='top', fill='both', padx=15, pady=1, expand=True)

lbl_TT.pack(side='top', fill='both', pady=1, expand=True)

lbl_total_wait_time.pack(side='top', fill='both', padx=15, pady=1, expand=True)
line_1.pack(side='top', fill='both', padx=5, pady=1, expand=True)
lbl_total_wait_time_m.pack(side='top', fill='both', padx=15, pady=1, expand=True)

lbl_TW.pack(side='top', fill='both', pady=1, expand=True)

scroll_0.pack(side=RIGHT, fill=Y, padx=0)
# scroll_1.pack(side= BOTTOM,fill=X)
process_table.pack()


app.mainloop()
