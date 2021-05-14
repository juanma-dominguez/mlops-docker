import json

import joblib
import pandas as pd

data_json = "model/data.json"
model = "model/model.pkl"

with open(data_json, 'r') as f:
    data = json.load(f)
df = pd.DataFrame([data])

print(df.head())
model = joblib.load(model)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df)
df_x_scaled = scaler.transform(df)
df_x_scaled = pd.DataFrame(df_x_scaled, columns=df.columns)
y_predict = model.predict(df_x_scaled)
result = {"Predicted House Price" : y_predict[0]}
print(result)
