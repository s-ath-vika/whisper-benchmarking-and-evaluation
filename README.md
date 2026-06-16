# AI Interviewer - Whisper Speech Recognition Benchmarking

This repository contains the local deployment, data profiling, and evaluation matrix pipeline built to benchmark OpenAI's Whisper Speech-to-Text engine for the speech processing layer of the AI-Based Interview System.

---

## 🚀 Key Features

* **Multi-Model Evaluation Matrix:** Dynamically loads and evaluates Whisper `tiny`, `base`, and `small` models locally.
* **7-Scenario Stress Testing:** Profiles speech recognition performance across seven real-world conditions, including ambient noise, regional accents, rapid speech, and technical jargon.
* **Linguistic Telemetry Integration:** Uses the `jiwer` library to automatically calculate Word Error Rate (WER) against predefined ground-truth transcripts.
* **Target Schema Enforcement:** Maps transcription outputs into a structured JSON format containing recognized text and processing metrics.

---

## 📊 Performance Benchmarks (Verified CPU Data)

### Highest Accuracy Baseline

**Whisper Small**

* Achieved **0.00% WER** on regional accent recordings.
* Delivered highly accurate transcription of technical vocabulary.
* Demonstrated the best overall recognition performance among tested models.

### Most Efficient Resource Footprint

**Whisper Base**

* Consistently processed short audio files in under 5 seconds.
* Balanced speed and transcription quality effectively.
* Suitable for deployment on CPU-only server environments.

---

## 📦 Project Directory Layout

```text
whisper-benchmarking-and-evaluation/
│
├── benchmark.py
├── README.md
└── audio_samples/
   ├── clean_baseline.mp3
   ├── background_noise.mp3
   ├── regional_accent.mp3
   ├── long_recording.mp3
   ├── custom_tech_jargon.mp3  
   ├── small_recording.mp3  
   └── speed_mumble.mp3 
```

### File Descriptions

| File/Folder        | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| `benchmark.py`     | Main benchmarking and evaluation script         |
| `audio_samples/`   | Contains the seven stress-test audio recordings |
| `README.md`        | Project documentation                           |

---

## 🔧 Installation & Setup

### 1. Install FFmpeg

Whisper requires FFmpeg for audio processing.

Verify installation:

```bash
ffmpeg -version
```

### 2. Install Required Python Packages

```bash
pip install openai-whisper torch jiwer
```

---

## ▶️ Running the Benchmark

Execute the benchmarking pipeline:

```bash
python benchmark.py
```

The script will:

1. Load Whisper models (`tiny`, `base`, `small`)
2. Process all stress-test audio files
3. Generate transcriptions
4. Compute Word Error Rate (WER)
5. Measure processing time
6. Output evaluation metrics in the required schema

---

## 📈 Evaluation Metrics

The benchmarking framework measures:

* Transcription Accuracy
* Word Error Rate (WER)
* Processing Time
* Model Performance Comparison
* Noise Robustness
* Accent Recognition Capability
* Technical Vocabulary Recognition

---
## 📄 Sample Benchmark Logs

Click below to expand the complete benchmark execution logs.

<details>
<summary><strong>View Full Benchmark Execution Logs</strong></summary>

