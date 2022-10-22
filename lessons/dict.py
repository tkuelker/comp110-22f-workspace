"""Demonstrations of dictiionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# prints a dictionary literal representation
print(schools)

# Acess a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair form a dict by its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# update key-value pair
schools["UNC"] = 2000
schools["NCSU"] += 200

# demonstration of dictionary literals

# empty dictionary literal
schools = {} # same as dict()

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

print(type(schools))
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
print(type(school))
print(type(schools[school]))