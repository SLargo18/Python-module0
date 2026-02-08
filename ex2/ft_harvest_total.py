def ft_harvest_total():
    """Calculate total harvest over a period of days"""
    total = 0
    i = 0
    while i < 3:
        total += int(input(f"Day {i + 1} harvest: "))
        i += 1
    print("Total harvest:", total)
