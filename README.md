# Amdox AI-Powered Task Optimizer 🚀

## Project Overview
During my internship at **Amdox**, I developed the AI-Powered Task Optimizer—a multi-modal Data Science solution designed to bridge the gap between employee mental well-being and operational productivity. 

In a modern workplace, "one size fits all" task management is outdated. This system uses Computer Vision and NLP to sense an employee's current emotional state and suggests the right kind of work for that moment, ensuring high efficiency without the risk of burnout.

## 🛠 Features (The 6-Point Implementation)

### 1. Real-Time Multi-Modal Detection
Unlike single-source models, this system analyzes **facial expressions** via OpenCV/DeepFace and **text sentiment** via HuggingFace Transformers. This ensures a comprehensive understanding of mood.

### 2. Intelligent Task Mapping
The "Task Engine" maps 7 core emotions to specific work types. 
* *Example:* If 'High Stress' or 'Anger' is detected, the system suggests solo research tasks rather than high-pressure client meetings.

### 3. Historical Well-being Timeline
The system logs anonymized mood data into a CSV-based tracking system, allowing HR to see long-term trends rather than reacting to isolated bad days.

### 4. Automated Stress Alerts
I implemented a "Continuous Stress Threshold" logic. If negative emotions persist for a specific duration, the system flags a potential burnout risk, alerting HR (support@amdox.in) for proactive intervention.

### 5. Team Morale Analytics
Aggregated data provides managers with a "Team Pulse" dashboard, showing the overall health of the department without compromising individual privacy.

### 6. Privacy-First Architecture
Security was a top priority. Raw video and audio never leave the local machine. The system only stores anonymized emotion labels (e.g., `2026-02-12, neutral`), ensuring full compliance with data privacy standards.
