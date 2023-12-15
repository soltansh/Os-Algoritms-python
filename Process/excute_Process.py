try:
    from Process.Process_Model import Process
except:
    from Process_Model import Process

class Excute:
    total_waiting_time = 0
    total_service_time = 0
    qtime = 0
    cn_switch = 0
    c_cpu = 0
    process_list = []

    def __init__(self, process_list: list = []) -> None:
        self.process_list = process_list

    def fifpl(self, __o: Process) -> int:
        """
        find_index_from_process_list
        """
        for i in self.process_list:
            if i == __o:
                return self.process_list.index(i)
        return -1

    def fifl(self, __o: Process, li: list) -> int:
        """
        find_index_from__list
        """
        for i in li:
            if i == __o:
                return self.process_list.index(i)
        return -1

    def sort_by_type(self, sort_type: str = "fcfs"):
        if sort_type == "fcfs":
            self.process_list.sort(key=lambda e: (
                e["ProcessArriveTime"], e["ProcessID"]))
        elif sort_type == "sjf":
            self.process_list.sort(key=lambda e: (
                e["ProcessArriveTime"], e["ProcessServiceTime"], e["ProcessID"]))
        elif sort_type == "srt":
            self.process_list.sort(key=lambda e: (
                e["ProcessArriveTime"], e["ProcessServiceTime"], e["ProcessID"]))
        elif sort_type == "rr":
            self.process_list.sort(key=lambda e: (
                e["ProcessArriveTime"], e["ProcessID"]))
        elif sort_type == "mcpu":
            self.process_list.sort(key=lambda e: (
                e["ProcessArriveTime"], e["ProcessID"]))

    @property
    def calculate_FCFS(self):
        self.sort_by_type(sort_type="fcfs")
        for process in self.process_list:
            process: Process = process  # convert the process variable to class Process
            process.ProcessRemainingTime = process.ProcessServiceTime

        time_line = self.process_list[0].ProcessArriveTime

        for item in self.process_list:
            if time_line < item.ProcessArriveTime:
                time_line += (
                    item.ProcessArriveTime - time_line) + item.ProcessServiceTime
                item.ProcessWaitingTime = 0
                item.ProcessIsComplete = True
                item.ProcessRemainingTime = 0
            else:
                item.ProcessWaitingTime = time_line - item.ProcessArriveTime
                time_line += item.ProcessServiceTime
                item.ProcessIsComplete = True
                item.ProcessRemainingTime = 0

        for item in self.process_list:
            self.total_waiting_time += float(item.ProcessWaitingTime)
            self.total_service_time += int(item.ProcessServiceTime)
            item.ProcessTurnaroundTime = item.ProcessTurnaroundTime = (float(
                item.ProcessWaitingTime) + float(item.ProcessServiceTime)) / len(self.process_list)

    @property
    def calculate_SJF(self) -> None:
        self.sort_by_type(sort_type="sjf")
        for process in self.process_list:
            process: Process = process  # convert the process variable to class Process
            process.ProcessRemainingTime = process.ProcessServiceTime

        temp_list = [item for item in self.process_list]

        temp_process_time_line = []
        current_process = Process()

        time_line = 0

        while True:
            for item in temp_list:
                if (item.ProcessArriveTime <= time_line):
                    temp_process_time_line.append(item)

            for tp in temp_process_time_line:
                if tp in temp_list:
                    temp_list.remove(tp)

            for item in temp_process_time_line:
                if not current_process.is_null():
                    if item != current_process:
                        item.ProcessWaitingTime = time_line -  item.ProcessArriveTime

            temp_process_time_line.remove(current_process) if current_process in temp_process_time_line else None
            current_process = Process()

            if len(temp_process_time_line) > 0:
                temp_process_time_line.sort(key=lambda e: e["ProcessServiceTime"])
                current_process = temp_process_time_line[0]
                current_process.ProcessIsComplete = True
                current_process.ProcessRemainingTime = 0
                # index temp_process_time_line
                itptl = self.fifpl(current_process)
                self.process_list[itptl] = current_process if itptl != -1 else self.process_list[itptl]
                
                time_line += current_process.ProcessServiceTime
                    
            else:
                time_line += 1

            if len(temp_list) == 0 and len(temp_process_time_line) == 0:
                break
            
        for item in self.process_list:
            self.total_waiting_time += float(item.ProcessWaitingTime)
            self.total_service_time += int(item.ProcessServiceTime)
            item.ProcessTurnaroundTime = (float(
                item.ProcessWaitingTime) + float(item.ProcessServiceTime)) / len(self.process_list)

    @property
    def calculate_SRT(self) -> None:
        self.sort_by_type(sort_type="srt")
        time_line = 0
        for item in self.process_list:
            time_line += item.ProcessServiceTime
            item.ProcessRemainingTime = item.ProcessServiceTime
            item.ProcessEnterTimeFromQueue.append(item.ProcessArriveTime)
        temp_process_time_line = []
        check_remain_runtime = False
        current_process = Process()

        for i in range(0, time_line):
            before_count_temp_list = len(temp_process_time_line)

            # Add Item To Temp List
            for item in self.process_list:
                # Now I Access To All init Variable In Process Class ....
                item: Process = item
                if item.ProcessArriveTime == i:
                    temp_process_time_line.append(item)
                    check_remain_runtime = True

            if len(temp_process_time_line) == before_count_temp_list:
                check_remain_runtime = False

            if self.fifl(current_process, temp_process_time_line) == -1:
                check_remain_runtime = True

            # Start Calculate
            if check_remain_runtime:
                if len(temp_process_time_line) != 0:
                    # Condition Layer
                    min_rimain_time = temp_process_time_line[0].ProcessRemainingTime
                    process_after_change: Process = temp_process_time_line[0]
                    # Find Process Index On self.process_list

                    for j in temp_process_time_line:
                        temp_pro: Process = j
                        if temp_pro.ProcessRemainingTime < min_rimain_time:
                            min_rimain_time = temp_pro.ProcessRemainingTime
                            process_after_change = temp_pro

                    current_process = process_after_change

                    current_process.ProcessRemainingTime -= 1
                    current_process_index = self.fifpl(current_process)
                    self.process_list[current_process_index] = current_process if current_process_index != - \
                        1 else self.process_list[current_process_index]

                    if current_process.ProcessRemainingTime == 0:
                        current_process.ProcessIsComplete = True
                        temp_process_time_line.remove(
                            current_process) if current_process in temp_process_time_line else None
                        self.process_list[current_process_index].ProcessExitTimeFromQueue.append(
                            i+1) if current_process_index != -1 else None

            else:
                if not current_process.is_null():
                    current_process.ProcessRemainingTime -= 1
                    current_process_index = self.fifpl(current_process)
                    self.process_list[current_process_index] = current_process if current_process_index != - \
                        1 else self.process_list[current_process_index]

                    if current_process.ProcessRemainingTime == 0:
                        current_process.ProcessIsComplete = True
                        current_process_index = self.fifpl(current_process)
                        temp_process_time_line.remove(
                            current_process) if current_process in temp_process_time_line else None
                        self.process_list[current_process_index].ProcessExitTimeFromQueue.append(
                            i+1) if current_process_index != -1 else None


        for i in self.process_list:
            i.ProcessEnterTimeFromQueue = list(
                set(i.ProcessEnterTimeFromQueue))
            i.ProcessEnterTimeFromQueue.sort()
            i.ProcessExitTimeFromQueue = list(set(i.ProcessExitTimeFromQueue))
            i.ProcessExitTimeFromQueue.sort()

        for process in self.process_list:
            wait = process.ProcessExitTimeFromQueue[0] - process.ProcessServiceTime - process.ProcessEnterTimeFromQueue[0]
            process.ProcessWaitingTime = wait
            

        for item in self.process_list:
            self.total_waiting_time += float(item.ProcessWaitingTime)
            self.total_service_time += int(item.ProcessServiceTime)
            item.ProcessTurnaroundTime = item.ProcessTurnaroundTime = (float(
                item.ProcessWaitingTime) + float(item.ProcessServiceTime)) / len(self.process_list)

    @property
    def calculate_RR(self) -> None:
        self.sort_by_type(sort_type="rr")

        temp_list = [item for item in self.process_list]

        for item in temp_list:
            item.ProcessRemainingTime = item.ProcessServiceTime
            item.ProcessEnterTimeFromQueue.append(item.ProcessArriveTime)

            i_item = self.fifpl(item)
            self.process_list[i_item] = item if i_item != - \
                1 else self.process_list[i_item]

        temp_process_time_line_list = []
        curennt_process = Process()
        temp_process = Process()

        time_line = 0

        is_complate = False

        while not is_complate:  # Start while
            list_is_reverse = False
            is_add_more_than_one_item = False
            count_add_item = 0

            if len(temp_process_time_line_list) != 0:
                temp_process_time_line_list = temp_process_time_line_list[::-1]
                list_is_reverse = True

            for item in temp_list:
                if item.ProcessArriveTime <= time_line:
                    temp_process_time_line_list.append(item)
                    count_add_item += 1

            if list_is_reverse:
                temp_process_time_line_list = temp_process_time_line_list[::-1]

            if count_add_item > 1:
                is_add_more_than_one_item = True
                count_add_item = 0

            if is_add_more_than_one_item:
                for i in range(1, len(temp_process_time_line_list)):
                    temp_process_time_line_list[i].ProcessExitTimeFromQueue.append(
                        time_line)
                    temp_process_time_line_list[i].ProcessGetQTime = 0
                    # temp_process_time_line_list_index
                    tptlli = self.fifpl(temp_process_time_line_list[i])
                    self.process_list[tptlli] = temp_process_time_line_list[i] if tptlli != - \
                        1 else self.process_list[tptlli]

            for i in temp_process_time_line_list:
                temp_list.remove(i) if i in temp_list else None

            if not curennt_process.is_null() and len(temp_process_time_line_list) != 0:
                if temp_process_time_line_list[0] != curennt_process:
                    # add (context_switch) second to all the process
                    for i in range(len(temp_process_time_line_list)):
                        temp_process_time_line_list[i].ProcessWaitingTime += self.cn_switch
                        # temp_process_time_line_list_index
                        tp = self.fifpl(temp_process_time_line_list[i])
                        self.process_list[tp] = temp_process_time_line_list[i] if tp != - \
                            1 else self.process_list[tp]

                    temp_process_time_line_list[0].ProcessEnterTimeFromQueue.append(
                        time_line)
                    curennt_process.ProcessExitTimeFromQueue.append(time_line)
                    curennt_process.ProcessGetQTime = 0
                    temp_process_time_line_list[0].ProcessGetQTime = 0
                    time_line += self.cn_switch

                    tptl = self.fifpl(curennt_process)
                    self.process_list[tptl] = curennt_process if tptl != - \
                        1 else self.process_list[tptl]

                    # temp_process_time_line_list_index
                    tpt = self.fifpl(temp_process_time_line_list[0])
                    self.process_list[tpt] = temp_process_time_line_list[0] if tpt != - \
                        1 else self.process_list[tpt]

            # 1 second later
            time_line += 1

            if len(temp_process_time_line_list) != 0:
                curennt_process = temp_process_time_line_list[0]

                temp_process_time_line_list[0].ProcessRemainingTime -= 1
                temp_process_time_line_list[0].ProcessGetQTime += 1
                # temp_process_time_line_list_index
                tpt = self.fifpl(curennt_process)
                self.process_list[tpt] = curennt_process if tpt != - \
                    1 else self.process_list[tpt]

                # Process Remaining Time is 0
                if temp_process_time_line_list[0].ProcessRemainingTime == 0:
                    temp_process_time_line_list[0].ProcessIsComplete = True
                    temp_process_time_line_list[0].ProcessGetQTime = 0
                    self.process_list[tpt] = curennt_process if tpt != - \
                        1 else self.process_list[tpt]
                    temp_process_time_line_list.remove(
                        temp_process_time_line_list[0])

                    if len(temp_process_time_line_list) == 0 and len(temp_list) == 0:

                        curennt_process.ProcessExitTimeFromQueue.append(
                            time_line)
                        # temp_process_time_line_list_index
                        tptl = self.fifpl(curennt_process)
                        self.process_list[tptl] = curennt_process if tptl != - \
                            1 else self.process_list[tptl]
                        is_complate = True
                        break

                else:  # Process Remaining Time is not 0 yet
                    # Process shift To End of The List
                    if temp_process_time_line_list[0].ProcessGetQTime % self.qtime == 0:
                        temp_process = temp_process_time_line_list[0]
                        temp_process.ProcessGetQTime = 0

                        # temp_process_time_line_list_index
                        t = self.fifpl(temp_process)
                        self.process_list[t] = temp_process_time_line_list[0] if t != - \
                            1 else self.process_list[t]

                        temp_process_time_line_list.pop(0)
                        temp_process_time_line_list.append(temp_process)
                        temp_process = Process()

        for i in self.process_list:
            i.ProcessEnterTimeFromQueue = list(
                set(i.ProcessEnterTimeFromQueue))
            i.ProcessEnterTimeFromQueue.sort()
            i.ProcessExitTimeFromQueue = list(set(i.ProcessExitTimeFromQueue))
            i.ProcessExitTimeFromQueue.sort()

        for process in self.process_list:
            wait = 0
            if len(process.ProcessExitTimeFromQueue) == 1:
                wait += process.ProcessEnterTimeFromQueue[-1]
            else:
                for i in range(len(process.ProcessEnterTimeFromQueue)):
                    try:
                        wait += process.ProcessEnterTimeFromQueue[i +
                                                                  1] - process.ProcessExitTimeFromQueue[i]
                    except:
                        pass

            process.ProcessWaitingTime += wait

        for item in self.process_list:
            self.total_waiting_time += float(item.ProcessWaitingTime)
            self.total_service_time += int(item.ProcessServiceTime)
            item.ProcessTurnaroundTime = item.ProcessTurnaroundTime = (float(
                item.ProcessWaitingTime) + float(item.ProcessServiceTime)) / len(self.process_list)

    @property
    def calculate_MCPU(self) -> None:
        self.sort_by_type(sort_type="mcpu")

        for process in self.process_list:
            process: Process = process  # convert the process variable to class Process
            process.ProcessRemainingTime = process.ProcessServiceTime

        temp_list = [item for item in self.process_list]

        cpus_list = []
        for num in range(self.c_cpu):
            cpus_list.append([])
        timeline = 0

        is_all_cpu_empty = False

        while True:
            temp_current_process = Process()
            for i in range(self.c_cpu):
                for item in temp_list:
                    if item.ProcessArriveTime <= timeline:
                        if len(cpus_list[i]) == 0:
                            cpus_list[i].append(item)
                            temp_current_process = item
                            break
                try:
                    if not temp_current_process.is_null():
                        temp_list.remove(temp_current_process)
                        temp_current_process = Process()
                except:
                    pass

            for item in temp_list:
                if item.ProcessArriveTime <= timeline:
                    item.ProcessWaitingTime += 1

            for i in range(self.c_cpu):
                try:
                    if cpus_list[i][0].ProcessIsComplete != True:
                        cpus_list[i][0].ProcessRemainingTime -= 1
                        if cpus_list[i][0].ProcessRemainingTime == 0:
                            cpus_list[i][0].ProcessIsComplete = True
                            # item_in_orginal_list
                            iiol = self.fifpl(cpus_list[i][0])
                            self.process_list[iiol] = cpus_list[i][0] if iiol != - \
                                1 else self.process_list[iiol]
                            cpus_list[i].pop(0)
                except:
                    pass

            timeline += 1

            for i in range(self.c_cpu):
                if len(cpus_list[i]) == 0:
                    is_all_cpu_empty = True
                else:
                    is_all_cpu_empty = False

            if len(temp_list) == 0 and is_all_cpu_empty:
                break

        for item in self.process_list:
            self.total_waiting_time += float(item.ProcessWaitingTime)
            self.total_service_time += int(item.ProcessServiceTime)
            item.ProcessTurnaroundTime = item.ProcessTurnaroundTime = (float(
                item.ProcessWaitingTime) + float(item.ProcessServiceTime)) / len(self.process_list)

    @property
    def reset(self) -> None:
        for item in self.process_list:
            item.ProcessRemainingTime = 0
            item.ProcessGetQTime = 0
            item.ProcessWaitingTime = 0
            item.ProcessTurnaroundTime = 0
            item.ProcessIsComplete = False
            item.ProcessEnterTimeFromQueue = []
            item.ProcessExitTimeFromQueue = []

    @property
    def process_to_table_list(self):
        self.process_list.sort(key=lambda e: e["ProcessID"])
        return [[i.ProcessID, i.ProcessArriveTime, i.ProcessServiceTime, i.ProcessWaitingTime, i.ProcessTurnaroundTime] for i in self.process_list]

    def show_process(self) -> None:
        self.process_list.sort(key=lambda e: e["ProcessID"])
        print(f"P.ID\t   Arrive.Time\t  Service.Time\t    Wait.Time\t      T.Time")
        print("\a------------------------------------------------------------------------------")
        for item in self.process_list:
            item: Process = item
            print(
                f"{item.ProcessID}\t\t{item.ProcessArriveTime}\t\t{item.ProcessServiceTime}\t\t{item.ProcessWaitingTime}\t\t{item.ProcessTurnaroundTime}\n"
            )
            print(
                "------------------------------------------------------------------------------")
        print(
            f"\t\t\t{self.total_waiting_time}\t\t\t\t{self.total_service_time+self.total_waiting_time}")
        print(f"total_waiting_time : -------\ttotal_service_time : -------")
        print(
            f"\t\t\t{len(self.process_list)}\t\t\t\t{len(self.process_list)}\n")
        self.total_waiting_time = 0
        self.total_service_time = 0
        self.reset()
