import tkinter as tk
import requests
HEIGHT=500
WIDTH=500
#76a94b0bbb836a6b73b3716754111ff7
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def format_response(weather_json):
	try:
		name=weather_json['name']
		desc=weather_json['weather'][0]['description']
		temp=weather_json['main']['temp']
		final_str='City: %s \nConditions:%s \nTemperature:%s°C'%(name,desc,temp)

	except:
		final_str='Please try again'

	return final_str

def get_weather(city):
	weather_key='76a94b0bbb836a6b73b3716754111ff7'
	url='https://api.openweathermap.org/data/2.5/weather'
	params={'APPID':weather_key,'q':city,'units':'metric'}
	response=requests.get(url,params=params)
	weather_json=response.json()

	
	

	label['text']=format_response(weather_json)


root=tk.Tk()
root.title('Weather')

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_img=tk.PhotoImage(file='landscape.png')
backgroung_label=tk.Label(root,image=background_img)
backgroung_label.place(x=0,y=0,relwidth=1,relheight=1)

frame=tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=('Courier',12))
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text='Get weather',bg='gray',font=('Courier',10),command=lambda:get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

l_frame=tk.Frame(root,bg='#80c1ff',bd=10)
l_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')


label=tk.Label(l_frame,font=('Courier',18),anchor='nw',bd=5,justify='left')
label.place(relwidth=1,relheight=1)


 

root.mainloop()