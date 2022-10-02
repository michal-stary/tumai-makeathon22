import pandas as pd

def preproc(df):

    df["risk"] = df["Is the AI System high-risk or low risk?"]
    df["name"]  = df["Use case name EN"]
    df["desc"] = df["Description"]
    df["bus_ch"] = df["Business Challenge"] 
    df["system"] = df["AI System"]

    df = df.fillna("")


    df = df[df["risk"] != "It is unclear"]
    df = df[df["risk"] != ""]
    
    return df