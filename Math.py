import math

# Ask the user for an angle in degrees
angle_deg = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate sin, cos, and tan
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

# Display the results
print(f"sin({angle_deg}) = {sin_value}")
print(f"cos({angle_deg}) = {cos_value}")
print(f"tan({angle_deg}) = {tan_value}")