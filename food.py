import pandas as pd
import numpy as np

df = pd.read_csv("food-inspections.csv")

#domanda 1
#prendiamo una riga per ogni ispezione
df_un = df[~df.duplicated(subset=["Inspection ID"], keep="first")]
print(df_un.shape)
#contiamo il numero di ispezioni per tipo di facility e prendiamo il massimo
df1 = df_un.groupby("Facility Type")["Inspection ID"].count()
print(df1.idxmax())