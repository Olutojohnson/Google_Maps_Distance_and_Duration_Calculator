# Import necessary libraries
import pandas as pd
import googlemaps

# Load the dataset
data = pd.read_excel('data.xlsx', sheet_name='data')

# Google API key (replace 'your_api_key_here' with your actual API key)
API_key = 'your_api_key_here'
gmaps = googlemaps.Client(key=API_key)

# Define the origin point
origin = (-2.01234699405899, 29.377851313693)

# Initialize lists for storing results
actual_duration = []
actual_distance = []

# Calculate durations and distances
for destination in data['coordinates']:
    # Fetch duration (in hours)
    duration_result = gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["duration"]["value"]
    duration_hours = duration_result / 3600
    actual_duration.append(duration_hours)

    # Fetch distance (in kilometers)
    distance_result = gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
    distance_km = distance_result / 1000
    actual_distance.append(distance_km)

# Add the calculated values to the dataset
data["duration (Hours)"] = actual_duration
data["distance (Km)"] = actual_distance

# Display the first 15 rows of the dataset
print(data.head(15))

# Save the updated dataset to a new file
data.to_excel('distance_duration_output.xlsx', index=False)
