import urllib.request

url = (
    "https://service.earthscope.org/fdsnws/dataselect/1/query"
    "?net=IU"
    "&sta=ANMO"
    "&loc=00"
    "&cha=BHZ"
    "&start=2010-02-27T06:30:00"
    "&end=2010-02-27T06:35:00"
    "&format=geocsv"
)

print("Downloading real seismic waveform...")

try:
    urllib.request.urlretrieve(
        url,
        "earthquake_raw.txt"
    )

    print("Download completed successfully.")
    print("Saved as earthquake_raw.txt")

except Exception as e:
    print("Download failed.")
    print("Error:", e)