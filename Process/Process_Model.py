class Process:
    def __init__(
        self, ProcessID: int = "", ProcessArriveTime: int = 0, ProcessServiceTime: int = 0
    ) -> None:
        """
        initial new Process
        """
        self.ProcessID = ProcessID
        self.ProcessArriveTime = ProcessArriveTime
        self.ProcessServiceTime = ProcessServiceTime
        self.ProcessRemainingTime = 0
        self.ProcessGetQTime = 0
        self.ProcessWaitingTime = 0
        self.ProcessTurnaroundTime = 0
        self.ProcessIsComplete = False
        self.ProcessEnterTimeFromQueue = []
        self.ProcessExitTimeFromQueue = []

    def __getitem__(self, i):
        return getattr(self, i)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Process):
            if (
                self.ProcessID == __o.ProcessID
            ):
                return True
        return False

    def __ne__(self, __o: object) -> bool:
        if isinstance(__o, Process):
            if (
                self.ProcessID != __o.ProcessID
            ):
                return True
        return False

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Process):
            if self.ProcessArriveTime < __o.ProcessArriveTime:
                return True
            if self.ProcessServiceTime < __o.ProcessServiceTime:
                return True
            if self.ProcessID < __o.ProcessID:
                return True
        return False

    def __gt__(self, __o: object) -> bool:
        if isinstance(__o, Process):
            if self.ProcessArriveTime > __o.ProcessArriveTime:
                return True
            if self.ProcessServiceTime > __o.ProcessServiceTime:
                return True
            if self.ProcessID > __o.ProcessID:
                return True
        return False

    def __le__(self, __o: object) -> bool:
        if isinstance(__o, Process):
            if self.ProcessArriveTime <= __o.ProcessArriveTime:
                return True
            if self.ProcessServiceTime <= __o.ProcessServiceTime:
                return True
            if self.ProcessID <= __o.ProcessID:
                return True
        return False

    def __ge__(self, __o: object) -> bool:
        if isinstance(__o, Process):
            if self.ProcessArriveTime >= __o.ProcessArriveTime:
                return True
            if self.ProcessServiceTime >= __o.ProcessServiceTime:
                return True
            if self.ProcessID >= __o.ProcessID:
                return True
        return False

    def is_null(self) -> bool:
        """
        IF :: self.ProcessID == None => True :: False FI
        """
        if self.ProcessID == None:
            return True
        return False
