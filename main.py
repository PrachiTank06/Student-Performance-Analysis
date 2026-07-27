import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("images", exist_ok=True)
data = pd.read_csv("student/student-mat.csv", sep=";")

print("="*50)
print("STUDENT PERFORMANCE ANALYSIS")
print("="*50)
print(data.head())
print(data.shape)
print(data.info())
print(data.columns)
print(data.describe())
print(data.isnull().sum())

import os

os.makedirs("images", exist_ok=True)

plt.figure(figsize=(8,5))
data["age"].hist(bins=8, edgecolor="black")

plt.title("Distribution of Student Age")
plt.xlabel("Age")
plt.ylabel("Number of Students")

plt.savefig("images/age_distribution.png")
plt.show()

gender = data["sex"].value_counts()

plt.figure(figsize=(6,5))
gender.plot(kind="bar", color=["skyblue","pink"])

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Students")

plt.savefig("images/gender_distribution.png")
plt.show()

internet = data["internet"].value_counts()

plt.figure(figsize=(6,6))
internet.plot(kind="pie", autopct="%1.1f%%")

plt.title("Internet Access")
plt.ylabel("")

plt.savefig("images/internet_access.png")
plt.show()

plt.figure(figsize=(8,5))
data["G3"].hist(bins=20, edgecolor="black")

plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")

plt.savefig("images/final_grade_distribution.png")
plt.show()

average_marks = data[["G1", "G2", "G3"]].mean()

plt.figure(figsize=(6,5))
plt.bar(["G1","G2","G3"], average_marks,
        color=["red","blue","green"])

plt.title("Average Grades")
plt.xlabel("Exam")
plt.ylabel("Average Marks")

plt.savefig("images/average_grades.png")
plt.show()

print("\n========== GRADE ANALYSIS ==========")

print("Average Final Grade :", data["G3"].mean())
print("Highest Final Grade :", data["G3"].max())
print("Lowest Final Grade  :", data["G3"].min())

study_grade = data.groupby("studytime")["G3"].mean()

print("\nAverage Grade by Study Time")
print(study_grade)

plt.figure(figsize=(6,5))

study_grade.plot(kind="bar", color="green")

plt.title("Average Final Grade by Study Time")
plt.xlabel("Study Time")
plt.ylabel("Average Final Grade")

plt.savefig("images/studytime_vs_grade.png")

plt.show()

mother_grade = data.groupby("Medu")["G3"].mean()

plt.figure(figsize=(6,5))

mother_grade.plot(kind="bar", color="orange")

plt.title("Average Grade by Mother's Education")
plt.xlabel("Mother's Education")
plt.ylabel("Average Grade")

plt.savefig("images/mother_education_vs_grade.png")

plt.show()

father_grade = data.groupby("Fedu")["G3"].mean()

plt.figure(figsize=(6,5))

father_grade.plot(kind="bar", color="purple")

plt.title("Average Grade by Father's Education")
plt.xlabel("Father's Education")
plt.ylabel("Average Grade")

plt.savefig("images/father_education_vs_grade.png")

failure_grade = data.groupby("failures")["G3"].mean()

plt.figure(figsize=(6,5))

failure_grade.plot(kind="bar", color="red")

plt.title("Average Grade by Previous Failures")
plt.xlabel("Failures")
plt.ylabel("Average Grade")

plt.savefig("images/failures_vs_grade.png")

plt.show()

plt.figure(figsize=(6,5))

plt.scatter(data["G1"], data["G3"])

plt.title("G1 vs G3")
plt.xlabel("G1")
plt.ylabel("G3")

plt.savefig("images/g1_vs_g3.png")

plt.show()

import seaborn as sns

correlation = data.corr(numeric_only=True)

print("\n========== CORRELATION MATRIX ==========")
print(correlation)

plt.figure(figsize=(12,8))

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.savefig("images/correlation_heatmap.png")

plt.show()

print("\n========== CORRELATION WITH G3 ==========")

print(correlation["G3"].sort_values(ascending=False))

print("\n========== TOP 10 STUDENTS ==========")

top_students = data.sort_values(by="G3", ascending=False)

print(top_students[["G1","G2","G3"]].head(10))

print("\n========== BOTTOM 10 STUDENTS ==========")

bottom_students = data.sort_values(by="G3", ascending=True)

print(bottom_students[["G1","G2","G3"]].head(10))

print("\n")
print("="*50)
print("      STUDENT PERFORMANCE ANALYSIS")
print("="*50)

print("Dataset Shape :", data.shape)
print("Average Final Grade :", round(data["G3"].mean(),2))
print("Highest Grade :", data["G3"].max())
print("Lowest Grade :", data["G3"].min())

print("\nProject Completed Successfully!")

print("="*50)