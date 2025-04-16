# 🏥 Health Insurance Analysis Web App

🚀 **Project by:**  
👤 Fedrick Engels  
👤 Rohit – [GitHub Profile](https://github.com/rohit87887)

---

## 📌 Overview

This web-based application is designed to **analyze health insurance data** and provide insights using modern **visualization** and **predictive analytics** tools. Built with cutting-edge technologies, it offers an intuitive platform to upload, process, and visualize datasets, supporting features like **classification of insurance types** and **cost prediction**.

---

## ✅ Key Features

- 📁 Upload and visualize insurance data easily  
- ⚡ Fast prediction using trained ML models  
- 📂 Supports multiple file formats – CSV, XLSX, etc.  
- 📊 Interactive charts and dashboards  
- 🌐 Fully browser-based – No installation required  

---

## 🛠️ Tech Stack

| **Component** | **Technologies Used**                             |
|---------------|----------------------------------------------------|
| Language      | Python                                              |
| Libraries     | pandas, scikit-learn, xgboost, tensorflow, seaborn, matplotlib |
| Models        | Decision Tree, Random Forest, AdaBoost, XGBoost, LSTM |
| Interface     | Command-line based                                 |

---

## 🧪 Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/CropPredictor.git
cd CropPredictor
```

### 2️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Modules

➡️ **To predict Insurance Type:**
```bash
python models/Insurance_type_xgboost.py
```

➡️ **To get an Insurance Type Recommendation:**
```bash
python models/Insurance_Type_classifier.py
```

---

## 📈 Model Evaluation

| Model           | Accuracy | MSE       | R² Score | Evaluation      |
|------------------|----------|-----------|----------|-----------------|
| XGBoost          | 1.000    | 0.000     | 1.000    | Good Accuracy   |
| AdaBoost         | 0.872    | 0.128     | 0.894    | Good Accuracy   |
| Decision Tree    | 1.000    | 0.000     | 1.000    | Less Accuracy   |
| Random Forest    | 1.000    | 0.000     | 1.000    | Less Accuracy   |

---

## 🧹 Data Handling and Assumptions

### ➔ Handling Missing Values
- **Numerical Columns:** Replaced with the **median**  
- **Categorical Columns:** Replaced with the **mode**

### ➔ Data Normalization
- All text inputs are normalized (lowercase + whitespace-trimmed)

### ➔ Encoding for ML
- **Label Encoding** applied to:
  - `State` – geographical representation  
  - `Season` – for seasonal analysis  
  - `Insurance_Type` – for classification models

### ➔ Real-World Input Handling
- Flexible parsing logic  
- Built-in preprocessing pipeline  
- Graceful fallbacks for noisy or incomplete inputs

---

## 🤝 Contributing

Contributions are welcome!  
To contribute:

1. Fork the repository  
2. Create a new branch (e.g., `feature/new-feature`)  
3. Commit and push your changes  
4. Open a Pull Request 🎉

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

📧 Email: [rohit.s2023vitstudent.ac.in](mailto:rohit.s2023vitstudent.ac.in)  
🌐 GitHub: [rohit87887](https://github.com/rohit87887)

---
