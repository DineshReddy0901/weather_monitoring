from tkinter import *
from tkinter import ttk
import requests
def weather_update():
  city = city_name.get()
# city = "hyderabad"
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q= "+city+"&appid=2b0d2b670b1375d747de2461c9c31c69").json()
  # w_label1.config(text=data["weather"][0]["main"])
  # wd_label.config(text=data["weather"][0]["description"])
  t_label1.config(text=int(data["main"]["temp"]-273.15))
  p_label1.config(text=data["main"]["pressure"])
  
# print(data)


win = Tk()
win.title("Weather App")
win.geometry("500x500")
win.config(bg="pink")
heading = Label(win,text="Weather App",font=("Arial",40,"bold"),bg="pink",fg="black")
heading.pack(pady=30)
city_name = StringVar()
states_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
states_box = ttk.Combobox(win,values=states_name,font=("Arial",50,"bold"),width=15,textvariable=city_name)
states_box.pack(pady="5",side="top")



w_label= Label(win,text="Weather Climate:",font=("Arial",15,"bold"),bg="pink")
w_label.place(y=300,x=60)
w_label1= Label(win,text="",font=("Arial",15,"bold"),bg="pink")
w_label1.place(y=300,x=300)


wd_label= Label(win,text="Weather Description:",font=("Arial",15,"bold"),bg="pink")
wd_label.place(y=330,x=60)
wd_label1= Label(win,text="",font=("Arial",15,"bold"),bg="pink")
wd_label1.place(y=330,x=300)


t_label= Label(win,text="Temperature:",font=("Arial",15,"bold"),bg="pink")
t_label.place(y=360,x=60)
t_label1= Label(win,text="",font=("Arial",15,"bold"),bg="pink")
t_label1.place(y=360,x=300)


p_label= Label(win,text="Pressure:",font=("Arial",15,"bold"),bg="pink")
p_label.place(y=390,x=60)
p_label1= Label(win,text="",font=("Arial",15,"bold"),bg="pink")
p_label1.place(y=390,x=300)

Button_first = Button(win,text="Done",font=("Arial",20,"bold"),bg="pink",fg="black",command=weather_update)
Button_first.pack(pady=30)
Button_first.place(y=240,height=30,width=80,x=210)

win.mainloop()