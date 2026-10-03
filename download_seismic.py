
import urllib.request

url = (
    "https://service.earthscope.org/fdsnws/dataselect/1/query"
    "?net=IU"
    "&sta=MAJO"
    "&loc=00"
    "&cha=BHZ"
    "&start=2011-03-11T05:45:00"
    "&end=2011-03-11T05:52:00"
    "&format=geocsv"
)

output_file = "earthquake_raw.txt"

print("Downloading Tohoku earthquake seismic waveform...")
print("Station: IU.MAJO.00.BHZ")
print("Time: 2011-03-11 05:45:00 to 05:52:00 UTC")

try:
    urllib.request.urlretrieve(
        url,
        output_file
    )

    print()
    print("Download completed successfully.")
    print("Saved as:", output_file)

except Exception as e:
    print()
    print("Download failed.")
    print("Error:", e)
