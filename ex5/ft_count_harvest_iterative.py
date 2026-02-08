def ft_count_harvest_iterative():
    """Counts the days until harvest iteratively"""
    total_days = int(input("Days until harvest: "))
    for i in range(total_days):
        if i <= total_days:
            print(f"Day {i + 1}")
    print("Harvest time!")
