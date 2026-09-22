import pandas as pd

input_file = "earthquake_raw.txt"
output_file = "earthquake.csv"

print("Reading seismic waveform...")

data = pd.read_csv(
    input_file,
    comment="#",
    skipinitialspace=True
)

data.columns = ["time", "sample"]

data["sample"] = pd.to_numeric(
    data["sample"],
    errors="coerce"
)

data = data.dropna()

sample_rate = 20

data["time_seconds"] = (
    data.index / sample_rate
)

output = data[
    ["time_seconds", "sample"]
]

output.columns = [
    "time",
    "acceleration"
]

output.to_csv(
    output_file,
    index=False
)

print("Conversion completed successfully.")

print("Number of samples:", len(output))

print("Sampling frequency:", sample_rate, "Hz")

print("Saved as:", output_file)