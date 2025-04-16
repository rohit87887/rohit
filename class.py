X_cls = df.drop(columns=['Insurance Type', 'Annual Premium (USD)'])
y_cls = df['Insurance Type']
X_cls_train, X_cls_test, y_cls_train, y_cls_test = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

selector_cls = SelectFromModel(RandomForestClassifier(random_state=42)).fit(X_cls_train, y_cls_train)
X_cls_train_fs = selector_cls.transform(X_cls_train)
X_cls_test_fs = selector_cls.transform(X_cls_test)

models_cls = {
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "AdaBoost": AdaBoostClassifier(),
    "XGBoost": XGBClassifier()
}

print("📊 Classification Results (with Feature Selection):")
for name, model in models_cls.items():
    model.fit(X_cls_train_fs, y_cls_train)
    preds = model.predict(X_cls_test_fs)
    acc = accuracy_score(y_cls_test, preds)
    f1 = f1_score(y_cls_test, preds, average='weighted')
    print(f"{name}: Accuracy = {acc:.4f}, F1 Score = {f1:.4f}")
