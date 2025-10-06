import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dữ liệu
df = pd.read_csv("loan_approval_dataset.csv")

# Xóa khoảng trắng trong tên cột
df.columns = df.columns.str.strip()

# Biểu đồ loan_status
plt.figure(figsize=(5,4))
sns.countplot(x="loan_status", data=df, palette="Set2")
plt.title("Tỷ lệ duyệt / không duyệt khoản vay")
plt.show()

# Biểu đồ education
plt.figure(figsize=(5,4))
sns.countplot(x="education", hue="loan_status", data=df, palette="Set3")
plt.title("Tình trạng duyệt vay theo trình độ học vấn")
plt.show()

# Histogram income_annum
plt.figure(figsize=(6,4))
sns.histplot(df["income_annum"], bins=30, kde=True)
plt.title("Phân phối thu nhập khách hàng (income_annum)")
plt.xlabel("Thu nhập hàng năm")
plt.show()

# Boxplot income_annum vs loan_status
plt.figure(figsize=(6,4))
sns.boxplot(x="loan_status", y="income_annum", data=df, palette="Set1")
plt.title("So sánh thu nhập theo trạng thái khoản vay")
plt.show()

# Countplot theo số người phụ thuộc
plt.figure(figsize=(6,4))
sns.countplot(x="no_of_dependents", hue="loan_status", data=df, palette="Set2")
plt.title("Ảnh hưởng số người phụ thuộc tới trạng thái duyệt vay")
plt.show()

# Boxplot CIBIL score vs loan_status
plt.figure(figsize=(6,4))
sns.boxplot(x="loan_status", y="cibil_score", data=df, palette="Set3")
plt.title("Điểm tín dụng (CIBIL) theo trạng thái duyệt vay")
plt.show()
