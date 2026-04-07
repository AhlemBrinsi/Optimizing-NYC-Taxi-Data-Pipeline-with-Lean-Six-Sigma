# 🚖 Optimizing NYC Taxi Data Pipeline with Lean Six Sigma

## 🧩 Project Overview

This project focuses on designing and optimizing a data preprocessing pipeline for the NYC Taxi dataset by combining:

- ETL (Extract, Transform, Load) workflow  
- Performance optimization techniques  
- Lean Six Sigma methodology (DMAIC + 5S)  

### 🎯 Objectives
- Reduce execution time  
- Improve data processing efficiency  
- Build a scalable and maintainable pipeline  

---

## 📊 Dataset

This project uses the NYC Taxi dataset.

Due to size limitations, the dataset is not included.  
You can download it using:

```bash
python src/extract.py
```

---

## ⚙️ ETL Pipeline Architecture

The pipeline follows a modular ETL design:

```
Extract → Transform (Before) → Transform (After) → Load
```

### 🔹 Extract
- Automatically downloads the dataset using the Kaggle API  
- Stores raw data in `data/raw/`

### 🔹 Transform (Before Optimization)
- Inefficient baseline pipeline  
- Contains:
  - Redundant operations  
  - Repeated transformations  
  - Loop-based computations  

### 🔹 Transform (After Optimization)
- Optimized pipeline using:
  - Vectorized operations (Pandas)  
  - Reduced redundancy  
  - Clean structure  

### 🔹 Load
- Saves processed data into `data/processed/`

---

## 🔍 Lean Six Sigma Approach (DMAIC)

### 🟢 Define
Identify inefficiencies in the preprocessing pipeline.

### 🟡 Measure
Benchmark execution time of the initial pipeline.

### 🔵 Analyze
Key issues detected:
- Duplicate transformations  
- Inefficient loops  
- Poor pipeline structure  

### 🟠 Improve
Implemented:
- Vectorization instead of loops  
- Removal of redundant computations  
- Code restructuring  

### 🔴 Control
- Standardized scripts  
- Ensured reproducibility  
- Documented workflow  

---

## 🧠 Lean 5S Application
- Sort → Removed unnecessary operations  
- Set in Order → Organized pipeline structure  
- Shine → Clean and readable code  
- Standardize → Modular ETL components  
- Sustain → Documentation and best practices  

---

## 📏 Performance Improvement

| Metric            | Before Optimization | After Optimization |
|------------------|--------------------|-------------------|
| Execution Time   | ~15.2 seconds      | ~8.7 seconds      |
| Improvement      | —                  | ~40% faster       |

---

## 📈 Results & Impact
- ⏱️ Reduced execution time by ~40%  
- 🔁 Eliminated redundant operations  
- 📊 Improved scalability and performance  
- 🧩 Built a reusable ETL pipeline  
- 🧠 Applied real-world industry methodology (Lean Six Sigma)  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Kaggle API  
- Jupyter Notebook  

---

## 📁 Project Structure

```
nyc-taxi-etl-optimization/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform_before.py
│   ├── transform_after.py
│   ├── load.py
│   └── pipeline.py
│
├── analysis.ipynb
├── results/
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run the Project

### Clone the repository:
```bash
git clone https://github.com/AhlemBrinsi/Optimizing-NYC-Taxi-Data-Pipeline-with-Lean-Six-Sigma.git
cd Optimizing-NYC-Taxi-Data-Pipeline-with-Lean-Six-Sigma
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Download dataset:
```bash
python src/extract.py
```

### Run the pipeline:
```bash
python src/pipeline.py
```

---

## 🎯 Resume Version

**Optimizing NYC Taxi Data Pipeline with Lean Six Sigma**

- Designed and implemented an ETL pipeline for large-scale taxi trip data  
- Applied DMAIC methodology to identify and resolve inefficiencies  
- Optimized preprocessing using vectorization and pipeline restructuring  
- Reduced execution time by ~40%  
- Applied Lean 5S principles to improve maintainability and scalability  

**Technologies:** Python, Pandas, NumPy  

---

## 🔮 Future Improvements
- Scale pipeline using PySpark  
- Orchestrate workflows with Apache Airflow  
- Add real-time data processing  
- Benchmark on full NYC dataset
