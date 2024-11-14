import urllib.request
import json
from datetime import datetime

url = "https://api.wordpress.org/stats/plugin/1.0/downloads.php?slug=akismet&limit=365"

# Fetch data using urllib
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

# Process data to convert timestamps to datetime and downloads to integers
data_processed = [
    {
        "timestamp": datetime.strftime(
            datetime.strptime(timestamp, "%Y-%m-%d"), "%Y-%m-%d"
        ),
        "downloads": int(downloads),
    }
    for timestamp, downloads in data.items()
]

print(data_processed)

# print(datetime.strptime("2023-11-15", "%Y-%m-%d"))

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import style
# import requests

# url = "https://api.wordpress.org/stats/plugin/1.0/downloads.php?slug=akismet&limit=365"
# r = requests.get(url)
# data = r.json()

# # print(data)

# data = [
#     {"timestamp": pd.to_datetime(timestamp, utc=False), "downloads": int(downloads)}
#     for (timestamp, downloads) in data.items()
# ]

# print(data)

# df = pd.DataFrame(data)
# df = df.set_index('timestamp')

# # print(df)

# weekly_average = df.rolling(window=7).mean()
# weekly_sum = df.rolling(window=7).sum()

# df.columns = ['Daily Downloads']
# weekly_average.columns = ['Weekly Average']
# weekly_sum.columns = ['Weekly Sum']

# style.use('ggplot')
# fig, ax = plt.subplots()

# ax.legend(loc="best")

# df.plot(ax=ax, label="Daily Downloads",
#         legend=True, style='r-', title="Downloads")
# weekly_average.plot(ax=ax, label="7 Day Average", legend=True, style='b-')
# weekly_sum.plot(ax=ax, label="7 Day Sum", legend=True, style='g--')

# plt.show()
