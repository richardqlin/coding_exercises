from datetime import date, datetime
today = date.today()
now = datetime.now()
d= now.strftime("%Y-%m-%d")
t = now.strftime("%H:%M:%S")
print("Today's date:",d, 'now=',t)
import weather_forecast as wf
wf.forecast(place ='Hayward', time=t,date=d, forecast='daily')
