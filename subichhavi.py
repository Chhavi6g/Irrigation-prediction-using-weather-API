from tkinter import *
import json
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

   
root=Tk()
root.title("Weather App")
root.geometry("840x470")
root.resizable(False, False)



# Add image file
bg = PhotoImage(file = "seminar/background2.png")
subi_label= Label(root, image=bg)
subi_label.place(x=0,y=0, relwidth=1, relheight=1)




def getWeather():
    city=textfield.get()
    geolocator= Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    ##weather
    api="https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=1ebc9d8315eaab08fd0d4ab1bd5d1fb8"
    json_data = requests.get(api).json()
    print(json_data)
    if json_data['cod'] == '404':
        print("invalid city: {}, please check your city name".format(location))
    else:
    

    ##current
        temp = (json_data['main']['temp'])
        humidity = json_data['main']['humidity']
        wind_speed = json_data['wind']['speed']
        pressure = json_data['main']['pressure']
        description= json_data['weather'][0]['description']
        

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind_speed,"m/s"))
    d.config(text=(description))
    
    #irrigation label
    irrigationbox=Label(root,text="-IRRIGATION CRITERIA-",font=('Helvetica',14),fg="#47A4ED",bg="black", width=30, height=1,anchor="center")
    irrigationbox.place(x=260,y=270)

    hbox=Label(root,text="HUMIDITY EFFECTS:",font=('Helvetica',13),fg="white",bg="black", width=20, height=1,anchor="w")
    hbox.place(x=85,y=290)

    tbox=Label(root,text="TEMPERATURE EFFECTS:",font=('Helvetica',13),fg="white",bg="black", width=25, height=1,anchor="w")
    tbox.place(x=80,y=375)





    

    data = json.dumps(humidity)
    humi = json_data['main']['humidity']
    humi = int(json_data['main']['humidity'])
    temp = json_data['main']['temp']
    temp = int(json_data['main']['temp'])
    if (humi==0):
        humibox=Label(root,text=" Vast irrigation required- no humidity present.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        humibox.place(x=100,y=325)
    elif ((humi>0) and (humi<=10)):
        humibox=Label(root,text="Profound irrigation required- only mild humidity present.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        humibox.place(x=100,y=325)
    elif ((humi>10) and (humi<=20)):
        humibox=Label(root,text="Substantial irrigation required- Cacti and succulents can survive. Air this dry will injure most houseplants.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        humibox.place(x=100,y=325)
    elif ((humi>20) and (humi<=40)):
        humibox=Label(root,text="Irrigation at regular intervals required- This is the humidity \nlevel of an average home. Some plants will be able to live, including cacti and succulents.",font=('Helvetica',12),fg="white",bg="white", width=55, height=2,anchor="center")
        humibox.place(x=100,y=325)
    elif ((humi>40) and (humi<=50)):
       humibox=Label(root,text="Moderate irrigation required- This is ideal for the flowering \nstage of mature plants.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
       humibox.place(x=100,y=325)
    elif ((humi>50) and (humi<=60)):
      humibox=Label(root,text="Occasional irrigation required- This is ideal for the vegetative\n stage of growing plants.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
      humibox.place(x=100,y=325)
    elif ((humi>60) and (humi<=80)):
      humibox=Label(root,text="Mild irrigation required(Showers expected)- This is ideal for\n a greenhouse, which can be used to grow various plants, both tropical and otherwise.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
      humibox.place(x=100,y=325)
    elif ((humi>80) and (humi<=100)):
      humibox=Label(root,text="No irrigation required(Rain expected)- This is the most ideal for\n the germination of seeds and growth of some seedlings. People would find it uncomfortable.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
      humibox.place(x=100,y=325)


        
    if ((temp >= 10) and (temp<=20)):
        tempbox=Label(root,text="Favourable for: Cardamom, Black Pepper, Flax, Cocoa, Coffee,\n Tea, Rice, Wheat, Maze, Lentil, Sugarbeet, Cotton, Rubber, Coconut.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        tempbox.place(x=100,y=410)
    elif ((temp >20) and (temp<=27)):
        tempbox=Label(root,text="Favourable for: Bajra, Pulses, Clove, Coconut, Cotton, Rabi,\n Rice, Maze, Wheat, Rubber, Sugarbeet.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        tempbox.place(x=100,y=410)
    elif ((temp >27) and (temp<=35)):
        tempbox=Label(root,text="Favourable for: Bajra, Oil palm, Clove, Cocoa, Sugarcane.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        tempbox.place(x=100,y=410)
    elif (temp >35):
        tempbox=Label(root,text="Favourable for: Black Pepper.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        tempbox.place(x=100,y=410)
    else:
        tempbox=Label(root,text="No crop can be planted in these conditions.",font=('Helvetica',12),fg="white",bg="black", width=70, height=2,anchor="center")
        tempbox.place(x=100,y=410)




       


##icon
image_icon=PhotoImage(file="seminar/logo.png")
root.iconphoto(False,image_icon)


#label
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="black")
label1.place(x=50,y=110)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="black")
label2.place(x=50,y=130)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="black")
label3.place(x=50,y=150)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="black")
label4.place(x=50,y=170)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="black")
label5.place(x=50,y=190)


#searching
textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="black",border=0,fg="white")
textfield.place(x=480,y=142)
textfield.focus()

Search_icon=PhotoImage(file="seminar/sicon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="black",command=getWeather)
myimage_icon.place(x=757,y=142)


#clock
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#47A4ED")
clock.place(x=90,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#47A4ED")
timezone.place(x=570,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#47A4ED")
long_lat.place(x=600,y=50)


##thpwd
t=Label(root,font=("Helvetica",10),fg="white",bg="black")
t.place(x=185,y=112)
h=Label(root,font=("Helvetica",10),fg="white",bg="black")
h.place(x=185,y=132)
p=Label(root,font=("Helvetica",10),fg="white",bg="black")
p.place(x=185,y=152)
w=Label(root,font=("Helvetica",10),fg="white",bg="black")
w.place(x=185,y=172)
d=Label(root,font=("Helvetica",10),fg="white",bg="black")
d.place(x=185,y=192)


    

root.mainloop()
