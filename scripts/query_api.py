from stackapi import StackAPI, StackAPIError
from datetime import datetime
import pandas as pd

sitename = 'stackoverflow'
post_type = "questions"
total_pages = 25

data = []
current_page = 1

while current_page < total_pages:
    try:
        site = StackAPI(sitename)
        results = site.fetch(post_type, page=current_page)
        data.extend(results['items'])

        # increase the count        
        current_page = results['page'] + 1

    except StackAPIError as e:
        print(e)
        print("retrying...")
        continue


data_df = pd.DataFrame(data)
data_df.to_csv(f"{post_type}.csv", index=False)