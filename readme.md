# 📊 Brandon Ytuarte — Data Science & Analytics Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.x-189AB4)](https://xgboost.readthedocs.io/)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e)](https://opensource.org/licenses/MIT)

> **An interactive Streamlit portfolio showcasing end-to-end data science and analytics projects — from customer segmentation and credit risk modeling to market intelligence and subscription prediction.**

🔗 [**View the Live Portfolio →**](https://brandon-ytuarte-portfolio.streamlit.app/)

---

## Table of Contents

1. [About This Portfolio](#about-this-portfolio)
2. [Featured Projects](#featured-projects)
   - [MSBA Capstone — UCI Bank Marketing](#1-msba-capstone--uci-bank-marketing)
   - [BMY Analytics — Marketing Segmentation App](#2-bmy-analytics--marketing-segmentation-app)
   - [Credit Risk Modeling Pipeline](#3-credit-risk-modeling-pipeline)
   - [Python Data Job Market Analysis](#4-python-data-job-market-analysis)
3. [Tech Stack](#tech-stack)
4. [Portfolio Structure](#portfolio-structure)
5. [Quick Start](#quick-start)
6. [About the Author](#about-the-author)

---

## About This Portfolio

I am a **Master of Science in Business Analytics (MSBA)** graduate with a passion for building data-driven solutions that bridge technical rigor and real business impact. My background spans business strategy, machine learning, and marketing analytics — and this portfolio is where those threads come together.

Each project here reflects the full analytical lifecycle: defining a business problem, acquiring and cleaning data, running exploratory analysis, building and evaluating models, and deploying results in an interactive interface that non-technical stakeholders can actually use.

**What you'll find:**

- End-to-end ML pipelines with documented decision-making at every step
- Customer segmentation and classification work on real-world datasets
- Privacy-first application architecture for sensitive customer data
- Labor market intelligence derived from live job posting data
- Deployed Streamlit applications — not just notebooks

**Target audience:** Hiring managers, analytics leads, and consulting clients evaluating applied data science capability.

---

## Featured Projects

### 1. MSBA Capstone — UCI Bank Marketing

> *Customer Segmentation & Term Deposit Subscription Prediction*

🔗 [**Live App →**](https://msba-capstone-project.streamlit.app/)

The capstone project for my MSBA degree. Portuguese banks run outbound telemarketing campaigns to sell term deposit subscriptions with a natural conversion rate of ~11%. This project answers two strategic questions simultaneously: **who is most likely to subscribe**, and **what types of customers exist** — using a production-ready ML pipeline deployed in a six-page Streamlit dashboard.

**Key highlights:**

| Dimension | Detail |
|---|---|
| Dataset | UCI Bank Marketing — 41,188 records × 21 features |
| After cleaning | 39,803 records × 22 columns |
| Class balance | 88.7% negative / 11.3% positive (imbalanced) |
| Primary metric | PR-AUC (superior to accuracy/ROC-AUC for rare positive class) |
| Clustering | Agglomerative Clustering — Ward linkage, k=3 |
| Classification | Tuned XGBoost — **PR-AUC: 0.8522** |
| Dashboard | 6-page Streamlit app with EDA, cluster profiling, and real-time scoring |

**Three customer segments identified:**

| Cluster | Size | Subscription Rate | Key Driver | Strategy |
|---|---|---|---|---|
| Repeat Responders | 13.65% | 26.43% | Prior positive campaign result | Warm re-engagement |
| Engaged Long-Callers ⭐ | 20.90% | **36.67%** | Long calls + low Euribor | Invest in call quality |
| Cold Prospects | 65.45% | 0.00% | High Euribor environment | Deprioritize until rates fall |

**Top business finding:** Concentrating campaign effort on Clusters 0 and 1 — just 34% of contacts — captures nearly all subscriptions, enabling dramatic ROI improvement without sacrificing reach.

**Tools:** Python · scikit-learn · XGBoost · Agglomerative Clustering · PCA · Streamlit · pandas · seaborn · matplotlib

---

### 2. BMY Analytics — Marketing Segmentation App

> *Privacy-First Customer Segmentation & Marketing Intelligence*

🔗 [**Live App →**](https://marketingseg.streamlit.app/)

Small businesses are sitting on goldmines of customer data but lack affordable tools to segment audiences without sending sensitive records to enterprise cloud platforms. BMY Analytics delivers professional-grade segmentation entirely on the user's machine — no cloud uploads, no subscriptions, no tracking.

**Key highlights:**

| Dimension | Detail |
|---|---|
| Core algorithm | K-Means with automatic elbow detection (`kneed`) |
| Pipeline modules | 5 — Data Intake, Cleaning, Feature Engineering, EDA, Segmentation |
| Privacy model | 100% local processing, zero telemetry, works fully offline |
| Output | Labeled CSV export ready for CRM / email platform import |
| Deployment | Streamlit Community Cloud — ephemeral session state, no persistence |

**Five customer archetype outputs:**

| Segment | RFM Signal | Marketing Action |
|---|---|---|
| VIPs | High frequency · High monetary · Low recency | Loyalty rewards & early access |
| At-Risk | Historically high value · Lapsed (high recency) | Win-back emails & personal outreach |
| Promising | Moderate frequency · Rising monetary | Upsell to premium tier |
| Price-Sensitive | High frequency · Low monetary | Bundle deals & bulk discounts |
| New / Explorers | Low frequency · Low monetary | Onboarding & first-purchase incentives |

**Pipeline overview:**

```
Upload (CSV/TXT/Excel) → Clean → Engineer Features → EDA → Segment → Export Labeled CSV
```

Each page passes data forward automatically via `session_state` — no re-uploading between steps.

**Tools:** Python · scikit-learn · K-Means · kneed · StandardScaler · PCA · Plotly · Streamlit · pandas · NumPy

---

### 3. Credit Risk Modeling Pipeline

> *German Credit Data: EDA → Multi-Model Benchmarking → XGBoost → Streamlit Prediction App*

End-to-end credit risk scoring pipeline on the **German Credit Risk dataset** (Kaggle, 1,000 applicants). Replicates the full analytical workflow a data science team at a bank or fintech would follow — from raw data through rigorous EDA, feature engineering, four-model benchmarking, and a live Streamlit prediction interface.

**Key highlights:**

| Dimension | Detail |
|---|---|
| Dataset | German Credit Risk — 1,000 rows × 10 features + 1 target |
| After null removal | 522 records (55.7% Good / 44.3% Bad) |
| Task | Binary classification — Good (1) / Bad (0) |
| Models benchmarked | Decision Tree · Extra Trees · Random Forest · XGBoost |
| Tuning method | GridSearchCV — 5-fold CV |
| Winner | **XGBoost — 66.7% test accuracy** |
| Deployment | Streamlit prediction app with real-time single-applicant scoring |

**Model benchmark results:**

| Model | Test Accuracy | Notes |
|---|---|---|
| Decision Tree | 60.0% | Baseline |
| Extra Trees | 62.9% | — |
| Random Forest | 64.8% | — |
| **XGBoost** | **66.7%** | Shallow trees + aggressive subsampling |

**Key EDA finding:** Bad-risk applicants carry an average loan balance **38.6% higher** than good-risk applicants (€3,881 vs €2,801) and a median loan duration **40% longer** (25.4 vs 18.1 months). Account health (checking/savings balance tier) is the strongest categorical predictor.

**8 predictive features:** Age · Sex · Job (skill level 0–3) · Housing · Saving accounts · Checking account · Credit amount · Duration

**Tools:** Python · XGBoost · scikit-learn · GridSearchCV · LabelEncoder · joblib · Streamlit · pandas · seaborn · matplotlib

---

### 4. Python Data Job Market Analysis

> *Skill Demand, Salary Trends & Optimal Learning Paths for Data Roles — US 2023*

Python-based analysis of 2023 US job postings answering four career-critical questions that directly shape skill investment decisions for anyone targeting the data field.

**Key highlights:**

| Dimension | Detail |
|---|---|
| Dataset | US job postings — 2023 |
| Roles analyzed | Data Analyst · Data Scientist · Data Engineer |
| Analysis questions | 4 |
| Visualization library | matplotlib · seaborn · adjustText |
| Notebook | Jupyter — fully reproducible |

**Four analysis questions:**

| # | Question | Key Finding |
|---|---|---|
| Q1 | Most demanded skills by role? | Python #1 for Data Scientists (72%) and Engineers (65%); SQL #1 for Analysts (51%) |
| Q2 | How are skills trending in 2023? | SQL consistent all year; Excel surged in September; Power BI shows upward trend |
| Q3 | How well do roles and skills pay? | Senior Data Scientist up to $600K; specialized skills (dplyr, Bitbucket) reach $200K |
| Q4 | Most optimal skills to learn? | Programming (Python) highest salary ceiling; SQL/Excel highest demand — clear tradeoff |

**Top 5 skills by role:**

| Data Analyst | Data Scientist | Data Engineer |
|---|---|---|
| SQL (51%) | Python (72%) | SQL (68%) |
| Excel (41%) | SQL (51%) | Python (65%) |
| Tableau (28%) | R (44%) | AWS (43%) |
| Python (27%) | Tableau (24%) | Azure (32%) |
| Power BI (20%) | SAS (24%) | Spark (32%) |

**Core insight:** The most in-demand skills (SQL, Excel) are not the highest paid. Analysts maximizing career potential should build a foundational layer for employability and a specialized layer (Python, cloud, database tools) to push compensation upward.

**Tools:** Python · pandas · matplotlib · seaborn · adjustText · Jupyter · PercentFormatter

---

## Tech Stack

| Layer | Tools |
|---|---|
| App framework | Streamlit |
| Language | Python 3.10+ |
| Machine learning | scikit-learn · XGBoost |
| Data manipulation | pandas · NumPy |
| Visualization | Plotly · matplotlib · seaborn |
| Clustering | AgglomerativeClustering · KMeans · kneed |
| Model persistence | joblib |
| Dimensionality reduction | PCA |
| Notebook environment | Jupyter |
| Deployment | Streamlit Community Cloud |

---

## Portfolio Structure

```
1_About_Me_Portfolio/
│
├── app.py                          # Multi-page app entry point & navigation
├── 0_Home_Page.py                  # Bio, stats, featured project cards, links
├── 1_MSBA_Capstone_Project.py      # UCI Bank Marketing — clustering + classification
├── 2_Marketing_Segmentation_App.py # BMY Analytics — K-Means segmentation app
├── 3_Credit _Risk_Modeling.py      # German Credit Risk — XGBoost pipeline
├── 4_Python_Data_Job_Analysis_4.py # 2023 US job market analysis
│
├── images/                         # Portfolio-level assets (logo, headshot, favicon)
├── MSBA Capstone Images/           # EDA and modeling charts — Capstone project
├── Marketing Segmentation App Images/  # App screenshots — segmentation project
├── Credit Risk Modeling Images/    # EDA and model evaluation charts
├── Python Data Job Analysis Images/    # Visualization outputs — job market analysis
│
└── readme.md
```

---

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Brandon-m-Y/portfolio
cd 1_About_Me_Portfolio

# 2. Create a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install streamlit pandas numpy scikit-learn xgboost plotly matplotlib seaborn kneed joblib openpyxl

# 4. Launch the portfolio
streamlit run app.py
```

The portfolio will open at `http://localhost:8501`. Navigate between projects using the sidebar.

---

## About the Author

**Brandon Ytuarte** — Data Scientist & Business Analyst | MSBA Graduate

I build end-to-end analytical solutions that translate complex data into decisions businesses can act on. My work spans machine learning, customer segmentation, credit risk modeling, and labor market intelligence — always with an eye toward deployment, explainability, and real-world applicability.

Currently pivoting into the analytics industry through an upcoming **Marketing Analytics internship**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-brandon--m--ytuarte-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brandon-m-ytuarte/)
[![GitHub](https://img.shields.io/badge/GitHub-Brandon--m--Y-181717?logo=github&logoColor=white)](https://github.com/Brandon-m-Y)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live%20App-FF4B4B?logo=streamlit&logoColor=white)](https://brandon-ytuarte-portfolio.streamlit.app/)

---

*MIT License · Built with Python & Streamlit · BMY Analytics*
