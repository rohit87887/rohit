stack_cls = StackingClassifier(
    estimators=[
        ('rf', RandomForestClassifier()),
        ('xgb', XGBClassifier()),
        ('ada', AdaBoostClassifier())
    ],
    final_estimator=LogisticRegression(),
    passthrough=True
)
stack_cls.fit(X_cls_train_fs, y_cls_train)
stack_preds = stack_cls.predict(X_cls_test_fs)
acc = accuracy_score(y_cls_test, stack_preds)
f1 = f1_score(y_cls_test, stack_preds, average='weighted')
print(f"Stacked Ensemble: Accuracy = {acc:.4f}, F1 Score = {f1:.4f}")
