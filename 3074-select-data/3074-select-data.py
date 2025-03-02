import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    res = students.loc[students['student_id'] == 101]
    return res.iloc[:,1:]