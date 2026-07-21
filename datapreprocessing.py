import pandas as pd
import numpy as np
import fastf1

all_data = []

def fuel_burnoff(df, session):
    fuel = 110
    burn_constant = 0.03
    race_laps = session.total_laps
    
    fuel_per_lap = fuel / race_laps
    remaining_fuel = fuel - (fuel_per_lap * df["lapnumber"])
    df["fuel_burnoff_laptime"] = df["laptime"] - (remaining_fuel * burn_constant)
    df["sec1_burnoff"] = df["sec1"] - ((remaining_fuel * burn_constant)/3)
    df["sec2_burnoff"] = df["sec2"] - ((remaining_fuel * burn_constant)/3)
    df["sec3_burnoff"] = df["sec3"] - ((remaining_fuel * burn_constant)/3)

    return df
    

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
            laps = laps[laps["TrackStatus"] == "1"]

            weather = weather[weather["Rainfall"] == False]
                              
            # sort the data to be chronological, rather than starting over for each driver
            laps = laps.sort_values(by="LapStartTime")
            weather = weather.sort_values(by="Time")

            # put the lap and weather data in an order similar to one another 
            lap_weather = pd.merge_asof(laps,weather,left_on="LapStartTime",right_on="Time",direction="backward")

            df = pd.DataFrame()
            df["eventname"] = [session.event["EventName"]] * len(lap_weather)  # so that every row for each lap for the race has event name
            df["driver"] = lap_weather["Driver"]
            df["compound"] = lap_weather["Compound"]
            df["stint"] = lap_weather["Stint"]
            df["tyrelife"] = lap_weather["TyreLife"]
            df["lapnumber"] = lap_weather["LapNumber"]  # !!!
            df["laptime"] = lap_weather["LapTime"].dt.total_seconds()
            df["sec1"] = lap_weather["Sector1Time"].dt.total_seconds()
            df["sec2"] = lap_weather["Sector2Time"].dt.total_seconds()
            df["sec3"] = lap_weather["Sector3Time"].dt.total_seconds()
            df["airtemp"] = lap_weather["AirTemp"]
            df["tracktemp"] = lap_weather["TrackTemp"]
            df = df.dropna(subset=["laptime", "sec1", "sec2", "sec3", "airtemp", "tracktemp"])  # so that it will drop rows that are missing critical info
            
            # making sure the data is 5 or more rows in a stint
            df = df[df.groupby(["driver", "stint"])["lapnumber"].transform("size") >= 5]

            if len(df)>0:
                df = fuel_burnoff(df, session)
                df["actual_pit_lap"] = df.groupby(["driver", "stint"])["lapnumber"].transform("max")  # to show when you start a new stint to use for prediction comparison
                df["laps_until_pit"] = df["actual_pit_lap"] - df["lapnumber"]  # to show the lap on which each driver pitted
                
                # this down look at again
                df["baseline_laptime"] = df.groupby(["driver", "stint"])["fuel_burnoff_laptime"].transform(lambda x: x.head(3).median())
                df["baseline_sec1"] = df.groupby(["driver", "stint"])["sec1_burnoff"].transform(lambda x: x.head(3).median())
                df["baseline_sec2"] = df.groupby(["driver", "stint"])["sec2_burnoff"].transform(lambda x: x.head(3).median())
                df["baseline_sec3"] = df.groupby(["driver", "stint"])["sec3_burnoff"].transform(lambda x: x.head(3).median())
                
                df["laptime_delta"] = df["fuel_burnoff_laptime"] - df["baseline_laptime"]
                df["sec1_delta"] = df["sec1_burnoff"] - df["baseline_sec1"]
                df["sec2_delta"] = df["sec2_burnoff"] - df["baseline_sec2"]
                df["sec3_delta"] = df["sec3_burnoff"] - df["baseline_sec3"]

                all_data.append(df)  

        except:
            print(f"{2025-year} {r} data not available")
            continue

full_df = pd.concat(all_data, ignore_index=True)
full_df.to_csv("full_data.csv", index=False)
print("Data processing complete.")