```text
🚀 STARTING WHISPER PERFORMANCE BENCHMARKING ENGINE
======================================================================

⚙️ LOADING MODEL TIER: [TINY]...
C:\Users\91955\AppData\Roaming\Python\Python314\site-packages\whisper\transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
 📂 Test Scenario: 1_clean_baseline
    ⏱️ Processing Time: 2.74s
    📉 Word Error Rate: 50.00%
{
    "transcript": "I am a back end developer, a design scalable API micro services using the fast API framework and Python.",
    "processing_time": 2.74
}
--------------------------------------------------
 📂 Test Scenario: 2_background_noise
    ⏱️ Processing Time: 1.63s
    📉 Word Error Rate: 13.33%
{
    "transcript": "In my previous workspace, I configured post-press here databases inside Docker container volumes for data persistence.",
    "processing_time": 1.63
}
--------------------------------------------------
 📂 Test Scenario: 3_regional_accent
    ⏱️ Processing Time: 1.51s
    📉 Word Error Rate: 6.25%
{
    "transcript": "We need optimize the network throughput by managing intermediate web proxy and disabling buffering lines.",
    "processing_time": 1.51
}
--------------------------------------------------
 📂 Test Scenario: 4_technical_jargon
    ⏱️ Processing Time: 1.89s
    📉 Word Error Rate: 57.14%
{
    "transcript": "Our automated monitoring pipeline relies on Yolo V8 for deep learning of Jet Detection, Media Pipes for Face Landmarks and the Fast API Backend.",
    "processing_time": 1.89
}
--------------------------------------------------
 📂 Test Scenario: 5_speed_mumble
    ⏱️ Processing Time: 1.7s
    📉 Word Error Rate: 35.29%
{
    "transcript": "Then a client suddenly terminates their browser tap session. It's significantly as the server task memory instantly.",
    "processing_time": 1.7
}
--------------------------------------------------
 📂 Test Scenario: 6_long_payload
    ⏱️ Processing Time: 4.24s
    📉 Word Error Rate: 22.22%
{
    "transcript": "The primary objective of this architecture is to provide an automated fair and reliable interview environment, a combining multiple mission learning models, instead of looking at a single rule, other platform processes, continuous video streams, audio data, and context shared language outputs simultaneously. A video system extracts features like multiple synthetics and mobile phone usage using convolutional neural network while acoustic engine evaluates ambient sound cues. This multi-modal strategy ensures maximum security against candidate, cheating and minimizes false rate warnings drastically.",
    "processing_time": 4.24
}
--------------------------------------------------
 📂 Test Scenario: 7_small_payload
    ⏱️ Processing Time: 1.1s
    📉 Word Error Rate: 28.57%
{
    "transcript": "I have worked with Python and Fast API",
    "processing_time": 1.1
}
--------------------------------------------------

⚙️ LOADING MODEL TIER: [BASE]...
 📂 Test Scenario: 1_clean_baseline
    ⏱️ Processing Time: 3.29s
    📉 Word Error Rate: 43.75%
{
    "transcript": "I am a backend developer, a design scalable API micro services using the first API Framework and Python.",
    "processing_time": 3.29
}
--------------------------------------------------
 📂 Test Scenario: 2_background_noise
    ⏱️ Processing Time: 4.8s
    📉 Word Error Rate: 26.67%
{
    "transcript": "In my previous workspace, I configured post-press SQL databases inside Docker Container and volumes for data persistence.",
    "processing_time": 4.8
}
--------------------------------------------------
 📂 Test Scenario: 3_regional_accent
    ⏱️ Processing Time: 4.26s
    📉 Word Error Rate: 0.00%
{
    "transcript": "We need to optimize the network throughput by managing intermediate web proxy and disabling buffering lines.",
    "processing_time": 4.26
}
--------------------------------------------------
 📂 Test Scenario: 4_technical_jargon
    ⏱️ Processing Time: 3.15s
    📉 Word Error Rate: 23.81%
{
    "transcript": "Our automated monitoring pipeline relies on YOLO V8 for deep learning object detection, media pipe for face landmarks and the fast API backend.",
    "processing_time": 3.15
}
--------------------------------------------------
 📂 Test Scenario: 5_speed_mumble
    ⏱️ Processing Time: 2.82s
    📉 Word Error Rate: 5.88%
{
    "transcript": "When a client suddenly terminates their browser tap session, a signal clears the server task memory instantly.",
    "processing_time": 2.82
}
--------------------------------------------------
 📂 Test Scenario: 6_long_payload
    ⏱️ Processing Time: 7.94s
    📉 Word Error Rate: 25.93%
{
    "transcript": "The primary objective of this architecture is to provide an automated, fair, unreliable interview environment, a commanding multiple mission-learning models, instead of looking at a single tool, our platform processes continuous video streams, audio data and contextual language outputs simultaneously. The video system extracts features like multi-person detection, mobile phone usage, using a convolutional neural network, while a acoustic engine evaluates ambient sound cues. This multimodal strategy ensures maximum security against candidate, cheating, and minimizes false rate warnings drastically.",
    "processing_time": 7.94
}
--------------------------------------------------
 📂 Test Scenario: 7_small_payload
    ⏱️ Processing Time: 2.5s
    📉 Word Error Rate: 28.57%
{
    "transcript": "I have worked with Python and Fast API.",
    "processing_time": 2.5
}
--------------------------------------------------

⚙️ LOADING MODEL TIER: [SMALL]...
 📂 Test Scenario: 1_clean_baseline
    ⏱️ Processing Time: 10.75s
    📉 Word Error Rate: 12.50%
{
    "transcript": "I am a backend developer. I design scalable API microservices using the fast API framework and Python.",
    "processing_time": 10.75
}
--------------------------------------------------
 📂 Test Scenario: 2_background_noise
    ⏱️ Processing Time: 9.61s
    📉 Word Error Rate: 13.33%
{
    "transcript": "In my previous workspace, I configured Postgres SQL databases inside Docker container volumes for data persistence.",
    "processing_time": 9.61
}
--------------------------------------------------
 📂 Test Scenario: 3_regional_accent
    ⏱️ Processing Time: 9.56s
    📉 Word Error Rate: 0.00%
{
    "transcript": "We need to optimize the network throughput by managing intermediate web proxy and disabling buffering lines.",
    "processing_time": 9.56
}
--------------------------------------------------
 📂 Test Scenario: 4_technical_jargon
    ⏱️ Processing Time: 10.47s
    📉 Word Error Rate: 19.05%
{
    "transcript": "Our automated monitoring pipeline relies on YOLO v8 for deep learning object detection, media pipe for face landmarks and the fast API backend.",
    "processing_time": 10.47
}
--------------------------------------------------
 📂 Test Scenario: 5_speed_mumble
    ⏱️ Processing Time: 9.32s
    📉 Word Error Rate: 5.88%
{
    "transcript": "When a client suddenly terminates their browser tab session, it signal clears the server task memory instantly.",
    "processing_time": 9.32
}
--------------------------------------------------
 📂 Test Scenario: 6_long_payload
    ⏱️ Processing Time: 23.99s
    📉 Word Error Rate: 17.28%
{
    "transcript": "The primary objective of this architecture is to provide an automated, fair, unreliable interview environment, like a mining multiple machine learning model. Instead of looking at a single rule, our platform processes continuous video streams, audio data, and contextual language outputs simultaneously. The video system extracts features like multi-person detection, mobile phone usage, using convolutional neural network, while acoustic engine evaluates ambient sound cues. This multimodal strategy ensures maximum security against candidate cheating and minimizes false rate warnings drastically.",
    "processing_time": 23.99
}
--------------------------------------------------
 📂 Test Scenario: 7_small_payload
    ⏱️ Processing Time: 10.94s
    📉 Word Error Rate: 28.57%
{
    "transcript": "I have worked with Python and Fast API.",
    "processing_time": 10.94
}
--------------------------------------------------

🏆 Benchmarking Execution Complete. Log details captured.
```

