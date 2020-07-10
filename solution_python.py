class EventSourcer():
    # Do not change the signature of any functions
    
    def __init__(self):
        self.value = 0
        # to maintain the history of undo
        self.history_undo=[]
        # to maintain the histoy of redo
        self.history_redo=[]

    def add(self, num: int):
        self.value+=num
        self.history_undo.append((num,'+'))

    def subtract(self, num: int):
        self.value-=num
        self.history_undo.append((num,'-'))

    def undo(self):
        if len(self.history_undo) == 0:
            return
        num, sign = self.history_undo[-1]
        del self.history_undo[-1]
        if sign == '+':
            self.value -=num
        else:
            self.value +=num
        self.history_redo.append((num, sign))


    def redo(self):
        # to check out of bound
        if len(self.history_redo) == 0:
            return
        num, sign = self.history_redo[-1]
        del self.history_redo[-1]
        if sign == '+':
            self.value +=num
        else:
            self.value -=num
        
        self.history_undo.append((num, sign))

    def bulk_undo(self, steps: int):
        # to check out of bound condisttion
        if steps > len(self.history_undo):
            steps = len(self.history_undo)
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        if steps > len(self.history_redo):
            steps = len(self.history_redo)
        for i in range(steps):
            self.redo()