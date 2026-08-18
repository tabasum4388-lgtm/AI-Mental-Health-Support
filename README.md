# AI Mental Health Support for Students 🧠💬

An AI-powered **sentiment analysis + routing system** for students — it analyzes a student's message, detects their emotional state using AI, and automatically routes them to the right kind of support.

## 🔍 How It Works
1. **Input** — Student enters their name and a message describing how they feel
2. **Sentiment Analysis** — AI (Transformers/PyTorch) analyzes the message and detects sentiment + confidence score
3. **Keyword Detection** — Message is scanned for emotional keywords (sad, stressed, anxious, worried, etc.)
4. **Routing** — Based on sentiment + keywords, the system recommends:
   - **Social Support** — for loneliness/social distress
   - **Counselor Support** — for stress, anxiety, or worry
   - **General Support** — for everything else

## 🎯 Why This Project?
Students often face academic pressure and emotional stress but hesitate to seek help directly. This tool acts as a quiet first step — analyzing sentiment and routing students toward appropriate support before issues escalate.

## 🛠️ Tech Stack
- Python
- Transformers (Hugging Face)
- PyTorch

## 🚀 How to Run

1. Clone the repository:
git clone https://github.com/tabasum4388-lgtm/AI-Mental-Health-Support.git
cd AI-Mental-Health-Support
2. Install dependencies:
pip install transformers torch
3. Run the app:
python main.py
## 📌 Project Status
🚧 Work in progress — improving routing logic and sentiment accuracy.

## 👩‍💻 Author
**Tabasum**