</details>
---

### 📈 Speech Recognition Benchmarking & Evaluation Matrix

To determine the optimal operational deployment profile, a comprehensive performance evaluation was executed across all three local model tiers using seven distinct verbal stress-test conditions:

| Evaluation Scenario | Whisper Tiny (Speed / WER) | Whisper Base (Speed / WER) | Whisper Small (Speed / WER) |
| :--- | :---: | :---: | :---: |
| **1. Clean Baseline** | 2.74s / 50.00% | 3.29s / 43.75% | **10.75s / 12.50%** |
| **2. Background Noise** | 1.63s / 13.33% | 4.80s / 26.67% | **9.61s / 13.33%** |
| **3. Regional Accent** | 1.51s / 6.25% | **4.26s / 0.00%** | **9.56s / 0.00%** |
| **4. Technical Jargon** | 1.89s / 57.14% | 3.15s / 23.81% | **10.47s / 19.05%** |
| **5. Speed Mumble** | 1.70s / 35.29% | **2.82s / 5.88%** | **9.32s / 5.88%** |
| **6. Long Payload** | 4.24s / 22.22% | 7.94s / 25.93% | **23.99s / 17.28%** |
| **7. Small Payload** | 1.10s / 28.57% | 2.50s / 28.57% | **10.94s / 28.57%** |

*Note: Bold values denote high-performance milestones, showcasing Whisper Small's superior linguistic stability (such as achieving 0.00% Word Error Rate under regional pronunciation challenges) alongside Whisper Base's competitive sub-5-second runtime balance.*

---

## 🛠️ Technologies Used

* Python
* OpenAI Whisper
* PyTorch
* JiWER
* FFmpeg

---

## 🎯 Project Objective

The goal of this project is to identify the most suitable Whisper model for integration into an AI-powered interview platform by comparing transcription quality, execution speed, and resource consumption under realistic speech conditions.

---

## 📝 Notes

This project was developed for academic and research purposes as part of the AI-Based Interview System speech processing evaluation workflow.
