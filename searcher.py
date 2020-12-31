import pandas as pd

class Searcher:
    @staticmethod
    def search(source, word):
        if word in source:
            result = f"『{word}』はあります"
        else:
            result = f"『{word}』はありません...追加します"
            source.append(word)
        return result