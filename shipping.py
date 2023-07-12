def get_ground_cost(package_weight):
  if package_weight <= 2:
    return 1.50 + 20
  elif package_weight > 2 <= 6:
    return 3.00 + 20
  elif package_weight > 6 <= 10:
    return 4.00 + 20
  if package_weight > 10:
    return 4.75 + 20

def get_ground_premium_cost():
  return 125.00

def get_drone_cost(package_weight):
  if package_weight <= 2:
    return 4.50
  elif package_weight > 2 <= 6:
    return 9.00
  elif package_weight > 6 <= 10:
    return 12.00
  if package_weight > 10:
    return 14.25

# Obtain package weight.
package_weight = 22

# Use functions to get all weights. 
ground = get_ground_cost(package_weight)
premium = get_ground_premium_cost()
drone = get_drone_cost(package_weight)

# Control statement for minimum weight.
if ground < premium and ground < drone:
  print("Ground Shipping")
elif premium < ground and premium < drone:
  print("Premium Shipping")
elif drone < ground and drone < premium:
  print("Drone Shipping")