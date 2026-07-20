import fastf1
# load session
session = fastf1.get_session(2025, 13, "R" )
session.load()
lap = session.laps.pick_fastest()
pos = lap.get_pos_data()
<<<<<<< HEAD

=======
>>>>>>> 07e389c9c1acc41718ddf98ccdb93e10b15e0995
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
<<<<<<< HEAD

=======
    
>>>>>>> 07e389c9c1acc41718ddf98ccdb93e10b15e0995
circuit_info = session.get_circuit_info()
print(circuit_info)
session.load()
print(session.laps.head(10))
pia_laps = session.laps.pick_drivers("Pia")
print(pia_laps)
<<<<<<< HEAD

print("commit check")
=======
>>>>>>> 07e389c9c1acc41718ddf98ccdb93e10b15e0995
