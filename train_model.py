import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Indian_Student_Placement_Dataset_2025.csv")

# Remove columns we don't need
df = df.drop(
    ["student_id", "company_type", "package_lpa"],
    axis=1
)

# Convert text columns to numbers
le = LabelEncoder()

df["gender"] = le.fit_transform(df["gender"])
df["degree"] = le.fit_transform(df["degree"])
df["branch"] = le.fit_transform(df["branch"])

# Inputs and Output
X = df.drop("placed", axis=1)
y = df["placed"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})

print("\nFeature Importance:")
print(feature_importance.sort_values(
    by='Importance',
    ascending=False
))
import joblib

joblib.dump(model, "placement_model.pkl")

print("Model saved successfully!")