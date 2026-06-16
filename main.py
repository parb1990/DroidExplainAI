import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from explainer import explain

data = pd.read_csv("sample_features.csv")

X = data.drop("Label", axis=1)
y = data["Label"]

model = RandomForestClassifier(random_state=42)

model.fit(X, y)

new_app = pd.DataFrame({
    "READ_SMS": [1],
    "SEND_SMS": [1],
    "INTERNET": [1],
    "execve": [1],
    "socket": [0]
})

prediction = model.predict(new_app)[0]

permissions = [
    "READ_SMS",
    "SEND_SMS"
]

system_calls = [
    "execve"
]

report = explain(
    prediction,
    permissions,
    system_calls
)

print(report)