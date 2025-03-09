import json

# Load the GeoJSON file
with open('/Users/sluger/Downloads/garmingravel.geojson', 'r') as file:
    data = json.load(file)

# Initialize variables
previous_altitude = None
downhill_sum = 0
uphill_sum = 0

# Iterate over the features
for feature in data['features']:
    if feature['geometry']['type'] == 'Point':
        current_altitude = feature['properties']['altitude']
        if previous_altitude is not None and current_altitude < previous_altitude:
            downhill_sum += abs(previous_altitude - current_altitude)
        elif previous_altitude is not None and current_altitude > previous_altitude:
            uphill_sum += abs(current_altitude - previous_altitude)
        previous_altitude = current_altitude

# Print the result
print(f"Uphill: {uphill_sum} meters")
print(f"Downhill: {downhill_sum} meters")