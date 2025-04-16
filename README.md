Health Insurance Analysis Web App
🚀 Project by:
👤 Fedrick engels 
👤 Rohit – GitHub Profile

 
 Overview
This web-based application is designed to analyze health insurance data effectively and provide insights using modern visualization and predictive analytics tools. Built with cutting-edge technologies, it offers an intuitive platform to upload, process, and visualize insurance datasets, supporting features like classification of insurance types and cost predictions.

 Key Features
 Upload and visualize insurance data easily
 Fast prediction using trained ML models
 Multiple file formats supported – CSV, XLSX, etc.
Interactive charts and dashboards
 No installation required – 100% browser-based

Tech Stack
Component	Technologies Used
Language	Python
Libraries	pandas, scikit-learn, xgboost, tensorflow, seaborn, matplotlib
Models	Decision Tree, Random Forest, AdaBoost, XGBoost, LSTM
Interface	Command-line based


Installation and Setup
Clone the repository
git clone https://github.com/yourusername/CropPredictor.git
cd CropPredictor
Install required packages 

pip install -r requirements.txt  
Run the modules 

To predict Insurance Type:

python models/Insurance type_xgboost.py
To get a insurance type recommendation:

python models/Insurace_Type_classifier.py



           Model  Accuracy       MSE  R2 Score     Evaluation
0        XGBoost  1.000000  0.000000  1.000000  Good Accuracy
1       AdaBoost  0.871779  0.128221  0.893681  Good Accuracy
2  Decision Tree  1.000000  0.000000  1.000000  Less Accuracy
3  Random Forest  1.000000  0.000000  1.000000  Less Accuracy





 Data Handling and Assumptions
Our system is designed to process real-world insurance data reliably by implementing robust preprocessing strategies:

 Handling Missing Values
Numerical Columns: Missing values are filled using the median to reduce the effect of outliers.

Categorical Columns: Missing entries are filled with the mode to maintain the most frequent value representation.

 Data Normalization
All text inputs (such as names, categories) are normalized by converting to lowercase and trimming whitespaces to ensure consistency and avoid mismatched labels.

 Encoding for Machine Learning
Label Encoding is applied to key categorical features such as:

State – To represent geographical regions numerically.

Season – For seasonal trend analysis.

Insurance_Type – To make it suitable for model training and classification tasks.

 Real-World Input Handling
The prediction system is built to accept messy or imperfect user input and still produce accurate results. It includes:

Flexible parsing logic

Built-in preprocessing pipeline for incoming data

Graceful fallbacks for unexpected or noisy data





Contributing
Contributions are welcome. To contribute:

Fork the repository
Create a new branch (e.g., feature/new-feature)

License
This project is licensed under the MIT License.

Contact
For questions or suggestions:

Email: rohit.s2023vitstudent.ac.in
GitHub: rohit87887
