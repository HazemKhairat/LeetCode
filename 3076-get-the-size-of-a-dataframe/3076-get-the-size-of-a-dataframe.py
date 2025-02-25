import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    num_rows, num_cols = 0, 0
    for _ in players.iterrows():
        num_rows += 1
    
    for _ in players.columns:
        num_cols += 1
    
    return [num_rows, num_cols]