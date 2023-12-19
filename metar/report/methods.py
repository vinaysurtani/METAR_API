from urllib.request import urlopen
import re
import math

def setinfo(key1):
    data=urlopen(f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{key1}.TXT").read().decode('utf-8')
    datac=data.split()
    print(type(datac))
    for i in datac:
        if(re.match(r'M?\d\d\/M?\d\d',i)):
            temp=i
        if(re.match(r'\d\d\d\d\d(G\d\d(\d)?)?KT',i)):
            wind=i
    if(temp[0]=="M"):
        temp_cel=int(temp[1:3])
        temp_cel*=(-1)
    else:
        temp_cel=int(temp[0:2])
    if not wind:
        wind_vel=""
    direction = int(wind[0:3])
    if(direction > 45 and direction <= 135):
        degree = "E"
    elif(direction > 135 and direction <=225):
        degree = "S"
    elif(direction > 225 and direction <=315):
        degree = "W"
    else:
        degree = "N"
    velocity_knot = int(wind[3:5])
    if "G" in wind:
        gust = int(wind[6:8])
        wind_vel = f"{degree} at {math.floor(velocity_knot*1.151)} mph ({velocity_knot} knots) with gusts of {math.floor(gust*1.151)} mph ({gust} knots)"
    wind_vel = f"{degree} at {math.floor(velocity_knot*1.151)} mph ({velocity_knot} knots)"
    print(f"temp = {temp}")
    print(f"wind = {wind}")
    keys=["station", "last_observation", "temperature", "wind"]
    values=[f"{datac[2]}",f"{datac[0]} at {datac[1]}",f"{temp_cel} C ({math.floor((temp_cel*1.8)+32)} F)",wind_vel]
    trial = dict(zip(keys,values))
    return trial
    