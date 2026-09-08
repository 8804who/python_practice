import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    temp = pd.merge(employee, bonus, on="empId", how="left")
    temp = temp[(temp["bonus"] < 1000) | (temp["bonus"].isna())][["name", "bonus"]]
    return temp