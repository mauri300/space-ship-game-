
from tkinter import *
import threading
import time

from sympy import fps


class Window():
    def __init__(self):
        self.__WIDTH = 800
        self.__HEIGHT = 600
        self.__running = 0
        self.__x = 100
        self.__y = 200

        self.__FPS = 60
        self.__TARGETTIME = 1000000000/self.__FPS
        self.__delta = 0
        self.__AVERAGEFPS = self.__FPS

        self.__window = Tk()
        self.__window.title("Space Ship Game")
        self.__window.resizable(0, 0) # No se puede redimensionar ni en alto ni en ancho
        # self.__window.geometry(str(self.__WIDTH) + 'x' + str(self.__HEIGHT))
        # self.__window.config(bg="blue") # El color de fondo
        # self.__start()
        self.__myFrame = Frame(self.__window, width=self.__WIDTH, height=self.__HEIGHT)
        self.__myFrame.pack()
        self.__myLabel = Label(self.__myFrame, text="Hello")
        self.__myLabel.place(x=self.__x, y=self.__y)
        self.__start()
        self.__window.mainloop() # La ventana esta a la escucha, siempre debe estar al final

    def __run(self):
        now = 0 # Variable para medir el instante actual
        frames = 0
        duration = 0
        time.sleep(1)
        lastTime = time.time_ns() # Variable que almacena el instante anterior
        while(self.__running):
 
            now = time.time_ns()
            self.__delta += (now - lastTime)/self.__TARGETTIME # ns*60/1000000000
            # print("Delta es: ",float(self.__delta))
            duration += (now - lastTime) # ns
            # print("La duracion es: ", duration)
            lastTime = now
            
            if(float(self.__delta) >= 1):
                self.__update()
                self.__draw()
                self.__delta -= 1
                frames += 1
                # print("Los frames son: ", frames)
            
            if(duration >= 1000000000):
                
                
                # time.sleep(5)
                self.__AVERAGEFPS = frames
                frames = 0
                duration = 0
        self.__stop()

    def __start(self):
        self.__thread = threading.Thread(target=self.__run)
        self.__thread.start()
        print(self.__running)
        self.__running = 1
        print(self.__running)
        

    def __stop(self):
        self.__thread.join
        self.__running = 0

    def __update(self):
        self.__x = self.__x + 1
        

    def __draw(self):
        self.__myLabel.place(x=self.__x, y=self.__y)
        

myWindow = Window()


print("joined")



