# Engineering Data Foundations
- Engineering data forms the backbone of any AI system used in industry.
- High-quality data leads to reliable AI predictions and decisions.
- This topic introduces data types, structures, preprocessing, and engineering data workflows.

# Why Engineers Must Understand Data
- Engineers are closest to the physical systems generating data.
- Deep understanding of data improves feature engineering and model reliability.
- Data quality determines AI performance more than model choice.

# What Engineering Data Looks Like
- Often time-series data from sensors measuring physical quantities.
- Can include images, logs, discrete states, or categorical labels.
- Data complexity varies across mechanical, electrical, civil, and manufacturing domains.

# Types of Engineering Data
- Time-series signals (vibration, temperature, current).
- Images (defects, corrosion, cracks).
- System logs (PLC events, alarms).
- Machine states and operational modes.

# Time-Series Sensor Data
- Sequential data recorded at regular or irregular intervals.
- Used for detecting trends, anomalies, and predicting failures.
- Common in mechanical, electrical, and process industries.

# Image Data in Engineering
- Captured via cameras or borescopes.
- Used for surface inspection, gauge reading, corrosion detection.
- Requires preprocessing to normalize lighting and orientation.

# Tabular Engineering Data
- Columns represent attributes such as pressure, temperature, or cycle count.
- Rows represent individual observations or time snapshots.
- Simple but extremely powerful for many ML models.

# Categorical and State Data
- Machines have states such as idle, running, fault, or maintenance.
- AI models use these states to understand system behavior.
- Helps correlate operating mode with performance or failures.

# Engineering Data Challenges
- Missing data from sensor dropout or communication failure.
- Noise due to hardware limitations or environmental conditions.
- Drift caused by aging sensors or structural changes.

# Impact of Poor Data Quality
- Leads to unreliable models and incorrect decisions.
- AI systems may misclassify faults or miss warning signs.
- Engineering judgement is required to validate data integrity.

# Understanding Sampling Frequency
- Sensors sample data at specific intervals (Hz).
- Higher frequency captures rapid events like vibrations.
- Lower frequency suitable for slow-changing variables like temperature.

# Nyquist Criterion for Engineers
- Sampling must be at least twice the highest frequency of interest.
- Undersampling leads to aliasing, hiding important fault frequencies.
- Critical for vibration and acoustic analysis.

# Aligning Data from Multiple Sensors
- Engineering systems often use multiple sensors with different timings.
- Data alignment ensures accurate feature extraction.
- Methods include interpolation, resampling, or time-window alignment.

# Normalizing Sensor Data
- Ensures all variables contribute fairly to model training.
- Prevents large-scale features from dominating.
- Methods include min-max scaling or standardization.

# Handling Missing Data
- Identify the cause: sensor dropout or benign gap.
- Options: interpolation, forward fill, backward fill.
- Engineers decide based on safety and domain requirements.

# Filtering and Noise Reduction
- Use low-pass, high-pass, or band-pass filters depending on the signal.
- Filtering enhances important patterns while removing irrelevant noise.
- Essential for vibration or acoustic signal processing.

# Fourier Transform for Engineers
- Converts time-domain signals into frequency-domain information.
- Reveals characteristic fault frequencies in rotating machinery.
- Forms the basis of many predictive maintenance features.

# Statistical Properties of Signals
- Mean, standard deviation, and variance describe signal stability.
- Kurtosis and skewness detect abnormalities or sharp transients.
- Useful for early-stage fault identification.

# Feature Engineering Basics
- Transform raw sensor data into meaningful numerical features.
- Includes statistics, FFT peaks, waveform descriptors.
- Strong features greatly improve model performance.

# Domain-Specific Feature Engineering Examples
- Mechanical: RMS vibration, harmonics, bearing frequencies.
- Electrical: THD (Total Harmonic Distortion), current unbalance.
- Civil: crack length, structural displacement, strain.

# Understanding Labels and Targets
- Labels are outputs the model tries to predict: fault status, load, temperature.
- High-quality labels are essential for supervised learning.
- Incomplete or incorrect labels reduce model accuracy.

# Dealing with Imbalanced Data
- Some engineering faults occur rarely.
- Models may learn to ignore minority classes.
- Solutions include resampling, synthetic data, or anomaly detection approaches.

# Engineering Metadata Importance
- Metadata includes asset ID, operating mode, environment, and load conditions.
- Provides context that improves feature engineering.
- Often necessary to interpret sensor data correctly.

# Data Storage in Engineering Systems
- Data may come from local SCADA, historians, PLC logs, or cloud storage.
- Engineers must understand the pipeline to obtain relevant data.
- Storage format affects speed and preprocessing needs.

# The Data Lifecycle in Engineering Projects
- Data collection → preprocessing → feature extraction → model training → deployment.
- Each stage must preserve data integrity.
- Poor early-stage decisions propagate downstream.

# Data Annotation for Engineering AI
- Labeling images or time-series segments may require expert input.
- Annotation tools help categorize states or defects.
- High-quality annotation increases trust and accuracy.

# Drift in Engineering Data
- Sensor drift: slow change in sensor behavior over time.
- Concept drift: relationship between inputs and outputs changes.
- Requires recalibration or model retraining.

# Data Visualization for Engineers
- Trend plots show long-term behavior.
- Spectrograms show changes over time in vibration signals.
- Scatter plots reveal correlations between variables.

# Outlier Detection Before Modeling
- Identifies unexpected data points due to rare events or sensor faults.
- Prevents misleading model training.
- Techniques include z-score, IQR, or simple engineering thresholds.

# Importance of Units and Scaling
- Mixed units can distort model training if not standardized.
- Engineering judgment required to convert or normalize values.
- Always verify sensor calibration and output units.

# Building a Data Dictionary
- Defines all variables, units, ranges, and descriptions.
- Essential for large engineering datasets.
- Helps maintain consistency across teams.

# Data Splitting for Model Training
- Train/validation/test splits ensure models generalize well.
- Engineers must ensure splits represent all operating modes.
- Avoid temporal leakage in time-series projects.

# Engineering Data Security
- Sensor data may include sensitive operational information.
- Secure handling ensures compliance with safety and regulatory standards.
- Encryption and access controls often required.

# Edge Data Considerations
- Edge devices have limited memory and processing.
- Data must be filtered or downsampled before inference.
- Ensures real-time performance and low latency.

# Data Quality Checklist for Engineers
- Are sensors calibrated?
- Are timestamps synchronized?
- Are there missing values or noise?
- Are units documented?
- Is the dataset representative of real operations?

# Summary of Topic 2
- Clean, reliable engineering data is vital for AI success.
- Engineers must understand data characteristics and preprocessing.
- Strong data foundations ensure robust AI models downstream.

# Q&A
- Discussion and clarifications about engineering data handling.
