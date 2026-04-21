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

  /* ── Cluster archetype cards ── */
  .cluster-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 1rem;
  }
  .cluster-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1rem 1.1rem;
  }
  .cluster-card.top {
      border-color: #A39A88;
      background: linear-gradient(145deg, #4A3F35 0%, #3A3028 100%);
  }
  .cluster-name {
      font-size: 0.92rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .cluster-rate {
      font-size: 1.5rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .cluster-size {
      font-size: 0.75rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
  }
  .cluster-desc {
      font-size: 0.8rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.5;
      margin-bottom: 8px;
  }
  .cluster-action {
      font-size: 0.74rem;
      color: #F5EEDD;
      background: #4A3F35;
      border: 1px solid #7A6E60;
      border-radius: 6px;
      padding: 4px 8px;
      display: inline-block;
  }

  /* ── Model comparison cards ── */
  .model-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
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
  .model-score {
      font-size: 1.6rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .model-note {
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

  /* ── Finding cards ── */
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
  .finding-stat {
      font-size: 1.1rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 3px;
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

  /* ── App pages grid ── */
  .pages-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 1rem;
  }
  .page-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 0.85rem 1rem;
  }
  .page-icon {
      font-size: 1.2rem;
      margin-bottom: 5px;
  }
  .page-name {
      font-size: 0.83rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 3px;
  }
  .page-desc {
      font-size: 0.76rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.45;
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
<div class="page-title">UCI Bank Marketing — MSBA Capstone</div>
<div class="page-subtitle">Customer Segmentation &amp; Term Deposit Subscription Prediction · End-to-End ML Pipeline</div>
<div style="margin-bottom: 0.9rem;">
  <span class="tag">Python</span>
  <span class="tag">XGBoost</span>
  <span class="tag">Agglomerative Clustering</span>
  <span class="tag">scikit-learn</span>
  <span class="tag">PR-AUC</span>
  <span class="tag">Streamlit</span>
  <span class="tag tag-accent">Live App</span>
</div>
<div class="cta-row">
  <a class="cta-btn cta-primary" href="https://msba-capstone-project.streamlit.app/" target="_blank">&#9654; Try the Live Demo</a>
  <a class="cta-btn cta-secondary" href="https://github.com/Brandon-m-Y" target="_blank">View on GitHub</a>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── Stat cards ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-number">41,188</div>
    <div class="stat-label">Dataset Records</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">0.8522</div>
    <div class="stat-label">XGBoost PR-AUC</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">3</div>
    <div class="stat-label">Customer Segments</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">6</div>
    <div class="stat-label">Dashboard Pages</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Business Problem ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
  <div class="section-title">Business Problem</div>
  <p class="section-body">
    Portuguese banks run outbound telemarketing campaigns to sell term deposit subscriptions —
    a critical revenue product with a natural conversion rate of roughly 11%. Calling every
    customer is expensive and risks churn, yet there is no cost-effective way to know in advance
    who will subscribe. This creates a classic resource allocation problem.
    <br><br>
    This project answers two strategic questions simultaneously:
    <strong style="color:#F5EEDD;">Who is most likely to subscribe?</strong> — a tuned XGBoost
    classifier predicts individual subscription probability so campaign resources concentrate on
    high-yield prospects. And:
    <strong style="color:#F5EEDD;">What kinds of customers exist?</strong> — agglomerative
    clustering segments the base into three behaviorally distinct groups with different conversion
    rates, call-duration profiles, and macroeconomic sensitivity. The result is a six-page
    Streamlit dashboard combining interactive EDA, cluster profiling, and real-time model scoring.
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
      <div class="step-title">Business Understanding &amp; Data Acquisition</div>
      <p class="step-body">Framed the problem as imbalanced binary classification and selected
      PR-AUC as the primary evaluation metric — superior to accuracy or ROC-AUC when the positive
      class is rare (11.3%). The full 41,188-record dataset was loaded without prior filtering
      to preserve maximum signal before any analytical decisions.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 2</div>
    <div>
      <div class="step-title">Data Cleaning &amp; Feature Engineering</div>
      <p class="step-body">Renamed all 21 columns to descriptive snake-case equivalents.
      Dropped rows with unknown job, marital, or loan values (total ~3.4%). Mode-imputed
      education within job groups. Engineered three binary indicators: was_previously_contacted,
      positive_campaign_result, and default_status_known. Dropped five multicollinear/redundant
      columns. Net: 39,803 rows x 22 columns.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 3</div>
    <div>
      <div class="step-title">Exploratory Data Analysis (EDA)</div>
      <p class="step-body">Three-axis EDA across univariate distributions, bivariate target
      relationships, and multivariate interactions. Key findings: students and retired customers
      convert at the highest rates by job; Q4 and early-year contacts convert far better than
      mid-year bulk outreach; cellular contact significantly outperforms telephone; Euribor
      rate is the strongest macro-level predictor of subscription.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 4</div>
    <div>
      <div class="step-title">Preprocessing &amp; Clustering Pipeline</div>
      <p class="step-body">Built a ColumnTransformer pipeline with StandardScaler for 9 numeric
      features and OneHotEncoder for 8 categorical features. Applied PCA (10 components) to
      reduce dimensionality before clustering. Evaluated K-Means and Agglomerative Clustering
      across multiple k values and linkage strategies — selected Ward linkage with k=3 for the
      best balance of silhouette score and business interpretability.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 5</div>
    <div>
      <div class="step-title">Cluster Analysis &amp; Interpretation</div>
      <p class="step-body">Profiled all three segments across numeric means, categorical
      distributions, and conversion rates. Euribor 3-month rate emerged as the dominant
      cluster separator. Cluster 1 (Engaged Long-Callers) achieved the highest conversion
      at 36.67% with average call duration of 376 seconds. Cluster 2 (Cold Prospects, 65% of
      population) had zero conversions — all contacted during high-Euribor periods.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 6</div>
    <div>
      <div class="step-title">Classification Modeling</div>
      <p class="step-body">Benchmarked three classifiers — SVM (baseline), Random Forest, and
      XGBoost — using the same ColumnTransformer preprocessing pipeline. Excluded
      last_contact_duration_sec to prevent data leakage (only observable post-call). Handled
      class imbalance via class weighting throughout: class_weight='balanced' for Random Forest
      and scale_pos_weight (~7.8) for XGBoost.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 7</div>
    <div>
      <div class="step-title">Model Evaluation &amp; Selection</div>
      <p class="step-body">Tuned Random Forest and XGBoost with RandomizedSearchCV (40 iterations,
      5-fold stratified CV, optimizing average_precision). XGBoost selected at PR-AUC 0.8522 vs.
      Random Forest's 0.8277 — also faster inference and native imbalance handling via
      scale_pos_weight. Full sklearn Pipeline saved as tuned_xgboost_model.pkl for consistent
      train/serve transformation.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">STEP 8</div>
    <div>
      <div class="step-title">Streamlit Application</div>
      <p class="step-body">Six-page dashboard with interactive EDA, cluster profiling, and
      real-time model scoring. The prediction page collects 16 applicant inputs, passes them
      through the saved pipeline, and returns a binary subscription prediction with confidence
      probability — color-coded green for positive, red for negative. No manual preprocessing
      required at inference time.</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Cluster Profiles ─────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Customer Segment Profiles</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cluster-grid">

  <div class="cluster-card">
    <div class="cluster-name">Cluster 0 — Repeat Responders</div>
    <div class="cluster-rate">26.43%</div>
    <div class="cluster-size">13.65% of customer base (5,433 records)</div>
    <p class="cluster-desc">All records carry a positive prior campaign result. Euribor rate is low
    (1.50), placing contacts in a favorable interest rate environment. These are warm leads —
    previously engaged and proven responsive. Call duration is moderate.</p>
    <span class="cluster-action">Warm re-engagement &amp; cross-sell</span>
  </div>

  <div class="cluster-card top">
    <div class="cluster-name">Cluster 1 — Engaged Long-Callers &#9733;</div>
    <div class="cluster-rate">36.67%</div>
    <div class="cluster-size">20.90% of customer base (8,320 records) — highest value</div>
    <p class="cluster-desc">Never previously contacted, yet the highest-converting segment.
    Average call duration of 376 seconds — the longest of all clusters. Euribor is low (1.83)
    and 85.8% use cellular contact. Single well-executed conversations are highly effective here.</p>
    <span class="cluster-action">Invest in call quality — cellular first</span>
  </div>

  <div class="cluster-card">
    <div class="cluster-name">Cluster 2 — Cold Prospects</div>
    <div class="cluster-rate">0.00%</div>
    <div class="cluster-size">65.45% of customer base (26,050 records)</div>
    <p class="cluster-desc">The largest segment with zero conversions. Never previously contacted
    and experienced significantly higher Euribor rates (4.63) — contacts fell during an
    economically unfavorable period for term deposits. Call duration is the shortest across
    all clusters (median ~162 sec).</p>
    <span class="cluster-action">Deprioritize — re-activate when rates fall</span>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Model Comparison ──────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Model Benchmark Results (PR-AUC)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="model-grid">

  <div class="model-card">
    <div class="model-name">SVM (RBF Kernel)</div>
    <div class="model-score">Baseline</div>
    <p class="model-note">class_weight='balanced' · C=1.0 · probability=True<br>
    Outperformed by both ensemble methods on this tabular dataset.</p>
  </div>

  <div class="model-card">
    <div class="model-name">Tuned Random Forest</div>
    <div class="model-score">0.8277</div>
    <p class="model-note">n_estimators=600 · max_depth=25 · class_weight='balanced_subsample'<br>
    Competitive but slower inference; slightly higher false negative rate.</p>
  </div>

  <div class="model-card winner">
    <div class="winner-badge">&#9733; WINNER</div>
    <div class="model-name">Tuned XGBoost</div>
    <div class="model-score">0.8522</div>
    <p class="model-note">n_estimators=500 · max_depth=4 · lr=0.05 · scale_pos_weight=1<br>
    Best PR-AUC + fastest inference + native imbalance handling.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Key Business Findings ─────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Key Business Takeaways</div>', unsafe_allow_html=True)

st.markdown("""
<div class="finding-grid">

  <div class="finding-card">
    <div class="finding-stat">Euribor Rate</div>
    <div class="finding-title">Strongest Macro-Level Predictor</div>
    <p class="finding-body">Term deposits are most attractive when rates are low (~1.5–2%).
    Campaigns during high-rate periods (Euribor > 4%) are nearly ineffective — evidenced by
    Cluster 2's zero conversion rate. Timing campaigns around macroeconomic conditions alone
    could dramatically improve ROI.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">376 sec avg call</div>
    <div class="finding-title">Call Quality Beats Call Quantity</div>
    <p class="finding-body">Cluster 1's 376-second average duration paired with 36.67%
    conversion demonstrates that longer, more engaging conversations convert far better.
    Subscribers also receive fewer repeat contacts on average, suggesting over-contacting
    reduces conversion odds.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">Cellular wins</div>
    <div class="finding-title">Channel Prioritization Signal</div>
    <p class="finding-body">Cellular contact achieves significantly higher subscription rates
    than telephone across the dataset and within high-conversion clusters. 85.8% of Cluster 1
    — the highest-converting segment — uses cellular contact, making channel selection an
    actionable pre-call filter.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">34% of contacts</div>
    <div class="finding-title">Campaign Concentration Opportunity</div>
    <p class="finding-body">Concentrating campaign effort on Clusters 0 and 1 — just 34% of
    the full contact list — would capture nearly all subscriptions. This enables dramatic
    improvement in campaign ROI without sacrificing reach, making segmentation the single
    highest-leverage operational decision.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">Students &amp; Retirees</div>
    <div class="finding-title">Highest-Converting Job Categories</div>
    <p class="finding-body">Students and retired customers convert at disproportionately high
    rates relative to their share of contact volume. Blue-collar workers are the hardest segment
    to convert. Q4 and early-year contacts consistently outperform mid-year bulk outreach —
    aligned with year-end financial planning behavior.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">PR-AUC 0.8522</div>
    <div class="finding-title">Meaningful Improvement Over Random Selection</div>
    <p class="finding-body">A PR-AUC of 0.8522 against a random baseline of 0.113 (the positive
    class rate) confirms the model provides strong discriminative power. Using the model for
    pre-call scoring means campaign managers can concentrate on the highest-probability
    prospects rather than contacting the full 41,188-record list.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── App Pages ─────────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Dashboard Pages</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pages-grid">
  <div class="page-card">
    <div class="page-icon">🏠</div>
    <div class="page-name">Home</div>
    <p class="page-desc">Project overview, dataset summary, and navigation guide.</p>
  </div>
  <div class="page-card">
    <div class="page-icon">📊</div>
    <div class="page-name">General Analysis</div>
    <p class="page-desc">Interactive EDA — subscription rates, distributions, correlations, and lift charts by job, education, and contact timing.</p>
  </div>
  <div class="page-card">
    <div class="page-icon">🔵</div>
    <div class="page-name">Segmentation Analysis</div>
    <p class="page-desc">Cluster profiles — conversion rates, Euribor by segment, call duration, and categorical breakdowns per cluster.</p>
  </div>
  <div class="page-card">
    <div class="page-icon">🤖</div>
    <div class="page-name">Model Prediction</div>
    <p class="page-desc">Real-time single-customer scoring. Enter 16 features and receive a subscription probability with color-coded output.</p>
  </div>
  <div class="page-card">
    <div class="page-icon">📋</div>
    <div class="page-name">Model Assumptions</div>
    <p class="page-desc">Model documentation, evaluation metrics, tuning rationale, feature leakage decisions, and known limitations.</p>
  </div>
  <div class="page-card">
    <div class="page-icon">📖</div>
    <div class="page-name">About the Data</div>
    <p class="page-desc">Dataset description, full feature definitions, cleaning decisions, and UCI citation information.</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Technical Deep Dives ─────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

with st.expander("Clustering Algorithm Selection", expanded=False):
    st.markdown("""
Both K-Means and Agglomerative Clustering were evaluated across multiple k values and
linkage strategies. Average linkage with k=2 produced the highest silhouette score (0.7176)
but collapsed customers into two overly broad groups with limited business utility.
Ward linkage with k=3 was selected for the best balance of cluster separation and marketing granularity.

| Algorithm | k | Linkage | Silhouette Score |
|---|---|---|---|
| K-Means | 4 | — | 0.1932 |
| Agglomerative | 2 | Average | 0.7176 |
| Agglomerative | 3 | Average | 0.5316 |
| **Agglomerative** | **3** | **Ward** | **0.2589** ✓ |
""")
    st.code("""from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_cols)
])

X_scaled = preprocessor.fit_transform(df)
X_pca    = PCA(n_components=10).fit_transform(X_scaled)

model = AgglomerativeClustering(n_clusters=3, linkage='ward')
df['cluster'] = model.fit_predict(X_pca)""", language="python")

with st.expander("XGBoost Tuning — Best Hyperparameters", expanded=False):
    st.markdown("""
Tuned with RandomizedSearchCV (40 iterations, 5-fold stratified CV, optimizing
`average_precision`). Key configuration choices: shallow trees (`max_depth=4`) prevent
overfitting on the engineered feature set; aggressive subsampling provides stochastic
regularization; `scale_pos_weight=1` paired with `gamma` and `min_child_weight` handles
the 88.7/11.3% class split.
""")
    st.code("""from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline

xgb_best_params = {
    'n_estimators':     500,
    'max_depth':        4,
    'learning_rate':    0.05,
    'subsample':        0.85,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'gamma':            0.2,
    'scale_pos_weight': 1,
}

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier',   XGBClassifier(**xgb_best_params, random_state=42))
])

pipeline.fit(X_train, y_train)

import joblib
joblib.dump(pipeline, 'Models/tuned_xgboost_model.pkl')""", language="python")

with st.expander("Data Cleaning — Feature Engineering Decisions", expanded=False):
    st.markdown("""
**Three binary indicators engineered before any feature drops:**

| New Feature | Logic | % Positive |
|---|---|---|
| `was_previously_contacted` | 1 if contacted in a prior campaign | 3.7% |
| `positive_campaign_result` | 1 if prior campaign resulted in subscription | 13.6% |
| `default_status_known` | 1 if default status is explicitly known | ~79% |

**Five columns dropped for redundancy or multicollinearity:**

| Column | Reason |
|---|---|
| `days_since_prev_campaign_contact` | 96.3% are value 999 — captured by `was_previously_contacted` |
| `previous_campaign_result` | 86.4% "nonexistent" — redundant with `positive_campaign_result` |
| `employment_variation_rate` | Highly multicollinear with Euribor and other macro indicators |
| `num_employees` | Highly multicollinear with `employment_variation_rate` |
| `consumer_price_index` | Highly multicollinear with other macro indicators |

**`last_contact_duration_sec` excluded from classification** — strong predictor but only
observable after a call occurs. Including it would constitute data leakage in a pre-call
scoring system.
""")

with st.expander("Repository Structure", expanded=False):
    st.markdown("""
| File / Folder | Role |
|---|---|
| `1_UCI_Data_Cleaning.ipynb` | Column renaming, unknown handling, feature engineering, multicollinear drops |
| `2_EDA.ipynb` | Exploratory analysis — distributions, lift charts, correlations |
| `3_Preprocessing_Clustering.ipynb` | ColumnTransformer pipeline, PCA, agglomerative clustering |
| `4_Clustering_Analysis.ipynb` | Cluster profiling and business interpretation |
| `5_Classification.ipynb` | Model training, tuning, evaluation |
| `Models/preprocessing_pipeline.pkl` | StandardScaler + OneHotEncoder pipeline |
| `Models/pca.pkl` | PCA transformer (10 components) |
| `Models/agglomerative_model.pkl` | Ward-linkage k=3 clustering model |
| `Models/tuned_xgboost_model.pkl` | Full sklearn Pipeline — preprocessing + classifier |
| `Streamlit_App/app.py` | Multi-page dashboard entry point |
""")

# ── CTA Footer ────────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
  <div>
    <div style="font-size: 1rem; font-weight: 600; color: #F5EEDD; margin-bottom: 4px;">
      Explore the live dashboard
    </div>
    <div class="secondary-text" style="font-size: 0.9rem;">
      Interactive EDA, cluster profiling, and real-time subscription scoring — all in one app.
    </div>
  </div>
  <div class="cta-row" style="margin-top: 0;">
    <a class="cta-btn cta-primary" href="https://msba-capstone-project.streamlit.app/" target="_blank">&#9654; Open Live App</a>
    <a class="cta-btn cta-secondary" href="https://github.com/Brandon-m-Y" target="_blank">View Source</a>
  </div>
</div>
""", unsafe_allow_html=True)
