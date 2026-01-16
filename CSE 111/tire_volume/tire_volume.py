import math
from datetime import date

width = float(input("Enter the tire width in mm: "))
aspect_ratio = float(input("Enter the aspect ratio: "))
diameter = float(input("Enter the wheel diameter in inches: "))

volume = (
    math.pi *
    (width ** 2) *
    aspect_ratio *
    (width * aspect_ratio + 2540 * diameter)
)  / 10000000000

current_date = date.today()

print(f"Tire volume: {volume:2f} liters")
print(f"Date: {current_date}")

with open("tire_volume_log.txt", "a") as file:
    file.write(
        f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n"
    )
    