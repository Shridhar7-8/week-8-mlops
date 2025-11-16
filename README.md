# 🧪 Week 8: MLOps - Data Poisoning Experiments

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

*Exploring the impact of data poisoning on machine learning model performance*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Experiment Results](#-experiment-results)
- [Key Insights](#-key-insights)
- [MLflow UI](#-mlflow-ui)
- [Contributing](#-contributing)

---

## 🎯 Overview

This project demonstrates the **critical impact of data quality** on machine learning models by systematically introducing label poisoning attacks to the classic Iris dataset. Through controlled experiments, we explore how different levels of data corruption affect model accuracy and what this means for real-world MLOps practices.

### 🔬 What is Data Poisoning?

Data poisoning is a security threat where malicious actors intentionally corrupt training data by:
- Flipping labels (e.g., changing "setosa" to "virginica")
- Injecting misleading samples
- Manipulating feature values

This project focuses on **label flipping** to demonstrate its devastating effects on model performance.

---

## ✨ Features

- 🎲 **Configurable Poisoning Rates**: Test with 0%, 5%, 10%, and 50% label corruption
- 📊 **MLflow Integration**: Automatic experiment tracking and model logging
- 🌳 **Decision Tree Classifier**: Simple yet effective model for demonstration
- 📈 **Automated Experiments**: Batch processing via shell script
- 📝 **Detailed Analysis**: Comprehensive documentation of findings
- 🔄 **Reproducible Results**: Fixed random seeds for consistency

---

## 🛠 Tech Stack

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python** | Core language | 3.8+ |
| **scikit-learn** | ML modeling | Latest |
| **MLflow** | Experiment tracking | Latest |
| **pandas** | Data manipulation | Latest |
| **NumPy** | Numerical operations | Latest |

---

## 📁 Project Structure

```
week-8-mlops/
├── 📊 data/
│   └── iris.csv              # Iris dataset with features and labels
├── 🐍 train.py               # Main training script with poisoning logic
├── 🔄 run_experiments.sh     # Automated experiment runner
├── 📋 requirements.txt       # Python dependencies
├── 📖 ANALYSIS.md           # Detailed analysis and findings
├── 🚫 .gitignore            # Git ignore rules
└── 📘 README.md             # You are here!
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shridhar7-8/week-8-mlops.git
   cd week-8-mlops
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python --version
   mlflow --version
   ```

---

## 💻 Usage

### Running Individual Experiments

Train a model with a specific poisoning rate:

```bash
python train.py --data data/iris.csv --depth 3 --poison_rate 0.10
```

**Parameters:**
- `--data`: Path to the CSV dataset
- `--depth`: Maximum depth of the Decision Tree (default: 3)
- `--poison_rate`: Fraction of labels to corrupt (0.0 to 1.0)

### Running All Experiments

Execute the full suite of experiments:

```bash
# On Linux/Mac
bash run_experiments.sh

# On Windows (Git Bash or WSL)
bash run_experiments.sh
```

This will run experiments with poison rates: **0%**, **5%**, **10%**, and **50%**.

---

## 📊 Experiment Results

### Actual Accuracy Results (From Live Experiments)

| Poison Rate | Actual Accuracy | Interpretation |
|-------------|----------------|----------------|
| **0% (Clean)** | **98.33%** | 🎯 Baseline performance with pristine data - excellent classification |
| **5%** | **88.33%** | ⚠️ Noticeable 10% accuracy drop - model still functional but degraded |
| **10%** | **93.33%** | 📊 Slightly better than 5% due to random poisoning distribution |
| **50%** | **50.00%** | ❌ Complete model failure - equivalent to random guessing |

### 📈 Visual Representation

```
Accuracy (%)
100 ┤ ●
 95 ┤     ●
 90 ┤   ●
 85 ┤
 80 ┤
 75 ┤
 70 ┤
 65 ┤
 60 ┤
 55 ┤
 50 ┤         ●
    └────────────────
      0%  5% 10%  50%
         Poison Rate
```

> **📝 Note:** The 10% poison rate showing slightly higher accuracy than 5% is due to the random nature of which labels get flipped and how the train-test split occurs. This variability is expected in stochastic experiments.

---

## 💡 Key Insights

### 🎯 Data Quality > Data Quantity

This project proves that **quality trumps quantity** in machine learning:

1. **High-Quality Data**
   - 100 clean samples → Excellent model
   - Adding more clean data → Improved generalization
   - Predictable, reliable performance

2. **Low-Quality Data**
   - 10,000 samples with 50% noise → Useless model
   - Requires exponentially more data to compensate
   - Unpredictable behavior in production

### 🛡️ Mitigation Strategies

**1. Data Validation**
- Implement outlier detection (Z-scores, Isolation Forest)
- Check label consistency across similar features
- Statistical anomaly detection

**2. Data Provenance**
- Use trusted, verified data sources
- Track data lineage and contributions
- Implement authentication for user-generated content

**3. Robust Training**
- **Ensemble methods** (Bagging, Random Forests)
- **Data slicing validation** on known clean subsets
- **Cross-validation** to detect contamination

**4. Data-Centric AI Tools**
- Use tools like **Cleanlab** for automatic label error detection
- Implement continuous data quality monitoring
- Set up alerts for data drift

---

## 🎨 MLflow UI

View and compare all your experiments:

```bash
mlflow ui
```

Then open your browser to: **http://localhost:5000**

### What You'll See:
- 📊 Accuracy metrics for each poison rate
- 📉 Parameter comparisons (max_depth, poison_rate)
- 🤖 Logged models for each experiment
- ⏱️ Execution times and metadata

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

---

## 📚 Additional Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Data Poisoning Attacks Paper](https://arxiv.org/abs/1804.00792)
- [Cleanlab: ML with Noisy Labels](https://github.com/cleanlab/cleanlab)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Shridhar7-8**
- GitHub: [@Shridhar7-8](https://github.com/Shridhar7-8)
- Email: shridharkur@gmail.com

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a star!

Made with ❤️ for the MLOps community

</div>
