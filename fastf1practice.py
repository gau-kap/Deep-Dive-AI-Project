import fastf1
<<<<<<< HEAD
<<<<<<< HEAD
# load session
=======
>>>>>>> c7165fca6641c731dc875ce464e90957090c3e24
=======
# load session
>>>>>>> 7bba4a8f415c00a369b522647d460c75e8de997f
session = fastf1.get_session(2025, 13, "R" )
session.load()
lap = session.laps.pick_fastest()
pos = lap.get_pos_data()

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7bba4a8f415c00a369b522647d460c75e8de997f
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
=======

>>>>>>> 7bba4a8f415c00a369b522647d460c75e8de997f
circuit_info = session.get_circuit_info()
print(circuit_info)
session.load()
print(session.laps.head(10))
pia_laps = session.laps.pick_driver("Pia")
print(pia_laps)
>>>>>>> c7165fca6641c731dc875ce464e90957090c3e24
