import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Screener API that returns HTML data
url = "https://www.screener.in/api/company/6594852/peers/"

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to fetch the HTML content
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Locate the table in the HTML response
    table = soup.find("table")  # Assuming there's only one table in the response

    if table:
        # Extract column headers
        headers = [th.get_text(strip=True) for th in table.find_all("th")]

        # Extract rows
        rows = []
        for row in table.find_all("tr")[1:]:  # Skip the header row
            columns = row.find_all("td")
            rows.append([col.get_text(strip=True) for col in columns])

        # Convert data to DataFrame
        df = pd.DataFrame(rows, columns=headers)

        # Save the DataFrame as a CSV file
        df.to_csv("peer_comparison.csv", index=False)
        print("Peer Comparison data has been saved as 'peer_comparison.csv'.")
        print(df)
    else:
        print("No table found in the HTML response.")
else:
    print(f"Failed to retrieve data: Status code {response.status_code}")
