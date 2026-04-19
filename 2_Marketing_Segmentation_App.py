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

  /* ── Feature module cards ── */
  .feature-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 1rem;
  }
  .feature-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 0.9rem 1rem;
  }
  .feature-icon {
      font-size: 1.4rem;
      margin-bottom: 6px;
  }
  .feature-title {
      font-size: 0.88rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 5px;
  }
  .feature-body {
      font-size: 0.8rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.5;
      margin: 0;
  }

  /* ── Segment archetype cards ── */
  .archetype-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px;
      margin-bottom: 1rem;
  }
  .archetype-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 0.85rem 0.9rem;
      text-align: center;
  }
  .archetype-name {
      font-size: 0.82rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 5px;
  }
  .archetype-signal {
      font-size: 0.75rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
      line-height: 1.4;
  }
  .archetype-action {
      font-size: 0.72rem;
      color: #F5EEDD;
      background: #4A3F35;
      border: 1px solid #7A6E60;
      border-radius: 6px;
      padding: 3px 6px;
      display: inline-block;
  }

  /* ── Privacy grid ── */
  .privacy-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin-bottom: 1rem;
  }
  .privacy-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 0.85rem 1rem;
  }
  .privacy-prop {
      font-size: 0.85rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .privacy-impl {
      font-size: 0.8rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.5;
      margin: 0;
  }

  /* ── CTA button ── */
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
  .cta-btn:hover { opacity: 0.85; }
</style>
""", unsafe_allow_html=True)

# ── Hero ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-title">BMY Analytics</div>
<div class="page-subtitle">Privacy-First Customer Segmentation &amp; Marketing Intelligence</div>
<div style="margin-bottom: 0.9rem;">
  <span class="tag">Python</span>
  <span class="tag">K-Means Clustering</span>
  <span class="tag">scikit-learn</span>
  <span class="tag">Streamlit</span>
  <span class="tag">Plotly</span>
  <span class="tag">RFM Analysis</span>
  <span class="tag tag-accent">Live App</span>
</div>
<div class="cta-row">
  <a class="cta-btn cta-primary" href="https://marketingseg.streamlit.app/" target="_blank">&#9654; Try the Live Demo</a>
  <a class="cta-btn cta-secondary" href="https://github.com/Brandon-m-Y/Marketing_Analytics_App" target="_blank">View on GitHub</a>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── Stat cards ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-number">5</div>
    <div class="stat-label">Pipeline Modules</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">100%</div>
    <div class="stat-label">Local Processing</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">K-Means</div>
    <div class="stat-label">Core ML Engine</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">0</div>
    <div class="stat-label">Cloud Uploads</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Business Problem ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
  <div class="section-title">Business Problem</div>
  <p class="section-body">
    Small businesses and marketing agencies are sitting on goldmines of customer data — transaction
    histories, email lists, CRM exports — but lack the in-house data science capability to turn that
    data into decisions. Enterprise platforms like Salesforce and HubSpot charge thousands per month
    for segmentation features, and they do it by processing your most sensitive asset on their servers.
    <br><br>
    BMY Analytics answers one fundamental question: <strong style="color:#F5EEDD;">Who are my customers,
    how are they different from each other, and what should I do differently for each group?</strong>
    Every computation runs locally — no cloud uploads, no subscriptions, no tracking.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Workflow Steps ───────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">End-to-End Workflow</div>', unsafe_allow_html=True)

st.markdown("""
<div class="workflow-grid">

  <div class="workflow-card">
    <div class="step-badge">STEP 1</div>
    <div>
      <div class="step-title">Business Understanding &amp; Problem Definition</div>
      <p class="step-body">Frames four core marketing ROI outcomes: identify VIPs, win back
      churners, find upsell targets, and suppress low-engagement audiences from broad campaigns.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 2</div>
    <div>
      <div class="step-title">Data Acquisition &amp; Initial Inspection</div>
      <p class="step-body">Accepts CSV, TXT, or Excel up to 200 MB with automatic delimiter
      detection. Preview pane surfaces row/column counts, detected types, and data health before
      any processing begins.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 3</div>
    <div>
      <div class="step-title">Exploratory Data Analysis (EDA)</div>
      <p class="step-body">Interactive Plotly charts covering missingness analysis, histogram
      &amp; boxplot explorer, a point-and-click scatter builder, and a Pearson correlation
      heatmap across all numeric columns.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 4</div>
    <div>
      <div class="step-title">Data Preprocessing &amp; Feature Engineering</div>
      <p class="step-body">No-code calculated fields, column concatenation, numeric binning,
      date/time extraction, and type standardization. RFM metrics (Recency, Frequency,
      Monetary) can be derived entirely within the interface.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 5</div>
    <div>
      <div class="step-title">K-Means Clustering &amp; Segmentation</div>
      <p class="step-body">Auto-filters ID/zero-variance columns, iterates K across a
      user-defined range, applies kneed elbow detection, and presents three
      candidate K values side-by-side before fitting. StandardScaler + SimpleImputer ensure
      no feature dominates cluster geometry.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 6</div>
    <div>
      <div class="step-title">Model Evaluation &amp; Cluster Profiling</div>
      <p class="step-body">Silhouette score, cluster size distribution, per-segment profile
      tables, and PCA scatter visualization. A diff-insight engine flags any feature where
      a segment deviates more than 20% from the dataset mean.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 7</div>
    <div>
      <div class="step-title">Insights &amp; Marketing Recommendations</div>
      <p class="step-body">Statistical output is translated into campaign-ready language:
      plain-English callouts like "85% higher monetary than average — top revenue driver"
      map directly to VIP, win-back, upsell, and suppression actions.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 8</div>
    <div>
      <div class="step-title">Streamlit App &amp; Deployment</div>
      <p class="step-body">Multi-page app with persistent session_state so
      cleaned and engineered data flows automatically through each module. Deployed on
      Streamlit Community Cloud with zero server-side data persistence — all state is
      ephemeral and local to the browser session.</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── App Features ─────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">App Features at a Glance</div>', unsafe_allow_html=True)

st.markdown("""
<div class="feature-grid">

  <div class="feature-card">
    <div class="feature-icon">📥</div>
    <div class="feature-title">Data Intake</div>
    <p class="feature-body">CSV / TXT / Excel upload, auto-delimiter detection, 200 MB limit,
    instant preview, and data health summary.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">🧹</div>
    <div class="feature-title">Data Cleaning</div>
    <p class="feature-body">Deduplication, missing value strategies (drop / fill / interpolate),
    type casting, and format standardization.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">🧠</div>
    <div class="feature-title">Feature Engineering</div>
    <p class="feature-body">Calculated metrics, numeric binning, date/time extraction,
    column concatenation, and custom transformations — no code required.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">🔍</div>
    <div class="feature-title">EDA Suite</div>
    <p class="feature-body">Interactive missingness heatmap, distribution explorer,
    scatter builder, and Pearson correlation matrix via Plotly.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">🧩</div>
    <div class="feature-title">Customer Segmentation</div>
    <p class="feature-body">K-Means with auto elbow detection, silhouette scoring, PCA
    visualization, segment profiling, and labeled CSV export.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">🔒</div>
    <div class="feature-title">Privacy-First</div>
    <p class="feature-body">100% local processing, no telemetry, no cloud uploads.
    Works fully offline. Compliant-friendly for GDPR / CCPA / HIPAA contexts.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Segment Archetypes ───────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Segment Archetypes &amp; Marketing Actions</div>', unsafe_allow_html=True)

st.markdown("""
<div class="archetype-grid">

  <div class="archetype-card">
    <div class="archetype-name">VIPs</div>
    <div class="archetype-signal">High frequency · High monetary · Low recency</div>
    <div class="archetype-action">Loyalty rewards &amp; early access</div>
  </div>

  <div class="archetype-card">
    <div class="archetype-name">At-Risk</div>
    <div class="archetype-signal">Historically high value · High recency (lapsed)</div>
    <div class="archetype-action">Win-back emails &amp; personal outreach</div>
  </div>

  <div class="archetype-card">
    <div class="archetype-name">Promising</div>
    <div class="archetype-signal">Moderate frequency · Rising monetary</div>
    <div class="archetype-action">Upsell to premium tier</div>
  </div>

  <div class="archetype-card">
    <div class="archetype-name">Price-Sensitive</div>
    <div class="archetype-signal">High frequency · Low monetary</div>
    <div class="archetype-action">Bundle deals &amp; bulk discounts</div>
  </div>

  <div class="archetype-card">
    <div class="archetype-name">New / Explorers</div>
    <div class="archetype-signal">Low frequency · Low monetary</div>
    <div class="archetype-action">Onboarding &amp; first-purchase incentives</div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Technical Deep Dives (Expanders) ─────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

with st.expander("K-Means Implementation Details", expanded=False):
    st.markdown("""
**Feature preparation pipeline** — Before fitting, the app auto-removes ID-like columns,
zero-variance columns, and sequential row-number columns. Users can override in the Advanced
Options panel.

**Elbow analysis** — Iterates K-Means across a user-defined range (default 2–10), plots
inertia vs. K, then applies `kneed` convex curve detection to identify the inflection point.

**Guided K selection** — Presents elbow − 1, elbow, and elbow + 1 side-by-side with a
recommended marker and cluster size preview before the final fit.
""")
    st.code("""from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")
scaler  = StandardScaler()

X_imputed = imputer.fit_transform(features_df)
X_scaled  = scaler.fit_transform(X_imputed)

kmeans = KMeans(n_clusters=chosen_k, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)""", language="python")

with st.expander("RFM Feature Engineering", expanded=False):
    st.markdown("""
Recency, Frequency, and Monetary columns can be engineered inside the app's Feature Engineering
module without any code. For reference, the equivalent pandas logic is shown below — this is
what the app computes under the hood when date and transaction columns are mapped.
""")
    st.code("""today = pd.Timestamp("today")

rfm = df.groupby("customer_id").agg(
    recency   = ("last_purchase_date", lambda d: (today - d.max()).days),
    frequency = ("order_id",           "nunique"),
    monetary  = ("order_value",        "sum"),
).reset_index()""", language="python")

with st.expander("Tech Stack", expanded=False):
    st.markdown("""
| Layer | Library | Version |
|---|---|---|
| App framework | Streamlit | ≥ 1.54 |
| Data manipulation | pandas, NumPy | ≥ 2.0, ≥ 1.24 |
| Machine learning | scikit-learn | ≥ 1.3 |
| Statistical computing | SciPy | ≥ 1.11 |
| Elbow detection | kneed | ≥ 0.8.5 |
| Visualization | Plotly, Seaborn, Matplotlib | ≥ 5.17, ≥ 0.12, ≥ 3.7 |
| File I/O | openpyxl, pyarrow | ≥ 3.1, ≥ 18 |
| Deployment | Streamlit Community Cloud | — |
""")

# ── Privacy Architecture ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Privacy Architecture</div>', unsafe_allow_html=True)

st.markdown("""
<div class="privacy-grid">

  <div class="privacy-card">
    <div class="privacy-prop">No Server</div>
    <p class="privacy-impl">Streamlit Community Cloud serves only static app code. All computation
    runs inside the user's browser session — never on a shared server.</p>
  </div>

  <div class="privacy-card">
    <div class="privacy-prop">No Persistence</div>
    <p class="privacy-impl">Session state is ephemeral. All uploaded data is cleared the moment
    the browser tab closes — nothing is written to disk or database.</p>
  </div>

  <div class="privacy-card">
    <div class="privacy-prop">No Telemetry</div>
    <p class="privacy-impl">Zero analytics, tracking pixels, or usage logging in the codebase.
    Every claim is verifiable by reading the open-source code directly.</p>
  </div>

  <div class="privacy-card">
    <div class="privacy-prop">Compliance-Friendly</div>
    <p class="privacy-impl">Local execution means customer PII never crosses a network boundary
    under this tool's operation — favorable for GDPR, CCPA, and HIPAA contexts.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Roadmap ───────────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="section-card">
  <div class="section-title">v1.1 — Coming Soon</div>
  <p class="section-body">
    ☐ &nbsp;Linear regression for sales forecasting<br>
    ☐ &nbsp;Time-series visualization (trend lines, seasonality decomposition)<br>
    ☐ &nbsp;R² and RMSE evaluation metrics<br>
    ☐ &nbsp;AI-powered segment naming via user's own API key (anonymized summaries only)<br>
    ☐ &nbsp;Downloadable forecast results
  </p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="section-card">
  <div class="section-title">v2.0 — Planned</div>
  <p class="section-body">
    ☐ &nbsp;Churn prediction with classification models and probability scores<br>
    ☐ &nbsp;Campaign uplift / A/B impact analysis<br>
    ☐ &nbsp;Agglomerative clustering as an alternative to K-Means<br>
    ☐ &nbsp;Power BI / Tableau export connectors<br>
    ☐ &nbsp;Real-time scoring mode for new customer records
  </p>
</div>
""", unsafe_allow_html=True)

# ── CTA Footer ────────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
  <div>
    <div style="font-size: 1rem; font-weight: 600; color: #F5EEDD; margin-bottom: 4px;">
      Ready to segment your customers?
    </div>
    <div class="secondary-text" style="font-size: 0.9rem;">
      Upload any customer CSV and go from raw data to labeled segments in minutes.
    </div>
  </div>
  <div class="cta-row" style="margin-top: 0;">
    <a class="cta-btn cta-primary" href="https://marketingseg.streamlit.app/" target="_blank">&#9654; Open Live App</a>
    <a class="cta-btn cta-secondary" href="https://github.com/Brandon-m-Y/Marketing_Analytics_App" target="_blank">View Source</a>
  </div>
</div>
""", unsafe_allow_html=True)
