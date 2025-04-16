import pandas as pd

df = pd.read_csv("updated_health_insurance_dataset.csv")
summary = df.describe(include='all')
print("Summary Statistics:\n", summary)

def calculate_statistics(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    mean = sum(sorted_data) / n

    median = (sorted_data[n//2] if n % 2 else (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2)

    min_value, max_value = sorted_data[0], sorted_data[-1]

    variance = sum((x - mean) ** 2 for x in sorted_data) / n
    std_dev = variance ** 0.5

    return mean, median, min_value, max_value, std_dev

stats_results = {
    col: calculate_statistics(df[col].dropna().tolist())
    for col in df.select_dtypes(include=["number"]).columns
}

stats_df = pd.DataFrame.from_dict(stats_results, orient='index',
 columns=['Mean', 'Median', 'Min', 'Max', 'Std Dev'])

print("Custom Statistical Summary:\n", stats_df)
print("Missing Values:\n", df.isnull().sum())
print("Unique Values:\n", df.nunique())
