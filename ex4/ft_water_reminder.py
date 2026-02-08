def ft_water_reminder():
    """"Checks if plants need watering"""
    watering = int(input("Days since last watering: "))
    print("Plants are fine" if watering < 2 else "Water the plants!")
