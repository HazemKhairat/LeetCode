import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columnsNames = ["student_id", "age"]
    resDataFrame = pd.DataFrame(student_data, columns=columnsNames)
    return resDataFrame
    # return pd.DataFrame(student_data, columns=["student_id", "age"])