# Google Distance and Duration Calculator

This Python script calculates driving distances and durations between a given origin and multiple destinations using the Google Distance Matrix API. It is designed to integrate travel data into your analysis workflow efficiently.

## Features

- **Input**: Reads location data (latitude, longitude) from an Excel file (`data.xlsx`).
- **Output**: Produces a new Excel file (`distance_duration_output.xlsx`) with calculated distances (in kilometers) and durations (in hours).
- **Google API Integration**: Uses the Google Maps Distance Matrix API to calculate actual road-based distances and travel times.

## Prerequisites

1. **Google API Key**:
   - Obtain a Google API key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the *Distance Matrix API* for your project.
   - Replace `'your_api_key_here'` in the script with your actual API key.

2. **Python Libraries**:
   Install required libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Prepare Input Data**:

    - Save your dataset in an Excel file named data.xlsx with the following structure:
        - A coordinates column containing concatenated latitude and longitude values in the format (lat, lon).

2. **Run the Script**:

    - Execute the script:

    ```bash
    python distance_duration_calculator.py
    ```
3. **View Results**:

    - Check the output file distance_duration_output.xlsx for calculated distances and durations.

## Example Workflow

Given the input coordinates:

**coordinates**: (-2.01234699405899, 29.377851313693) and (-1.66881597155677, 30.5838648247755)

The script calculates the driving distance and duration to each location from the origin (-2.01234699405899, 29.377851313693).

**Output Example**:
coordinates	duration (Hours)	distance (Km)
(-2.01234699405899, 29.377851313693)	0.0	0.0
(-1.66881597155677, 30.5838648247755)	1.5	78.3

## Notes

- Distances and durations are based on road networks, ensuring accurate real-world estimates.
- The first entry's distance and duration are 0.0 because it serves as the origin.

## Troubleshooting

- Ensure the Google API key is valid and has access to the Distance Matrix API.
- Verify that your input data is correctly formatted (latitude and longitude in the coordinates column).
- Check your internet connection if API requests fail.
