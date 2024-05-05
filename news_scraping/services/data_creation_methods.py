import os
from datetime import datetime
import sys

import pandas as pd


class DataCreationMethods():

    def __init__(self):
        self.app_path = os.path.dirname(sys.executable)
        self.now = datetime.now()
        self.now_date_str = self.now.strftime("%d_%m_%Y_%p_%I_%M")

    def add_list_to_csv(self, articles):
        df = pd.DataFrame(articles)
        file_name = f"Ynet_{self.now_date_str}.csv"
        final_path = os.path.join(self.app_path, file_name)

        csv_file_path = final_path

        try:
            df_existing = pd.read_csv(csv_file_path)
        except:
            df.to_csv(csv_file_path, index=False)
        else:
            df_combine = pd.concat([df_existing, df], ignore_index=True)
            df_combine.to_csv(csv_file_path, index=False)
