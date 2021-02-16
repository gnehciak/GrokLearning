def to_kmh(knots):
    # Calculate the speed in km/h
    return 1.852 * speed


# Write the rest of your program here
import sys
speed = float(input('Speed (kn): '))
# if(range(0, 60))
if(speed < 60):
    print("Go faster!")
elif(60 <= speed < 100):
    print("Nice one.")
elif(100 <= speed < 120):
    print("Radical!")
elif(speed >= 120):
    print("Whoa! Slow down!")
"""
Speed Range	Message
<60 km/h	Go faster!
≥60 km/h and <100 km/h	Nice one.
≥100 km/h and <120 km/h	Radical!
≥120 km/h	Whoa! Slow down!
"""
