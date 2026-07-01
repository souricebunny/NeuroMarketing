🧠 NeuroAd Intelligence
### Multimodal AI Applied to Computational Advertising & Neuroscience-Inspired Analytics

> Predicting consumer neural engagement from FMCG advertisement videos and scripts — faster, cheaper, and smarter than traditional ad testing.

---

📌 Overview

**NeuroAd Intelligence** is an AI-powered neuromarketing tool that analyzes FMCG (Fast-Moving Consumer Goods) advertisements and predicts how the human brain responds to them — without a single EEG headset or fMRI scan.

By combining multimodal AI (vision + audio + language) with neuroscience-inspired scoring, the system identifies which moments in an ad trigger emotional responses, reward signals, and decision-making activity — giving creative teams actionable insights before a campaign goes live.

---

🎯 The Problem

Traditional ad testing is:
- **Expensive** — lab-based EEG/fMRI studies cost thousands per session
- **Slow** — results take weeks, not hours
- **Unscalable** — can only test a handful of participants

**We replace all of that with AI.**

---

💡 How It Works

```
Ad Video + Script
       ↓
Multimodal Feature Extraction
  ├── 🎥 Video frames → Emotion Detection (DeepFace)
  ├── 🔊 Audio → Tone Analysis (Whisper)
  └── 📝 Script → Semantic Understanding (CLIP + LLM)
       ↓
Neuroscience Scoring Engine
  ├── Valence    (positive ↔ negative emotional tone)
  ├── Arousal    (calm ↔ excited activation level)
  └── Cognitive Load (mental effort to process the ad)
       ↓
AI Insight Generator (Claude / GPT-4)
       ↓
📊 Streamlit Dashboard
```

---

🧬 Inspired By

This project is architecturally inspired by **Meta FAIR's TRIBE v2** (Trimodal Brain Encoder) — a foundation model trained on 500+ hours of fMRI recordings that predicts neural responses across 70,000 brain regions from video, audio, and text inputs.

We adapt the TRIBE v2 conceptual framework using open-source pre-trained encoders to build a computationally accessible neuromarketing tool.

- 📄 [TRIBE v2 Project Page](https://aidemos.atmeta.com/tribev2)
- 🤗 [TRIBE v2 on Hugging Face](https://huggingface.co/facebook/tribe-v2)

---

📦 Tech Stack

| Component | Tool |
|---|---|
| Emotion Detection | DeepFace, FER |
| Video Processing | OpenCV |
| Audio Analysis | Whisper (OpenAI) |
| Image-Text Understanding | CLIP |
| AI Insights | Claude API / GPT-4 |
| Dashboard | Streamlit |
| Data Handling | Pandas, NumPy |
| Deep Learning | PyTorch, HuggingFace Transformers |
| Experiment Environment | Google Colab (GPU) |

---

📊 Datasets

| Dataset | Purpose |
|---|---|
| [NeuMa Dataset](https://www.nature.com/articles/s41597-023-02392-9) | Primary — EEG + eye-tracking on FMCG grocery products |
| [NeuroBioSense](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10964042/) | Secondary — emotion signals from food & cosmetics ads |
| [Kaggle Video Ads](https://www.kaggle.com/datasets/karnikakapoor/video-ads-engagement-dataset) | Demo — video ads with engagement metrics |

---

🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/neuroadintelligence.git
cd neuroadintelligence
```

### 2. Install dependencies
```bash
pip install streamlit deepface opencv-python transformers torch openai pandas numpy whisper
```

### 3. Set your API key
```bash
export ANTHROPIC_API_KEY=your_key_here
# or
export OPENAI_API_KEY=your_key_here
```

### 4. Run the dashboard
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
neuroadintelligence/
│
├── app.py                  # Streamlit dashboard
├── pipeline/
│   ├── input_module.py     # Video + script preprocessing
│   ├── emotion_engine.py   # DeepFace emotion detection
│   ├── audio_analysis.py   # Whisper audio tone extraction
│   ├── scoring.py          # Valence-Arousal-CogLoad scorer
│   └── insight_generator.py# LLM-powered recommendations
│
├── data/
│   ├── sample_ads/         # Test advertisement inputs
│   └── datasets/           # NeuMa, NeuroBioSense (local)
│
├── notebooks/
│   └── tribe_v2_demo.ipynb # TRIBE v2 exploration on Colab
│
├── reports/                # Weekly progress reports (WPR1–8)
├── requirements.txt
└── README.md
```

---

📄 License

All third-party models and datasets are used in accordance with their respective licenses.

- TRIBE v2: CC-BY-NC 4.0 (Meta FAIR)
- DeepFace: MIT License
- NeuMa Dataset: Creative Commons

---

⭐ Topics

`neuromarketing` `multimodal-ai` `fmcg` `computational-advertising` `emotion-detection` `deepface` `streamlit` `consumer-neuroscience` `python` `tribe-v2`
