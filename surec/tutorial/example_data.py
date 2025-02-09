# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

import os
import zipfile
import requests
import pandas as pd
from io import BytesIO

EXAMPLE_DATA_PATH = os.path.join(os.path.dirname(__file__), "example_data")

class MovieLens100K:
    def __init__(self, save_path: str =EXAMPLE_DATA_PATH):
        self.save_path = save_path
        self.url = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
        self.column_names = ["user_id", "item_id", "rating", "timestamp"]
    
    def _if_exists(self):
        return os.path.exists(os.path.join(self.save_path, "ml-100k", "u.data"))

    def _download(self):
        if self._if_exists():
            print("MovieLens 100K dataset already exists.")
            return
        response = requests.get(self.url, stream=True)
        response.raise_for_status()
        with zipfile.ZipFile(BytesIO(response.content), 'r') as zip_ref:
            zip_ref.extractall(self.save_path)
        print(f"MovieLens 100K dataset downloaded and extracted to '{self.save_path}'")
    
    def load(self):
        ratings_path = os.path.join(self.save_path, "ml-100k", "u.data")
        if not os.path.exists(ratings_path):
            print("Dataset not found. Downloading now...")
            self._download()
        df = pd.read_csv(ratings_path, sep='\t', names=self.column_names, encoding='latin-1')
        return df


if __name__ == "__main__":
    dataset = MovieLens100K()
    df = dataset.load()
    print(df.head())