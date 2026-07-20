import fastf1
# load session
session = fastf1.get_session(2025, 13, "R" )
session.load()
lap = session.laps.pick_fastest()
pos = lap.get_pos_data()
# get circuit info
circuit_info = session.get_circuit_info()
# print(circuit_info)
session.load()
# print(session.laps.head(10))

# Piastri practice
pia_laps = session.laps.pick_drivers("Pia")
# print(pia_laps)

# print(pia_laps["TyreLife"])
print(session.laps.columns) 
print(session.laps["Stint"])
print(pia_laps["Stint"])
print(pia_laps["TrackStatus"])

print(session.weather_data)
    
circuit_info = session.get_circuit_info()
print(circuit_info)
session.load()
print(session.laps.head(10))
pia_laps = session.laps.pick_driver("Pia")
print(pia_laps)
