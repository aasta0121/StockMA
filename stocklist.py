import requests
import numpy as np
import pandas as pd

link = 'https://quality.data.gov.tw/dq_download_json.php?nid=11549&md5_url=bb878d47ffbe7b83bfc1b41d0b24946e'
r = requests.get(link)
data = pd.DataFrame(r.json())

print(data.loc['證卷代號'])