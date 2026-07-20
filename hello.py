import fastf1
session = fastf1.get_session(2025, 13, "R" )
session.load()
lap = session.laps.pick_fastest()
pos = lap.get_pos_data()

circuit_info = session.get_circuit_info()
print(circuit_info)
session.load()
print(session.laps.head(10))
pia_laps = session.laps.pick_driver("Pia")
print(pia_laps)