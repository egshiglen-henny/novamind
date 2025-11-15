# 🤖 NovaMind – AI Brainstorm Assistant

![Build Status](https://github.com/egshiglen-henny/novamind/actions/workflows/python-app.yml/badge.svg)
![Coverage](https://github.com/egshiglen-henny/novamind/raw/main/coverage.svg)
![Python Versions](https://img.shields.io/badge/Python-3.12%20%7C%203.13-blue)
![Framework](https://img.shields.io/badge/Framework-OpenAI%20API-green)
![Testing](https://img.shields.io/badge/Testing-Pytest%20%7C%20Pytest--Cov-purple)
![Prompt Engineering](https://img.shields.io/badge/AI%20Type-Prompt%20Engineering-orange)
![Tests](https://img.shields.io/badge/Tests-100%25%20Passing-blue)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)




NovaMind is a **Python-based AI brainstorming assistant** that uses **prompt engineering** and **NLP techniques** to generate diverse, relevant, and realistic project ideas tailored to the user’s interests and goals.

Built as part of my **Software Engineering & AI Practice**, this project demonstrates skills in **OpenAI API integration**, **natural language processing**, **input validation**, and **automated testing**.

---

## ✨ Features

* 🎯 **Prompt Engineering:** Structured AI prompts with creativity control (`temperature=0.7`)
* 🧠 **NLP-Powered Suggestions:** Generates 3 unique, feasible project ideas per session
* 🧩 **Input Validation:** Regex and heuristic rules to block gibberish, symbols, and invalid text
* ⚙️ **Performance Measurement:** Tracks response time per brainstorm request
* ✅ **Automated Testing:** Comprehensive unit tests with `pytest` and coverage metrics
* 💬 **Error Handling:** Graceful recovery from API or network issues
* 🧪 **End-to-End Testing:** Validates full user workflow with mocked OpenAI API
* ⚙️ **Unified Pipeline:** The `run_pipeline()` function orchestrates validation and AI generation for complete workflow automation.


---

## 🧩 Tech Stack

| Tool                         | Purpose                      |
| ---------------------------- | ---------------------------- |
| **Python 3.12/3.13**       | Core language                |
| **OpenAI API (GPT-4o-mini)** | AI text generation           |
| **Regex**                    | Input pattern validation     |
| **Pytest / Pytest-Cov**      | Automated testing & coverage |
| **Pylance / VS Code**        | Development environment      |

---

## 1. Project Overview

* **Type:** AI & NLP Brainstorming Assistant
* **Framework:** OpenAI API
* **Language:** Python 3.13
* **Main Features:**

  * Input validation (`validate_input()`)
  * AI brainstorming (`brainstorm()`)
  * Real-time idea generation with response timing
  * Structured prompt formatting
  * Unified pipeline (`run_pipeline`)
  * Full unit + E2E tests

---

## 2. Example Output
<details> <summary> 📌Click to view example output</summary>
**Input:**

```
What are your interests? 3D design
What is your goal? build a project
```

**NovaMind’s Output:**

```
Idea 1: 3D Art Gallery
Summary: Transform virtual spaces into immersive art experiences.
Description: Create an interactive online gallery showcasing 3D artworks, allowing users to navigate and explore different artistic styles and concepts from various creators.

Idea 2: Virtual Sculptor
Summary: Empower creativity through intuitive 3D modeling tools.
Description: Develop a user-friendly application that lets users design and sculpt 3D models using augmented reality, fostering creativity and accessibility in digital art creation.

Idea 3: 3D Puzzle Adventure
Summary: Engage players in a captivating world of spatial challenges.
Description: Design a 3D puzzle game where players manipulate the environment to solve challenges, combining art, design, and gameplay to create a unique interactive experience.
```
</details>

---

## 3. Local Setup & Run Instructions

**Clone the repository**

```bash
git clone https://github.com/egshiglen-henny/novamind.git
cd novamind
```

**Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Set your OpenAI API key**

```bash
setx OPENAI_API_KEY "your_api_key_here"   # Windows
export OPENAI_API_KEY="your_api_key_here" # macOS/Linux
```

**Run the app**

```bash
python novamind.py
```

---

## 4. Running Tests Locally

Run all tests:

```bash
pytest -v
```

Run with coverage:

```bash
pytest --cov=novamind -v
```

Example output:

```
---------- coverage: platform win32, python 3.13 ----------
Name           Stmts   Miss  Cover
----------------------------------
novamind.py       95      0   100%
----------------------------------
TOTAL             95      0   100%
```

---

## 5. File Structure

```
NovaMind/
├── novamind.py
├── requirements.txt
├── README.md
├── coverage.svg                 # auto-generated coverage badge
├── .github/
│   └── workflows/
│       └── python-app.yml       # CI pipeline
└── tests/
    ├── test_validation.py
    ├── test_brainstorm.py
    └── test_e2e.py              # full pipeline test

```

---

## 6. Validation Logic Highlights

The `validate_input()` function uses **regex + heuristics** to ensure realistic text input.

| Rule                           | Example                     | Accepted? |
| ------------------------------ | --------------------------- | --------- |
| Letters, numbers, tech symbols | `C++`, `AI/ML`, `3D design` | ✅         |
| Numbers only                   | `1234`                      | ❌         |
| Empty or spaces                | `"   "`                     | ❌         |
| Repetitive chars               | `aaaaaa`                    | ❌         |
| Gibberish                      | `asldkfjasldkjf`            | ❌         |
| Realistic tech term            | `Machine Learning`          | ✅         |

---

## 7. Test Coverage

* **Functional testing** (`pytest`) – validates correct behavior of validation logic
* **Mocked API testing** – ensures `brainstorm()` correctly interacts with OpenAI client
* **Coverage reports** with `pytest-cov`
* **Continuous validation** through reproducible test suite

---

## 8. Continuous Integration (CI)

NovaMind includes a fully automated **GitHub Actions CI pipeline** that ensures code quality and reliability on every push and pull request.

### The CI workflow performs:

- 🔄 **Python version matrix:** Tests run on Python **3.12** and **3.13**
- 🧹 **Linting:** `flake8` enforces code style and catches syntax issues
- 🧪 **Unit Tests:** `pytest` runs validation, brainstorm, and E2E tests
- 📊 **Coverage Reports:** Automatically generated with `pytest-cov`
- 🏷️ **Coverage Badge:** Auto-updated `coverage.svg` committed to the repo
- 📁 **Artifact Upload:** CI saves coverage reports for inspection

You can view all CI runs here:  
👉 https://github.com/egshiglen-henny/novamind/actions

---

## 9. Summary

NovaMind demonstrates the integration of **AI-powered idea generation**, **prompt engineering**, and **smart validation** within a lightweight, test-driven Python application.

> 🧠 “Turning thoughts into structured ideas — powered by AI.”

---

## 👩‍💻 Author
**Egshiglen Enkhbayar**
📍 Dublin, Ireland
🔗 [GitHub](https://github.com/egshiglen-henny)	|	[LinkedIn](https://linkedin.com/in/egshiglene)

