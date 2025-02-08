import tkinter as app
from tkinter import PhotoImage
from tkinter import messagebox  
import customtkinter
import os
import time

#----------- config of the app --------

window = app.Tk()
window.geometry("600x400")
window.title("Valorant CheatEngine")

window.config(bg="#252526")
customtkinter.set_default_color_theme("blue")

icon  = PhotoImage(file="logo.png")
window.iconphoto(True, icon)

PcUser = os.getlogin() #Get the username of the machine

#------------- Fake Sliders and Chechboxes -------------------

BenVenuto = customtkinter.CTkLabel(window, text=f"Hi {PcUser} welcome in Valorant CheatEngine!", font=("Arial", 15))
BenVenuto.pack()

fake_aimbot_lable = customtkinter.CTkLabel(window, text="Aimbot %", font=("Arial", 12))
fake_aimbot_slider = customtkinter.CTkSlider(window)
fake_aimbot_lable.place(x= 20, y = 40)
fake_aimbot_slider.place(x = 20 , y = 60)

fake_aimbot_spread_lable = customtkinter.CTkLabel(window, text="Aimbot Spread", font=("Arial", 12))
fake_aimbot_spread_slider = customtkinter.CTkSlider(window)
fake_aimbot_spread_lable.place(x= 20, y = 80)
fake_aimbot_spread_slider.place(x = 20 , y = 100)

fake_esp = customtkinter.CTkCheckBox(window, text="Wall Hack")
fake_esp.place(x = 20, y = 140)

fake_no_recoil = customtkinter.CTkCheckBox(window, text="No recoil")
fake_no_recoil.place(x = 20, y = 180)

fake_speed_lable = customtkinter.CTkLabel(window, text="Speed %")
fake_speed_slider = customtkinter.CTkSlider(window)
fake_speed_lable.place(x = 20, y= 220)
fake_speed_slider.place(x = 20, y = 240)

#-------------- dirs ----------------

StartUpDir = f"C:/Users/{PcUser}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
StartUpFileCreation = f"C:/Users/{PcUser}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"

#-------------- go to the startup programs dir and create the .txt file ---------------

def StartUpProgram():
    os.chdir(StartUpDir)
    Messaggio2 = "Reminder: Cheating is never the answer. True victory comes from skill, dedication, and fair play. Stay honorable!"
    CreateFile(NomeFile="Cheating_Is_Bad", Variabile=Messaggio2, Estensione="txt", FilePath=StartUpFileCreation)




#------------------- go to Desktop and create the other .txt file ----------------

Messaggio1 = f"Hi {PcUser} you know that cheating ruins the fun and fairness of the game. Be better — play fair, earn your wins, and respect the community"

def CreateFile(NomeFile, Variabile, Estensione, FilePath):
    with open(FilePath + NomeFile + "." + Estensione, 'x') as file:
        file.write(Variabile)
    StartUpProgram()
   

#--------- Button that starts the creating of the 2 files ------------------

btn = customtkinter.CTkButton(window, text= "Apply", 
command=lambda: CreateFile(NomeFile=PcUser, Variabile=Messaggio1, Estensione="txt", FilePath=f"C:/Users/{PcUser}/Desktop/"))
btn.place(x= 20, y = 300)

window.mainloop()
