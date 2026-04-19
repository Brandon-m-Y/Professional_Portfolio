import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
  [data-testid="stAppViewContainer"] {
      background: radial-gradient(circle at top left, #3A3A3A 0%, #2F2F2F 45%, #242424 100%);
  }
  [data-testid="stHeader"] { background-color: #2B2B2B; }
  [data-testid="stSidebar"] { background-color: #262626; }

  .block-container {
      padding-top: 2.5rem;
      padding-bottom: 3rem;
      max-width: 1200px;
      padding-left: 2.5rem;
      padding-right: 2.5rem;
  }

  html, body, [class*="css"] {
      color: #F5EEDD;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  /* ── Typography ── */
  .page-title {
      font-size: 2.2rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 0.3rem;
      line-height: 1.2;
  }
  .page-subtitle {
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      font-size: 1.05rem;
      margin-bottom: 1rem;
  }
  .section-label {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.1em;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
  }
  .divider {
      border: none;
      border-top: 1px solid #5A5349;
      margin: 1.5rem 0;
  }
  .secondary-text {
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.65;
  }

  /* ── Tags / Pills ── */
  .tag {
      display: inline-block;
      padding: 5px 14px;
      border-radius: 999px;
      border: 1px solid #8A8073;
      font-size: 13px;
      color: #F5EEDD;
      background: #3A3A3A;
      margin: 3px 4px 3px 0;
  }
  .tag-accent {
      background: #4A3F35;
      border-color: #A39A88;
      color: #F5EEDD;
  }

  /* ── Stat cards ── */
  .stat-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin: 1.25rem 0 1.5rem;
  }
  .stat-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1.1rem 1.25rem 0.9rem;
  }
  .stat-number {
      font-size: 24px;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .stat-label {
      font-size: 13px;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
  }

  /* ── Section cards ── */
  .section-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1.1rem 1.25rem;
      margin-bottom: 0.85rem;
  }
  .section-title {
      color: #F5EEDD;
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 0.45rem;
  }
  .section-body {
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.7;
      margin: 0;
      font-size: 0.95rem;
  }

  /* ── Workflow steps ── */
  .workflow-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 1rem;
  }
  .workflow-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1rem 1.1rem;
      display: flex;
      gap: 0.85rem;
      align-items: flex-start;
  }
  .step-badge {
      background: #4A3F35;
      border: 1px solid #A39A88;
      border-radius: 8px;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 700;
      color: #F5EEDD;
      flex-shrink: 0;
      letter-spacing: 0.05em;
      margin-top: 2px;
  }
  .step-title {
      font-size: 0.9rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .step-body {
      font-size: 0.82rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.55;
      margin: 0;
  }

  /* ── EDA finding cards ── */
  .finding-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 1rem;
  }
  .finding-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1rem 1.1rem;
  }
  .finding-title {
      font-size: 0.88rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 5px;
  }
  .finding-body {
      font-size: 0.81rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.55;
      margin: 0;
  }
  .finding-stat {
      font-size: 1.1rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 3px;
  }

  /* ── Model comparison cards ── */
  .model-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 1rem;
  }
  .model-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 0.9rem 1rem;
      text-align: center;
  }
  .model-card.winner {
      border-color: #A39A88;
      background: linear-gradient(145deg, #4A3F35 0%, #3A3028 100%);
  }
  .model-name {
      font-size: 0.85rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 6px;
  }
  .model-accuracy {
      font-size: 1.6rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .model-params {
      font-size: 0.72rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.45;
      margin: 0;
  }
  .winner-badge {
      display: inline-block;
      background: #5A4A3A;
      border: 1px solid #A39A88;
      border-radius: 6px;
      padding: 2px 8px;
      font-size: 11px;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 6px;
  }

  /* ── Feature table ── */
  .feature-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 9px;
      margin-bottom: 1rem;
  }
  .feature-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 10px;
      padding: 0.75rem 0.9rem;
  }
  .feature-name {
      font-size: 0.83rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 3px;
  }
  .feature-type {
      font-size: 0.74rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      margin: 0;
  }

  /* ── CTA ── */
  .cta-row {
      display: flex;
      gap: 12px;
      margin-top: 0.5rem;
      flex-wrap: wrap;
  }
  .cta-btn {
      display: inline-block;
      padding: 10px 22px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 600;
      text-decoration: none;
      color: #F5EEDD !important;
      -webkit-text-fill-color: #F5EEDD !important;
  }
  .cta-primary {
      background: linear-gradient(135deg, #6B5E4E 0%, #4A3F35 100%);
      border: 1px solid #A39A88;
  }
  .cta-secondary {
      background: transparent;
      border: 1px solid #5A5349;
  }
</style>
""", unsafe_allow_html=True)

# ── Hero ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-title">Credit Risk Modeling Pipeline</div>
<div class="page-subtitle">German Credit Data → EDA → Multi-Model Benchmarking → XGBoost → Streamlit Prediction App</div>
<div style="margin-bottom: 0.9rem;">
  <span class="tag">Python</span>
  <span class="tag">XGBoost</span>
  <span class="tag">scikit-learn</span>
  <span class="tag">Binary Classification</span>
  <span class="tag">GridSearchCV</span>
  <span class="tag">Streamlit</span>
  <span class="tag tag-accent">Deployed App</span>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── Stat cards ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-number">4</div>
    <div class="stat-label">Models Benchmarked</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">66.7%</div>
    <div class="stat-label">Best Accuracy (XGBoost)</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">1,000</div>
    <div class="stat-label">Dataset Rows</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">8</div>
    <div class="stat-label">Predictive Features</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Business Problem ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
  <div class="section-title">Business Problem</div>
  <p class="section-body">
    Credit default is one of the most costly risks a lending institution faces. When a borrower fails
    to repay, lenders absorb not only the outstanding principal but also the operational costs of
    collections, regulatory capital charges, and reputational damage. Accurately identifying
    high-risk applicants before a loan is issued is therefore a core function of any modern
    credit underwriting operation.
    <br><br>
    This project builds a production-oriented credit risk scoring pipeline on the
    <strong style="color:#F5EEDD;">German Credit Risk dataset</strong> (Kaggle, 1,000 applicants).
    It replicates the full analytical workflow a data science team at a bank or fintech would follow —
    from raw data ingestion through rigorous EDA, feature engineering, multi-model benchmarking, and
    an interactive Streamlit scoring interface. Credit decisions are asymmetric:
    <strong style="color:#F5EEDD;">approving a bad borrower costs far more than rejecting a good one</strong>,
    so class-balanced training is enforced throughout.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Workflow ─────────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">End-to-End Workflow</div>', unsafe_allow_html=True)

st.markdown("""
<div class="workflow-grid">

  <div class="workflow-card">
    <div class="step-badge">STEP 1</div>
    <div>
      <div class="step-title">Business Understanding &amp; Problem Definition</div>
      <p class="step-body">Frames the ML task as binary classification (Good = 1 / Bad = 0) on
      1,000 German credit applicants. Success metric is accuracy on a held-out test set with
      class-balanced model selection, targeting real-time scoring via Streamlit.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 2</div>
    <div>
      <div class="step-title">Data Acquisition &amp; Initial Inspection</div>
      <p class="step-body">1,000 rows × 11 columns. No duplicate rows. Two features with
      significant missingness: Saving accounts (18.3%) and
      Checking account (39.4%). Class imbalance in full dataset: 70'%' Good / 30%
      Bad. After listwise deletion: 522 records, near-balanced at 55.7% / 44.3%.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 3</div>
    <div>
      <div class="step-title">Exploratory Data Analysis</div>
      <p class="step-body">Three-axis EDA: univariate distributions (age ~normal, credit amount
      and duration right-skewed), bivariate splits by risk label, and a Pearson correlation
      heatmap. Key signal: bad-risk borrowers carry 38.6% higher average loan balances and
      40% longer tenors than good-risk borrowers.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 4</div>
    <div>
      <div class="step-title">Data Preprocessing &amp; Feature Engineering</div>
      <p class="step-body">Listwise deletion for missing account fields (imputation rejected —
      these are the strongest predictors). LabelEncoder for Sex, Housing, Saving accounts,
      Checking account, persisted to .pkl for consistent inference. 80/20
      stratified split: 417 train / 105 test samples.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 5</div>
    <div>
      <div class="step-title">Multi-Model Training &amp; Hyperparameter Tuning</div>
      <p class="step-body">Four classifiers benchmarked with a unified GridSearchCV
      helper (5-fold CV, accuracy scoring, n_jobs=-1): Decision Tree, Random Forest,
      Extra Trees, and XGBoost. All tree-based models use
      class_weight='balanced'; XGBoost uses
      scale_pos_weight for minority-class up-weighting.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 6</div>
    <div>
      <div class="step-title">Model Evaluation &amp; Comparison</div>
      <p class="step-body">XGBoost wins at 66.7% test accuracy (+1.9 pp over Random Forest,
      +6.7 pp over Decision Tree baseline). Shallow trees (max_depth=3 reduce
      overfitting on the 522-sample dataset. Aggressive subsampling
      (subsample=0.7, colsample_bytree=0.7) provides stochastic
      regularization.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 7</div>
    <div>
      <div class="step-title">Deployment — Streamlit Prediction App</div>
      <p class="step-body">Trained XGBoost model and label encoders persisted via
      joblib. The app collects 8 applicant inputs, encodes categoricals using
      stored encoders, constructs a single-row DataFrame matching training schema,
      and returns a Good / Bad credit risk prediction in real time.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">OUTPUT</div>
    <div>
      <div class="step-title">Business Impact</div>
      <p class="step-body">On a 105-applicant test set, XGBoost correctly classified ~70
      applicants. In a real portfolio, even a 5% lift in bad-loan detection rate translates
      directly to reduced expected credit losses — particularly valuable when the average
      bad loan balance in this dataset is €3,881.</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── EDA Key Findings ─────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">EDA Key Findings</div>', unsafe_allow_html=True)

st.markdown("""
<div class="finding-grid">

  <div class="finding-card">
    <div class="finding-stat">+38.6%</div>
    <div class="finding-title">Credit Amount — Bad vs Good Risk</div>
    <p class="finding-body">Bad-risk applicants carry an average loan balance of €3,881 vs
    €2,801 for good-risk applicants. Higher exposure at default combined with longer tenor
    is a textbook indicator of elevated credit risk.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">r = 0.61</div>
    <div class="finding-title">Credit Amount ↔ Duration Correlation</div>
    <p class="finding-body">The strongest inter-feature relationship in the dataset — larger
    loans structurally require longer repayment windows. Both features independently contribute
    to the model; neither is dropped despite multicollinearity given the small feature set.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">25.4 mo</div>
    <div class="finding-title">Median Loan Duration — Bad Risk</div>
    <p class="finding-body">Bad-risk borrowers have a median loan duration of 25.4 months vs
    18.1 months for good-risk borrowers — a 40% gap. Duration alone is a meaningful signal
    even without account-health features.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">#1 Signal</div>
    <div class="finding-title">Account Health as Top Predictor</div>
    <p class="finding-body">Applicants with little checking account balances are
    disproportionately concentrated in the bad-risk class. Those with rich or
    quite rich savings accounts skew heavily toward good-risk — liquidity buffers
    reduce default probability.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Model Comparison ──────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Model Benchmark Results</div>', unsafe_allow_html=True)

st.markdown("""
<div class="model-grid">

  <div class="model-card">
    <div class="model-name">Decision Tree</div>
    <div class="model-accuracy">60.0%</div>
    <p class="model-params">max_depth=7 · min_samples_leaf=2 · min_samples_split=12</p>
  </div>

  <div class="model-card">
    <div class="model-name">Extra Trees</div>
    <div class="model-accuracy">62.9%</div>
    <p class="model-params">max_depth=None · min_samples_leaf=1 · n_estimators=100</p>
  </div>

  <div class="model-card">
    <div class="model-name">Random Forest</div>
    <div class="model-accuracy">64.8%</div>
    <p class="model-params">max_depth=10 · min_samples_leaf=2 · n_estimators=100</p>
  </div>

  <div class="model-card winner">
    <div class="winner-badge">&#9733; WINNER</div>
    <div class="model-name">XGBoost</div>
    <div class="model-accuracy">66.7%</div>
    <p class="model-params">max_depth=3 · lr=0.3 · n_estimators=200 · subsample=0.7 · colsample_bytree=0.7</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Feature Set ──────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Feature Set (8 Predictors)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-name">Age</div>
    <p class="feature-type">Numeric · 19–75, mean 35.5</p>
  </div>
  <div class="feature-card">
    <div class="feature-name">Sex</div>
    <p class="feature-type">Categorical · 69% male (label encoded)</p>
  </div>
  <div class="feature-card">
    <div class="feature-name">Job</div>
    <p class="feature-type">Ordinal 0–3 · skill level</p>
  </div>
  <div class="feature-card">
    <div class="feature-name">Housing</div>
    <p class="feature-type">Categorical · own / rent / free</p>
  </div>
  <div class="feature-card">
    <div class="feature-name">Saving Accounts</div>
    <p class="feature-type">Ordinal · little → quite rich (label encoded)</p>
  </div>
  <div class="feature-card">
    <div class="feature-name">Checking Account</div>
    <p class="feature-type">Ordinal · little → rich (label encoded)</p>
  </div>
  <div class="feature-card">
    <div class="feature-name">Credit Amount</div>
    <p class="feature-type">Numeric · €250–€18,424, mean €3,271</p>
  </div>
  <div class="feature-card">
    <div class="feature-name">Duration</div>
    <p class="feature-type">Numeric · 4–72 months, mean 20.9</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Technical Deep Dives ─────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

with st.expander("GridSearchCV Training Pipeline", expanded=False):
    st.markdown("""
A unified helper function benchmarks all four classifiers with identical cross-validation
settings, ensuring a fair apples-to-apples comparison. Class imbalance is handled at the
estimator level rather than via resampling, which avoids data leakage across CV folds.
""")
    st.code("""from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def train_model(model, param_grid, X_train, y_train, X_test, y_test):
    grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_
    y_pred = best_model.predict(X_test)
    return best_model, accuracy_score(y_test, y_pred), grid.best_params_

# XGBoost search space
xgb_params = {
    "n_estimators":     [100, 200],
    "max_depth":        [3, 5, 7, 10, 12, 15],
    "learning_rate":    [0.01, 0.1, 0.2, 0.3],
    "subsample":        [0.7, 1.0],
    "colsample_bytree": [0.7, 1.0],
}""", language="python")

with st.expander("Preprocessing & Encoding Pipeline", expanded=False):
    st.markdown("""
Label encoders are fitted on training data and persisted to `.pkl` files so the Streamlit app
can apply identical transformations at inference time — a common source of train/serve skew
if not handled carefully. `Purpose` was dropped after EDA showed weak direct association
with the target relative to account-health features.
""")
    st.code("""from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

cat_cols = ["Sex", "Housing", "Saving accounts", "Checking account"]

encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le
    joblib.dump(le, f"{col}_encoder.pkl")

# Stratified split preserves class proportions in both sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)""", language="python")

with st.expander("Streamlit App — Inputs & Inference", expanded=False):
    st.markdown("""
The app loads the trained model and per-column encoders once at startup, then constructs a
single-row `DataFrame` that exactly mirrors the training feature schema before scoring.
""")
    st.markdown("""
| Input | Type | Range / Options |
|---|---|---|
| Age | Numeric | 18–80 |
| Sex | Dropdown | male, female |
| Job | Numeric | 0–3 (skill level) |
| Housing | Dropdown | own, rent, free |
| Saving accounts | Dropdown | little, moderate, rich, quite rich |
| Checking account | Dropdown | little, moderate, rich |
| Credit amount | Numeric | €0+ |
| Duration | Numeric | 1–72 months |
""")
    st.code("""import joblib, pandas as pd, streamlit as st

model    = joblib.load("xgb_credit_model.pkl")
encoders = {col: joblib.load(f"{col}_encoder.pkl") for col in cat_cols}

# Build a single-row DataFrame matching training schema
row = {
    "Age": age, "Sex": encoders["Sex"].transform([sex])[0],
    "Job": job, "Housing": encoders["Housing"].transform([housing])[0],
    "Saving accounts":  encoders["Saving accounts"].transform([saving])[0],
    "Checking account": encoders["Checking account"].transform([checking])[0],
    "Credit amount": credit_amount, "Duration": duration,
}
prediction = model.predict(pd.DataFrame([row]))[0]
label = "Good Risk" if prediction == 1 else "Bad Risk\"""", language="python")

with st.expander("Repository Structure", expanded=False):
    st.markdown("""
| File | Role |
|---|---|
| `german_credit_data.csv` | Source dataset (Kaggle German Credit Risk) |
| `EDA and Modeling.ipynb` | Full EDA, preprocessing, training, evaluation, artifact export |
| `app.py` | Streamlit prediction app |
| `xgb_credit_model.pkl` | Trained XGBoost classifier |
| `Sex_encoder.pkl` | Label encoder for Sex |
| `Housing_encoder.pkl` | Label encoder for Housing |
| `Saving accounts_encoder.pkl` | Label encoder for Saving accounts |
| `Checking account_encoder.pkl` | Label encoder for Checking account |
| `images/` | EDA and modeling visualizations |

> **Note:** `.pkl` artifacts are not committed to the repo. Run all cells in the notebook
> (uncommenting the `joblib.dump()` lines) to regenerate them before launching the app.
""")

with st.expander("Reproducibility & Potential Extensions", expanded=False):
    st.markdown("""
**Reproducibility:** `random_state=42` is used across all train/test splits and sklearn-based
models. XGBoost uses `random_state=1`. Re-running the notebook produces identical results.

**Extensions worth exploring:**

- **Imputation strategies** — Replace listwise deletion with `IterativeImputer` to recover the
  full 1,000-row dataset and measure the accuracy impact.
- **Feature engineering** — Add `credit_amount / duration` as a monthly repayment proxy; bin
  `Age` into risk tiers; apply target encoding to `Purpose`.
- **Probability calibration** — Apply Platt scaling or isotonic regression to convert raw XGBoost
  scores into well-calibrated default probabilities for Expected Loss calculations (EL = PD × LGD × EAD).
- **Threshold optimization** — Optimize the decision threshold using a business cost matrix; false
  negatives cost far more than false positives in credit risk.
- **SHAP explainability** — Add `shap.TreeExplainer` for per-prediction feature attribution — a
  regulatory requirement for model risk management in many jurisdictions.
- **Containerization** — Dockerize `app.py` for cloud deployment (Streamlit Cloud, AWS ECS,
  Azure Container Apps).
""")

# ── CTA Footer ────────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
  <div>
    <div style="font-size: 1rem; font-weight: 600; color: #F5EEDD; margin-bottom: 4px;">
      See the full analysis and source code
    </div>
    <div class="secondary-text" style="font-size: 0.9rem;">
      Notebook · model artifacts · Streamlit app — all in the GitHub repository.
    </div>
  </div>
  <div class="cta-row" style="margin-top: 0;">
    <a class="cta-btn cta-primary" href="https://github.com/Brandon-m-Y" target="_blank">View on GitHub</a>
    <a class="cta-btn cta-secondary" href="https://www.linkedin.com/in/brandon-m-ytuarte/" target="_blank">Connect on LinkedIn</a>
  </div>
</div>
""", unsafe_allow_html=True)
