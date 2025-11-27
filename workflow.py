import pandas as pd

# 1. Create a simple dataframe directly in code
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [24, 30, 29, 22],
    "score": [88, 92, 85, 90]
}

df = pd.DataFrame(data)

print("\n--- Original DataFrame ---")
print(df)

# 2. Basic transformations

# 2.1 Add a new column: Passed or Not (score >= 85)
df["passed"] = df["score"] >= 85

# 2.2 Add a bonus score (+5 points)
df["score_with_bonus"] = df["score"] + 5

print("\n--- Transformed DataFrame ---")
print(df)

# 3. Save result to a CSV file in the SAME folder as this script
df.to_csv("results.csv", index=False)

print("\nFile saved locally as: results.csv")
