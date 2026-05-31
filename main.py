import requests

launches = requests.get(
    "https://api.spacexdata.com/v4/launches"
).json()

print(f"Number of launches returned: {len(launches)}")
print()

for launch in launches[-5:]:
    print(launch["name"], "-", launch["date_utc"])