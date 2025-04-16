if 'Person_ID' in df.columns:
    df.drop(columns=['Person_ID'], inplace=True)


df.dropna(inplace=True)


label_cols = ['Gender', 'Smoker', 'Pre-existing Condition', 'Insurance Type']
for col in label_cols:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])


scaler = StandardScaler()
num_cols = ['Age', 'BMI', 'Annual Premium (USD)', 'Max Insurance Budget (USD)']
df[num_cols] = scaler.fit_transform(df[num_cols])

print("✅ Encoding and scaling completed!")
print(df.head())
