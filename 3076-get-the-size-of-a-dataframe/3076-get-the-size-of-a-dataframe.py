import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    dimensions = list(players.shape)
    return dimensions