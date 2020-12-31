import pandas as pd

class Controller:
    def __init__(self):
        df = pd.read_csv("./characters_kimetsu.csv", encoding="SHIFT-JIS")
        self.characters = list(df["name"])