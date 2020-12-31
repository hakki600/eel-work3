import pandas as pd

class Exporter:
    @staticmethod
    def export(source, filename):
        try:
            df = pd.DataFrame(source, columns=["name"])
            df.to_csv(filename, encoding="utf_8-sig")
        except:
            pass