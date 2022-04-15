weight = 41.5
flat_charge = 20

# Ground Shipping

if weight <= 2:
    ground_charge = weight * 1.5 + flat_charge
elif weight <= 6:
    ground_charge = weight * 3 + flat_charge
elif weight <= 10:
    ground_charge = weight * 4 + flat_charge
elif weight > 10:
    ground_charge = weight * 4.75 + flat_charge
else:
    ground_charge = ""

# Ground Shipping Premium

ground_premium_charge = 125

# Ground Shipping

if weight <= 2:
    drone_charge = weight * 4.5
elif weight <= 6:
    drone_charge = weight * 9
elif weight <= 10:
    drone_charge = weight * 12
elif weight > 10:
    drone_charge = weight * 14.25
else:
    drone_charge = ""

print("Cost of Ground Shipping: $", round(ground_charge, 2))
print("Cost of Ground Premium Shipping: $", round(ground_premium_charge, 2))
print("Cost of Drone Shipping: $", round(drone_charge, 2))