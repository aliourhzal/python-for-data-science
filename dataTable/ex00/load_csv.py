import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path)
        pd.set_option('display.max_rows', 2)
        print(data)
        return data
    except FileNotFoundError:
        print("error: no such file!")
        return pd.DataFrame()
    except Exception as e:
        print(f"error: {e}")
        return pd.DataFrame()
