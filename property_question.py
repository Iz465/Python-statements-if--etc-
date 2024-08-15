
land_sizes = [100,120,160,180,200,250]

builtup_area = [100,80,90,110,210,160]

cost = [800,750,900,910]

required_land = int(input("Enter the required land size: "))
required_builtup = int(input("Enter the required built-up area: "))
required_cost = int(input("Enter the required cost: "))

closest_builtup = builtup_area[0] # This is 100
min_difference = abs(closest_builtup-required_builtup) # Abs = absolute  value. it will show the number whether its negative or positive but with out the negative part
print("min is ",min_difference)
for area in builtup_area: # Will loop 6 times. This loop will result in closest-builtup holding the value closest to the users input
    difference = abs(area-required_builtup)
    if difference < min_difference:
        closest_builtup = area
        min_difference = difference


if required_land in land_sizes and required_cost in cost: #this checks if required_land is available in land_sizes list and required_Cost is available in cost list
    if required_builtup in builtup_area: # checks if  required built up is in built up area list
        print(f"The property with land size {required_builtup}, built-up area {required_builtup, required_cost}")
    else:
        print(f"The exact built-up area {required_builtup} is not available. The closest available built_up area is {closest_builtup} ") # Will tell yyou build up is not available, will instead show you closest built up one

else:
    print("The property with the specific land size and cost is not available")