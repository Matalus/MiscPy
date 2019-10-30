first_name = "Matt"
last_name = "Hamende"

print(first_name + last_name)

#using standard concat
print("Hello, "  + first_name.capitalize() + " " + last_name.capitalize())

#using F strings
print(f"Hello, {first_name.capitalize()} {last_name.capitalize()}")

print("Hello, {} {}".format(first_name.capitalize(), last_name.capitalize()))

#reverse
print("Hello, {1} {0}".format(first_name.capitalize(), last_name.capitalize()))