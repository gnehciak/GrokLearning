tour_locations = ['Netherlands', 'France', 'Switzerland', 'Italy', 'Spain', 'Denmark', 'Sweden', 'Finland']

# Add your code after this.

word = input("Country: ")
print(f"{word} is on the list!" if word in tour_locations else f"We will not be in {word} this time.")
