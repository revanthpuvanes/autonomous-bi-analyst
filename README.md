# 🧠 Autonomous BI Analyst (Powered by Mistral AI)

An AI-powered multi-agent data analysis system that answers business questions from raw datasets, just like a real data team.

---

## 🚀 Overview

Business users often ask:

- Why did sales drop?
- Which segment is underperforming?
- What caused churn to increase?

Traditional tools require SQL or dashboards.

👉 This project solves that by using **AI agents that analyze, verify, and explain insights automatically**.

---

## ⚙️ How It Works

The system follows a **multi-agent workflow**:

1. **Planner Agent**
   - Breaks the question into analysis steps

2. **Analyst Agent**
   - Generates Pandas code using LLM
   - Executes it on the dataset

3. **Visualizer Agent**
   - Creates charts (sales trends, region comparison)

4. **Reporter Agent**
   - Produces business insights from analysis

5. **Verifier Agent (Key Feature 🔥)**
   - Checks if the report is supported by data
   - Detects hallucinations
   - Assigns confidence score

---

## 🧠 Example

**Question:**
- 📊 Which month has the highest sales?
  
**Output:**
- 📊 Analysis Result: July
- 📝 Report: July has the highest sales
- 🛡️ Confidence: High
- 📈 Charts: Sales trends over time

---

## 🏗️ Project Structure
  ```
  autonomous-bi-analyst/
  │
  ├── app/
  │ ├── main.py # CLI pipeline
  │ └── streamlit_app.py # Web UI
  │
  ├── agents/
  │ ├── planner.py
  │ ├── analyst.py
  │ ├── reporter.py
  │ ├── verifier.py
  │ └── visualizer.py
  │
  ├── utils/
  │ ├── mistral_client.py
  │ ├── data_loader.py
  │ └── code_runner.py
  │
  ├── data/ # Sample datasets
  ├── outputs/ # Logs + charts
  ├── .env # API key (not committed)
  ├── requirements.txt
  └── README.md
  ```

---

## 🧰 Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit
- Mistral AI (LLM)

---

## ▶️ Run Locally

### 1. Clone repo

---

## 🧰 Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit
- Mistral AI (LLM)

---

## ▶️ Run Locally

### 1. Clone repo
git clone https://github.com/revanthpuvanes/autonomous-bi-analyst.git
cd autonomous-bi-analyst

### 2. Setup environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 3. Add API key
Create `.env` file:
MISTRAL_API_KEY=your_api_key_here

---

## 🖥️ Run CLI version
python -m app.main

---

## 🌐 Run Streamlit App
streamlit run app/streamlit_app.py

---

## 📊 Features

- ✅ Multi-agent architecture
- ✅ Automatic code generation & execution
- ✅ Data-driven insights (no hallucinations)
- ✅ Built-in verification layer 🔥
- ✅ Chart generation
- ✅ Streamlit UI for interaction

---

## 🌟 What Makes It Unique

- Focuses on **"why" analysis**, not just querying
- Includes a **Verifier Agent** to reduce hallucinations
- Produces **auditable outputs (code + data + report)**
- Mimics real-world data science workflows

---

## 📸 Screenshots

> <img width="1266" height="462" alt="Screenshot from 2026-03-25 23-27-41" src="https://github.com/user-attachments/assets/368d7112-da96-4fe8-8eaf-d411816d68da" />
> <img width="1251" height="583" alt="Screenshot from 2026-03-25 23-28-04" src="https://github.com/user-attachments/assets/6298ec10-0b57-41ad-9e46-e5cdc885a704" />

---

## 🚀 Future Improvements

- Structured JSON outputs (reduce errors)
- Advanced visualizations (Plotly)
- Multi-dataset support
- Memory for follow-up questions
- Deployment on Hugging Face Spaces



## 🤝 Contributing

Feel free to fork and improve!

---

## 📬 Contact

Built by Revanth 🚀
