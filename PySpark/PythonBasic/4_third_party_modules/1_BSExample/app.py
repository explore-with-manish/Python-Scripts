import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {}

headers["user-agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

# url = "https://www.google.com/search?q=bajaj"

# req = requests.get(url, headers)

# soup = BeautifulSoup(req.content, "html.parser")
# # print(soup.prettify())

# all_links = soup.find_all("a")

# for link in all_links:
#     print(link.get("href"))

url = "https://www.screener.in/api/company/6594852/peers/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    if table:
        # Extract column headers
        table_headers = [th.get_text(strip=True) for th in table.find_all("th")]

        # Extract rows
        rows = []
        for row in table.find_all("tr")[1:]:
            columns = row.find_all("td")
            rows.append([col.get_text(strip=True) for col in columns])

        df = pd.DataFrame(rows, columns=table_headers)

        df.to_csv("mydata.csv", index=False)
