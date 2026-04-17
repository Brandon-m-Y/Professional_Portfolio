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
      padding-bottom: 2.5rem;
      max-width: 1200px;
      padding-left: 2.5rem;
      padding-right: 2.5rem;
  }

  html, body, [class*="css"] {
      color: #F5EEDD;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .page-title {
      font-size: 2rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 0.4rem;
  }
  .page-subtitle {
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      margin-bottom: 1rem;
      font-size: 1rem;
  }
  .divider {
      border: none;
      border-top: 1px solid #5A5349;
      margin: 1rem 0 1.4rem 0;
  }
  .section-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1rem 1.1rem;
      margin-bottom: 0.85rem;
      width: 100%;
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
      line-height: 1.65;
      margin: 0;
  }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-title">Project 3</div>
<div class="page-subtitle">Project overview and impact narrative</div>
<hr class="divider">
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">
  <div class="section-title">Business Problem</div>
  <p class="section-body">Define the core business challenge, why it matters now, and which stakeholders are impacted.</p>
</div>
<div class="section-card">
  <div class="section-title">Technical Approach (Data Science/ML Techniques)</div>
  <p class="section-body">Summarize data preparation, modeling techniques, evaluation methods, and tools used to solve the problem.</p>
</div>
<div class="section-card">
  <div class="section-title">Key Insights</div>
  <p class="section-body">Highlight the most important findings, patterns, and model outputs that informed decision-making.</p>
</div>
<div class="section-card">
  <div class="section-title">Business Value Delivered</div>
  <p class="section-body">Explain measurable outcomes, expected ROI, and how recommendations drive practical business impact.</p>
</div>
""", unsafe_allow_html=True)

if st.button("Click Me for Balloons!"):
    st.success("Woohoo")
    st.balloons()
