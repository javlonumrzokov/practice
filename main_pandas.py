import pandas as pd
import numpy as np

df = pd.read_csv("StudentsPerformance.csv")

print("Datasset shape (rows , columns)", df.shape)

print("Column name:", df.columns.tolist())
print("First 5 rows of dataset")
print(df.head())

print("Summary statistics:")
print(df.describe())

print("Data types and null infos:")
print(df.info())

print("Average score of subjects by students:")
print(df[["math score", "reading score", "writing score"]].mean())

print("Max score of subjects by students:")
print(df[["math score", "reading score", "writing score"]].max())

print("Minimum score of subjects by students:")
print(df[["math score", "reading score", "writing score"]].min())


print("Correlation:")
print(df[["math score", "reading score", "writing score"]].corr())

df["total score"] = df[["math score",
                        "reading score", "writing score"]].sum(axis=1)
df["average score"] = df["total score"] / 3
df["passed"] = np.where(df["average score"] >= 50, "Yes", "No")

print("New column preview (total, average and passed):")
print(df[["total score", "average score", "passed"]].head())

print("Column name:", df.columns.tolist())

#  test preparation course based average
test_prep_group = df.groupby('test preparation course')[
    ["math score", "reading score", "writing score"]].mean()

print("Student score by test preparation course:")
print(test_prep_group)

#  gender based average
gender_group = df.groupby('gender')[
    ["math score", "reading score", "writing score"]].mean()

print("Student score by gender:")
print(gender_group)

# passed vs failed
pass_rate = df["passed"].value_counts(normalize=True) * 100
print("Pass rate\n", pass_rate)

# Convert scores to Numpy array
scores = df[["math score", "reading score", "writing score"]].values

# Mean, Std
print("Numpy Mean:", np.mean(scores, axis=0))
print("Numpy Std:", np.std(scores, axis=0))

# Z-score (normalize)
z_score = (scores - np.mean(scores, axis=0)) / np.std(scores, axis=0)

print("Z scores (normalized) numbers:")
print(z_score[:5])
# if 0 average student
# if negative average student dan past
# if positive average student dan yuqorida

# How many student scored above 90?
top_scorers = df[df["average score"] >= 90]
print("Top students scored above 90:", len(top_scorers))

failed = df[df["passed"] == "No"]
print("Failed students:", len(failed))
