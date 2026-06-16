import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("sample_features.csv")

# Features
X = data.drop("Label", axis=1)

# Target
y = data["Label"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# New app to test
new_app = pd.DataFrame({
    "READ_SMS": [1],
    "SEND_SMS": [1],
    "INTERNET": [1],
    "execve": [1],
    "socket": [0]
})
prediction = model.predict(new_app)
print("Prediction:", prediction[0])