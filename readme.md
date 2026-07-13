# NEUROMARKETING

### Multimodal AI Applied to Computational Advertising & Neuroscience-Inspired Analytics

> Predicting consumer neural engagement from FMCG advertisement videos — faster, cheaper, and smarter than traditional ad testing.

---

## 📌 Overview

**NeuroAd Intelligence** is an AI-powered neuromarketing tool that analyzes FMCG (Fast-Moving Consumer Goods) advertisements and predicts how the human brain responds to them — without a single EEG headset or fMRI scan.

By combining multimodal AI (facial expression + neural video encoding) with neuroscience-inspired scoring, the system identifies which moments in an ad trigger emotional responses and engagement — giving creative teams actionable insights before a campaign goes live.

---

## 🎯 The Problem

Traditional ad testing is:

- **Expensive** — lab-based EEG/fMRI studies cost thousands per session
- **Slow** — results take weeks, not hours
- **Unscalable** — can only test a handful of participants

**We replace all of that with AI.**

---

## 💡 How It Works

```
Ad Video
   ↓
Multimodal Feature Extraction
  ├── 🎥 Video frames → Facial Expression Recognition (DeepFace, local)
  └── 🧠 Full video   → Neural Activation Encoding (Custom TRIBE v2, Colab T4 GPU)
   ↓
Valence-Arousal Scoring Engine
  ├── DeepFace weight   (60%)
  ├── TRIBE v2 weight   (40%)
  ├── Valence
  ├── Arousal
  └── Engagement Index
   ↓
📊 Streamlit Dashboard
```

> 🎧 **Audio analysis (Whisper)** is included in the repo as a bonus/exploratory module — it is **not** part of the core scoring pipeline currently used for analysis.

---

## 🧬 Inspired By

This project is architecturally inspired by **Meta FAIR's TRIBE v2** (Trimodal Brain Encoder) — a foundation model trained on 500+ hours of fMRI recordings that predicts neural responses across 70,000 brain regions from video, audio, and text inputs.

Rather than using the original framework as-is, we've **modified and adapted TRIBE v2's architecture** to fit our neuromarketing use case, running a customized version (not Meta's stock implementation) on Colab with a T4 GPU, alongside DeepFace for facial emotion recognition run locally.

- 📄 [TRIBE v2 Project Page](https://aidemos.atmeta.com/tribev2)
- 🤗 [TRIBE v2 on Hugging Face](https://huggingface.co/facebook/tribe-v2)

---

## 📦 Tech Stack

| Component                | Tool                                      |
| ------------------------ | ------------------------------------------ |
| Facial Expression Recognition | DeepFace (local, Apple Silicon)       |
| Neural Video Encoding     | Custom-modified TRIBE v2 (Colab, T4 GPU)  |
| Video Processing         | OpenCV                                     |
| Audio Analysis (bonus)   | Whisper (OpenAI) — exploratory, not core   |
| AI Insights              | Claude API                                 |
| Dashboard                | Streamlit                                  |
| Data Handling            | Pandas, NumPy                              |
| Deep Learning            | PyTorch                                    |
| Experiment Environment   | Google Colab (T4 GPU)                      |

---

## 📊 Datasets

| Dataset                                                                                        | Purpose                                               |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| [NeuMa Dataset](https://www.nature.com/articles/s41597-023-02392-9)                            | Primary — EEG + eye-tracking on FMCG grocery products |
| [NeuroBioSense](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10964042/)                        | Secondary — emotion signals from food & cosmetics ads |
| [Kaggle Video Ads](https://www.kaggle.com/datasets/karnikakapoor/video-ads-engagement-dataset) | Demo — video ads with engagement metrics              |

---

## 🚀 Getting Started

### 1. Clone the repo

```
git clone https://github.com/souricebunny/NeuroMarketing.git
cd NeuroMarketing
```

### 2. Install dependencies

```
pip install streamlit deepface opencv-python torch pandas numpy
```

> Whisper is optional and only required if you want to explore the bonus audio module.

### 3. Set your API key

Add your Anthropic API key to `.streamlit/secrets.toml`:

```
ANTHROPIC_API_KEY = "your_key_here"
```

### 4. Run the dashboard

```
streamlit run app.py
```

---

## 📁 Project Structure

```
NeuroMarketing/
│
├── app.py                  # Streamlit dashboard
├── pipeline/
│   ├── input_module.py     # Video preprocessing (10s trim)
│   ├── emotion_engine.py   # DeepFace facial expression recognition (local)
│   ├── tribe_engine.py     # Custom-modified TRIBE v2 (Colab, T4 GPU)
│   ├── scoring.py          # Valence-Arousal-Engagement fusion (60/40)
│   ├── audio_analysis.py   # Whisper — bonus/exploratory, not core pipeline
│   └── insight_generator.py# LLM-powered recommendations
│
├── data/
│   ├── sample_ads/         # Test advertisement inputs
│   └── datasets/           # NeuMa, NeuroBioSense (local)
│
├── notebooks/
│   └── tribe_v2_custom.ipynb # Custom TRIBE v2 exploration on Colab
│
├── reports/                # Weekly progress reports (WPR1–8)
├── requirements.txt
└── README.md
```

---

## 📄 License

All third-party models and datasets are used in accordance with their respective licenses.

- TRIBE v2 (modified): CC-BY-NC 4.0 (Meta FAIR, original base)
- DeepFace: MIT License
- NeuMa Dataset: Creative Commons

---

## ⭐ Topics

`neuromarketing` `multimodal-ai` `fmcg` `computational-advertising` `emotion-detection` `deepface` `streamlit` `consumer-neuroscience` `python` `tribe-v2`
