import pandas as pd
import numpy as np
import fastf1

all_data = []
# looping through 2025-2022, inclusive, going through each race for each year to add to the dataframe

# using a try-except block so as to handle errors happening when some races are not available
# https://www.w3schools.com/python/python_try_except.asp where I learned the syntax
for year in range(4):
    races = fastf1.get_events(2025-year)
    for r in range(1, len(races)+1):
        try:
            session = fastf1.get_session(2025-year, r, "R")  
            session.load(laps=True, weather=True, telemetry=False)
            
            laps = session.laps.copy()
            weather = session.weather_data.copy()

            laps = laps[laps["IsAccurate"] == True]
            laps = laps[laps["TrackStatus"] == 1]

            weather = weather[weather["Rainfall"] == False
                              
            # sort the data to be chronological, rather than starting over for each driver
            # DO THIS LATER

            df["eventname"] = session.event["EventName"]
            df["stint"] = laps["Stint"]
            df["tyreage"] = laps["TyreAge"]
            df["laptime"] = laps["LapTime"]
            df["sec1"] = laps["Sector1Time"]
            df["sec2"] = laps["Sector2Time"]
            df["sec3"] = laps["Sector3Time"]
        
            
        except:
            print(f"{2025-year} {r} data not available")
            continue
