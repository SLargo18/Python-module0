def ft_plant_age():
    days = int(input("Enter plant age in days: "))
    print("Plant is ready to harvest !" if days > 60
          else "Plant needs more time to grow")
