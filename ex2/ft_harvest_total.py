def ft_harvest_total():
    total_days = 3
    days = 0
    i = 0
    while i < total_days:
        days += int(input(f"Day {i + 1} harvest: "))
        i += 1
    print("Total harvest:", days)
