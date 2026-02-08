def ft_plant_age():
    """Checks if a plant is ready to harvest based on its age"""
    age = int(input("Enter plant age in days: "))
    print("Plant is ready to harvest!" if age > 60
          else "Plant needs more time to grow.")
