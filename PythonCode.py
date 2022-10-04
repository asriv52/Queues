SIZE = 4
NumElements = 0
HeadPointer = 0
TailPointer = -1
Queue = ["" for i in range(SIZE)]


# ADD
def Enqueue(NewData : str):
    global HeadPointer, TailPointer, NumElements
    if NumElements >= SIZE:
        print(f"Unable to add {NewData} because the queue is full")
    else:
        TailPointer = TailPointer + 1
        if TailPointer > SIZE-1:
            TailPointer = 0
        Queue[TailPointer] = NewData
        NumElements = NumElements + 1
        print(f"Added {NewData} to the end of the queue")
        


# DELETE
def Dequeue():
    global HeadPointer, TailPointer, NumElements
    if NumElements <= 0:
        print("Cannot dequeue because the queue is empty")
    else:
        Removed = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1
        NumElements = NumElements - 1
        if HeadPointer > SIZE-1:
            HeadPointer = 0
        print(f"Removed {Removed} from the queue")
