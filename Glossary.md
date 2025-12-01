# Glossary of Engineering AI and Industrial Automation Terms

This glossary provides clear, engineering-focused definitions for all acronyms used throughout the course **AI in Engineering**.

---

## 🚦 Industrial & Automation Systems

### **PLC — Programmable Logic Controller**
A rugged industrial computer used for **real-time control** of machinery, robots, pumps, PLC-based assembly lines, HVAC controllers, and manufacturing equipment.  
Engineered for harsh environments, extremely reliable, and used in almost all industrial automation.

---

### **SCADA — Supervisory Control And Data Acquisition**
A high-level system used to **monitor**, **visualize**, and **manage** large industrial networks.  
Functions include:  
- Real-time sensor monitoring  
- Equipment status dashboards  
- Alarm management  
- Historical trend logging  
- Control of PLCs and remote devices  

Used in power plants, water treatment, oil & gas, and large factories.

---

### **BMS — Building Management System**  
(Also called **BAS — Building Automation System**)  
The automation system responsible for building-wide control of:  
- HVAC  
- Lighting  
- Energy usage optimization  
- Security & access control  
- Elevators and fire systems  

AI integrates with BMS to optimize energy efficiency and occupant comfort.

---

## ⚡ Engineering Predictive Maintenance & Diagnostics

### **ESA — Electrical Signature Analysis**
A method to analyze **voltage** and **current waveforms** to detect faults in:  
- Induction motors  
- Pumps  
- Compressors  
- Gearboxes  
- Rotating equipment  

Identifies rotor bar faults, bearing issues, air-gap problems, unbalanced loads, and misalignment—without additional sensors.

---

### **RUL — Remaining Useful Life**
The estimated **operational time left** before a machine or component fails.  
A key KPI in predictive maintenance, based on:  
- Statistical models  
- Regression ML models  
- Deep learning time-series models (LSTM/GRU)  

Used to schedule maintenance and reduce downtime.

---

## 🤖 AI, ML & Deep Learning

### **YOLO — You Only Look Once**
A fast, real-time **object detection** algorithm widely used for:  
- Manufacturing QC  
- Defect detection  
- Robotics and pick-and-place  
- Safety monitoring  
- Surface inspection  

Ideal for edge devices like NVIDIA Jetson.

---

### **GRU — Gated Recurrent Unit**
A lightweight deep learning architecture for **time-series** and **sequential data**, similar to LSTM but faster.  
Used in:  
- Vibration analysis  
- Structural monitoring  
- Power load forecasting  
- PdM anomaly detection  

---

### **ONNX — Open Neural Network Exchange**
An open format that allows models trained in one framework to be run in another.  
Supports:  
- PyTorch  
- TensorFlow  
- Keras  
- scikit-learn  
- C++ deployment  
- ONNX Runtime  
- TensorRT for acceleration  

Crucial for flexible, production-ready model deployment.

---

### **TensorRT — Tensor Real-Time**
NVIDIA’s high-performance deep learning inference optimization engine.  
Optimizes and accelerates models for:  
- GPUs  
- Edge devices (Jetson)  
- Real-time industrial systems  

**RT = Real-Time**, reflecting its deployment focus.

---

## 🧠 Common AI & Signal Processing Terms

### **CNN — Convolutional Neural Network**
Used for image analysis tasks: classification, defect detection, segmentation.

### **LSTM — Long Short-Term Memory**
Deep learning architecture designed for long time dependencies in sensor data.

### **FFT — Fast Fourier Transform**
Transforms time-domain signals into frequency domain.  
Used for vibration analysis and rotating equipment diagnostics.

### **API — Application Programming Interface**
Standard method for other systems to call your model (REST API, JSON output).

### **MQTT — Message Queuing Telemetry Transport**
Lightweight IoT/IIoT pub-sub protocol used for cloud/edge integration.

---

# 📄 End of Glossary
Save this file as **GLOSSARY.md** in your repository for easy student and instructor reference.

