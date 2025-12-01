# AI in Engineering — Complete Course Repository  
**Instructor:** Dr. Samuel Huang, Ph.D., P.Eng.  
**Organization:** TLNT Training (2026)  

![GitHub repo size](https://img.shields.io/github/repo-size/placeholder/ai-in-engineering)
![GitHub contributors](https://img.shields.io/github/contributors/placeholder/ai-in-engineering)
![GitHub last commit](https://img.shields.io/github/last-commit/placeholder/ai-in-engineering)
![License](https://img.shields.io/badge/license-MIT-green)

A complete professional training repository for the course  
**“Artificial Intelligence for Engineering Applications.”**  
Designed for mechanical, electrical, civil, manufacturing, HVAC, building automation, and power system engineers.

This repository includes **slides, labs, datasets, code templates, and capstone project materials**.

---

## 🧭 Table of Contents
- [Overview](#overview)  
- [Learning Outcomes](#learning-outcomes)  
- [Repository Structure](#repository-structure)  
- [Environment Setup](#environment-setup)  
- [How to Use This Repository](#how-to-use-this-repository)  
- [Topic Summaries (1–9)](#topic-summaries-1–9)  
- [Labs & Hands-On Work](#labs--hands-on-work)  
- [Datasets](#datasets)  
- [Capstone Project](#capstone-project)  
- [License](#license)  
- [Contact](#contact)  

---

## 🌐 Overview
This course teaches engineers how to use **Artificial Intelligence (AI)** to solve real-world industrial problems.

Focus areas include:

- Predictive Maintenance (PdM)
- Computer Vision (CV)
- Deep Learning (DL)
- Engineering Data Analysis
- PLC / SCADA / BMS Integration
- Edge AI and Industrial Deployment
- Robotics & Automation with AI
- Full end-to-end engineering AI projects

---

## 🎯 Learning Outcomes
After completing this course, learners will be able to:

- Process and analyze engineering sensor data  
- Build ML and DL models for real systems  
- Implement AI-based predictive maintenance  
- Deploy AI models to edge devices and cloud environments  
- Integrate AI with SCADA/PLC/BMS interfaces  
- Build full AI engineering workflows from data → deployment  
- Deliver industry-ready AI solutions supported by real datasets  

---

## 🗂 Repository Structure

```
ai-in-engineering/
│
├── README.md                       # This file
├── syllabus/                       # TLNT syllabus and course outline
│
├── slides/                         # Slides for 9 topics (TXT → PPTX)
│   ├── topic1/
│   ├── topic2/
│   ├── ...
│   └── topic9/
│
├── labs/                           # Jupyter notebooks for hands-on labs
│   ├── lab01_data_cleaning/
│   ├── lab02_fft_signal_analysis/
│   ├── lab03_regression/
│   ├── lab04_classification/
│   ├── lab05_predictive_maintenance/
│   ├── lab06_computer_vision/
│   ├── lab07_deployment_edge_cloud/
│   └── lab08_automation_integration/
│
├── datasets/                       # Engineering datasets (or download links)
│   ├── vibration/
│   ├── images/
│   ├── power/
│   └── structural/
│
├── code/                           # Reusable modules
│   ├── utils/
│   ├── preprocessing/
│   ├── models/
│   └── deployment/
│
└── assets/                         # Icons, diagrams, banners for slides
```

---

## ⚙ Environment Setup

### **Recommended: Conda**
```bash
conda create -n ai-eng python=3.10 -y
conda activate ai-eng
pip install -r requirements.txt
```

### **Or pip**
```bash
pip install -r requirements.txt
```

---

## ▶ How to Use This Repository

### **Slides**
Each topic folder contains a PowerPoint outline (`.txt`).  
Open directly in **PowerPoint → File → Open**  
PowerPoint auto-generates a full slide deck.

### **Labs**
Run the notebooks:

```bash
jupyter notebook
```

### **Code**
Reusable utilities for:

- Feature engineering  
- FFT + signal processing  
- ML/DL pipelines  
- CV preprocessing  
- Edge/cloud deployment  

---

## 🧩 Topic Summaries (1–9)

### **Topic 1 — Introduction to AI for Engineers**
AI fundamentals, engineering-specific applications, mechanical/electrical/civil examples.
- AI as a practical engineering tool, not an academic abstraction. Engineers learn how AI:
- Enhances reliability, safety, and operational efficiency
- Solves real-world problems (PdM, QC, optimization)
- Works with sensor data, image data, and system logs
- Complements physics-based engineering models
- Case studies:
- Manufacturing defect detection
- Mechanical bearing wear prediction
- Power system load forecasting
### **Topic 2 — Engineering Data Foundations**
Sensor data, filtering, FFT, feature extraction, alignment, cleaning.
- Covers data types, sensor behavior, cleaning, and preprocessing:
- Time-series (vibration, temperature, current)
- Images (defects, cracks, corrosion)
- SCADA/PLC logs
- Noise, missing data, drift
- FFT, filtering, statistical features
- Data normalization & alignment
- Engineers learn how data quality determines AI success.
### **Topic 3 — Machine Learning for Engineering**
Regression, classification, clustering, anomaly detection, metrics.
- Core ML techniques used across engineering industries:
- Regression (load prediction, temperature forecasting)
- Classification (fault/no-fault, pass/fail QC)
- Clustering (operational modes)
- Anomaly detection
- Models include:
- Linear/Logistic Regression
- Decision Trees / Random Forest / XGBoost
- SVM
- KNN
- Isolation Forest
- Also covers metrics, cross-validation, and error analysis.
### **Topic 4 — Predictive Maintenance (PdM)**
Vibration analysis, thermal analysis, ESA, RUL prediction, case studies.
- A full engineering treatment of PdM:
- Vibration, temperature, acoustic, and current-based monitoring
- Bearing/rotor defects, electrical faults, mechanical imbalance
- Time-series feature engineering
- Anomaly detection for early warnings
- Remaining Useful Life (RUL) estimation
- Case studies from pumps, conveyors, motors, and power transformers.
### **Topic 5 — Computer Vision**
CV workflows, CNNs, YOLO detection, segmentation, OCR, lighting/camera selection.
- Classical CV (thresholding, contours, edge detection)
- CNNs for image classification
- YOLO / Faster R-CNN for object detection
- U-Net for segmentation (cracks, corrosion, surface mapping)
- OCR for gauge reading & legacy system digitization
Also covers:
- Industrial lighting
- Camera selection
- Dataset labeling
### **Topic 6 — Deep Learning**
CNNs, 1D CNNs, LSTM/GRU, Autoencoders, transfer learning.
- Deep learning architectures:
- CNNs for images
- 1D CNNs for time-series
- LSTM / GRU for long-sequence modeling
- Autoencoders & VAEs for anomaly detection
- Transfer learning for small datasets
- Engineering applications:
- Vibration spectrogram analysis
- Electrical signature analysis
- Acoustic diagnostics
- Structural monitoring
### **Topic 7 — Deployment**
Cloud/edge deployments, Docker, ONNX, TensorRT, SCADA/PLC integration.
- Deployment environments:
- Cloud (AWS/Azure/GCP) for fleet-level monitoring
- Edge (Jetson, Raspberry Pi, industrial PCs) for low-latency
- Hybrid architectures
Covers:
- Docker
- ONNX Runtime
- TensorRT for high-speed inference
- REST APIs for predictions
- PLC / SCADA integration concepts
- Deployment constraints: Latency, reliability, cybersecurity, fail-safe design.
### **Topic 8 — System Integration & Automation**
AI in robotics, automated inspection, SCADA/BMS pipelines, event-driven systems.
- Engineering integration workflows:
- PLC, SCADA, BMS, DCS
- OPC UA / Modbus / MQTT / REST
- Robotics (vision-guided picking, automated inspection)
- Event-driven automation
- QA automation and real-time rejection systems
- Real examples:
- Packaging line defect removal
- Building energy automation
- Structural health alerting
### **Topic 9 — capstone Project**
Complete AI engineering solution with modeling + deployment + reporting.
- A complete end-to-end project:
- Data acquisition & preprocessing
- ML/DL modeling
- Deployment prototype (edge/cloud)
- Engineering dashboards
- Reliability, safety, and documentation
- Final presentation
- Example capstones:
- Pump bearing PdM system
- Power load forecasting model
- Surface defect detection Vision AI
- Structural anomaly detection (civil)
---

## 🧪 Labs & Hands-On Work

Included labs teach:

- Data cleaning & preprocessing  
- FFT and vibration analysis  
- Classical ML (regression, classification)  
- Deep learning (CNN, LSTM, Autoencoder)  
- Predictive maintenance modelling  
- Computer vision inspection  
- Edge device deployment  
- Integration with mock PLC/SCADA pipelines  

Labs include Jupyter notebooks and Python scripts.

---

## 📊 Datasets
This repository includes or references datasets for:

- **Vibration** (bearing, gearbox, motor faults)  
- **Thermal images** (electrical cabinet hotspots)  
- **Manufacturing defects**  
- **Power load forecasting**  
- **Structural monitoring** (strain, displacement, acceleration)  

Datasets may be:

- Included directly  
- Downloadable via script  
- Pointing to open-source sources  

---

## 🎓 Capstone Project

Learners build a complete engineering AI system.

### **Example Projects**
- Bearing PdM using vibration + LSTM  
- Surface defect detection (CNN + edge deployment)  
- Power load forecasting (regression models)  
- Structural anomaly detection (Autoencoder)  

### **Deliverables**
- Preprocessing + feature engineering  
- ML/DL models  
- Deployment demo (edge/cloud/REST API)  
- Dashboard or visualization  
- Engineering-style report  
- Presentation slides  

---

## 🧰 Software Tools
- Python 3.10+
- Jupyter Notebook
- pandas, numpy, matplotlib
- scikit-learn
- TensorFlow / PyTorch
- ONNX / TensorRT
- OpenCV
- Docker
- GitHub (version control)

---

## 🚀 What Students Will Be Able to Do

- Upon completion, participants will be able to:
- Analyze raw engineering datasets and extract meaningful features
- Build accurate ML/DL models tailored to engineering systems
- Develop computer vision inspection applications
- Implement vibration- and current-based PdM models
- Deploy models on real engineering hardware
- Integrate AI systems with automation/SCADA/PLC
- Deliver a professional-grade AI engineering project

---

## 🏁 Final Note

This course is designed for professional engineers, technical specialists, and engineering managers who want to adopt AI technologies responsibly, effectively, and safely in real industrial environments.

AI is not here to replace engineering expertise— AI amplifies engineering capability. AI + Engineering = Smarter, safer, more efficient systems.

---

## 📄 License
This project is covered under the **MIT License**.  
Modify as required for your institution or training provider.

---

## 📬 Contact
**Samuel Huang, Ph.D., P.Eng.**  
Email: ch9398@gmail.com  
Toronto, Canada

---

##🏁 Final Note

This course is designed for professional engineers, technical specialists, and engineering managers who want to adopt AI technologies responsibly, effectively, and safely in real industrial environments.

AI is not here to replace engineering expertise— AI amplifies engineering capability. AI + Engineering = Smarter, safer, more efficient systems. 🌟 Acknowledgments
This repository design follows modern engineering/AI course structures and has been enhanced with documentation best practices for professional GitHub repositories.
