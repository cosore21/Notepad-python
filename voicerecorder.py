from tkinter import*
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv


root=Tk()

root.geometry("700x800+400+90")
root.resizable(False,False)
root.title("Voice Recorder ")

root.configure(background="grey")


def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq, samplerate=freq,channels=2)
    
    #timer
    try:
        temp=int(duration.get())
    except:
        print("Please enter the Right Value")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1


        if(temp==0):
             messagebox.showinfo("Time Countdown","Time is Up!!")
        Label(text=f"{str(temp)}",font="Roman 30",width=4,bg="Grey").place(x=240,y=590)


    sound.wait()
    write("recording.wav",freq,recording)

#icon
#image_icon=PhotoImage(file="")
#root.iconphoto(False,image_icon)

#logo
#photo=PhotoImage(file="")
#myimage=Label(image=photo,background="green")
#myimage.pack(padx=5,pady=5)

#name
Label(text="Voice Recorder",font="Romans 30 bold", background="grey",fg="white").pack()

#entry Box
duration=StringVar()
entry=Entry(root,textvariable=duration,font="romans 24",width=16).pack(pady=10)
Label(text="Enter time in seconds",font="Romans 14",bg="grey",fg="white").pack()

#Button
record=Button(root,font="Roman 18",text="Record",bg="Green",fg="white",border=0, command=Record).pack()



root.mainloop()