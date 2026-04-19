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

  /* ── Analysis question cards (workflow) ── */
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

  /* ── Role skill cards ── */
  .role-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 1rem;
  }
  .role-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1rem 1.1rem;
  }
  .role-title {
      font-size: 0.92rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 8px;
  }
  .skill-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 4px 0;
      border-bottom: 1px solid #4A4440;
  }
  .skill-row:last-child { border-bottom: none; }
  .skill-name {
      font-size: 0.8rem;
      color: #F5EEDD;
  }
  .skill-pct {
      font-size: 0.75rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
  }
  .skill-bar-bg {
      width: 100%;
      background: #3A3530;
      border-radius: 4px;
      height: 5px;
      margin-top: 3px;
      margin-bottom: 4px;
  }
  .skill-bar-fill {
      height: 5px;
      border-radius: 4px;
      background: linear-gradient(90deg, #8A7A6A, #A39A88);
  }

  /* ── Insight finding cards ── */
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

  /* ── Salary tier cards ── */
  .salary-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 1rem;
  }
  .salary-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 0.9rem 1rem;
      text-align: center;
  }
  .salary-role {
      font-size: 0.82rem;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 5px;
  }
  .salary-amount {
      font-size: 1.4rem;
      font-weight: 700;
      color: #F5EEDD;
      margin-bottom: 3px;
  }
  .salary-note {
      font-size: 0.72rem;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.4;
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
<div class="page-title">Python Data Job Market Analysis</div>
<div class="page-subtitle">Skill demand, salary trends, and optimal learning paths for data roles in the US — 2023</div>
<div style="margin-bottom: 0.9rem;">
  <span class="tag">Python</span>
  <span class="tag">pandas</span>
  <span class="tag">matplotlib</span>
  <span class="tag">seaborn</span>
  <span class="tag">EDA</span>
  <span class="tag">Labor Market Analysis</span>
  <span class="tag tag-accent">Jupyter Notebook</span>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── Stat cards ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-number">4</div>
    <div class="stat-label">Analysis Questions</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">3</div>
    <div class="stat-label">Data Roles Compared</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">$600K</div>
    <div class="stat-label">Peak Salary Potential</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">2023</div>
    <div class="stat-label">US Job Postings Dataset</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Business Problem ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
  <div class="section-title">Business Problem</div>
  <p class="section-body">
    Breaking into or advancing within data analytics requires more than generic career advice —
    it demands evidence. Which skills actually appear in job postings? Do the skills employers
    ask for most also pay the best, or is there a tradeoff between demand and compensation?
    And how do those answers differ across Data Analysts, Data Scientists, and Data Engineers?
    <br><br>
    This project applies Python-based data analysis to a real dataset of US job postings from
    2023 to answer four concrete questions that directly shape career and learning decisions
    for anyone targeting the data field. The output is a structured set of visualizations and
    insights that cut through noise and identify where skill investment has the highest return.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Four Analysis Questions ───────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">The Four Analysis Questions</div>', unsafe_allow_html=True)

st.markdown("""
<div class="workflow-grid">

  <div class="workflow-card">
    <div class="step-badge">Q1</div>
    <div>
      <div class="step-title">What are the most demanded skills for the top 3 data roles?</div>
      <p class="step-body">Filtered job postings to the three most popular data role titles, then
      ranked the top five skills by mention count for each. The output reveals which skills are
      role-specific versus universal, and where to focus depending on the job target.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">Q2</div>
    <div>
      <div class="step-title">How are in-demand skills trending for Data Analysts in 2023?</div>
      <p class="step-body">Computed monthly skill mention percentages across 2023 job postings and
      plotted trend lines for the top five Data Analyst skills. Captures how the market shifted
      across the year — which skills grew, which plateaued, and which declined.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">Q3</div>
    <div>
      <div class="step-title">How well do jobs and skills pay for Data Analysts?</div>
      <p class="step-body">Built salary distribution box plots for the top 6 data job titles and
      dual bar charts comparing the top 10 highest-paid skills versus the top 10 most in-demand
      skills for Data Analysts — exposing the gap between what pays and what employers ask for.</p>
    </div>
  </div>

  <div class="workflow-card">
    <div class="step-badge">Q4</div>
    <div>
      <div class="step-title">What are the most optimal skills to learn for Data Analysts?</div>
      <p class="step-body">Mapped skills onto a scatter plot with demand (% of job postings) on
      the x-axis and median salary on the y-axis, color-coded by technology category. Identifies
      the sweet spot of high-demand and high-compensation — the optimal learning targets.</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Top Skills by Role ────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Top 5 Skills by Data Role — Q1 Results</div>', unsafe_allow_html=True)

st.markdown("""
<div class="role-grid">

  <div class="role-card">
    <div class="role-title">Data Analyst</div>
    <div class="skill-row">
      <span class="skill-name">SQL</span>
      <span class="skill-pct">51%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:51%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Excel</span>
      <span class="skill-pct">41%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:41%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Tableau</span>
      <span class="skill-pct">28%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:28%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Python</span>
      <span class="skill-pct">27%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:27%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Power BI</span>
      <span class="skill-pct">20%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:20%"></div></div>
  </div>

  <div class="role-card">
    <div class="role-title">Data Scientist</div>
    <div class="skill-row">
      <span class="skill-name">Python</span>
      <span class="skill-pct">72%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:72%"></div></div>
    <div class="skill-row">
      <span class="skill-name">SQL</span>
      <span class="skill-pct">51%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:51%"></div></div>
    <div class="skill-row">
      <span class="skill-name">R</span>
      <span class="skill-pct">44%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:44%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Tableau</span>
      <span class="skill-pct">24%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:24%"></div></div>
    <div class="skill-row">
      <span class="skill-name">SAS</span>
      <span class="skill-pct">24%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:24%"></div></div>
  </div>

  <div class="role-card">
    <div class="role-title">Data Engineer</div>
    <div class="skill-row">
      <span class="skill-name">SQL</span>
      <span class="skill-pct">68%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:68%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Python</span>
      <span class="skill-pct">65%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:65%"></div></div>
    <div class="skill-row">
      <span class="skill-name">AWS</span>
      <span class="skill-pct">43%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:43%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Azure</span>
      <span class="skill-pct">32%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:32%"></div></div>
    <div class="skill-row">
      <span class="skill-name">Spark</span>
      <span class="skill-pct">32%</span>
    </div>
    <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:32%"></div></div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Skill Trend Insights (Q2) ─────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">2023 Skill Trend Insights — Q2 Results</div>', unsafe_allow_html=True)

st.markdown("""
<div class="finding-grid">

  <div class="finding-card">
    <div class="finding-stat">SQL — #1 All Year</div>
    <div class="finding-title">Most Consistent Demand</div>
    <p class="finding-body">SQL remained the most consistently demanded skill for Data Analysts
    throughout 2023, though it showed a gradual decrease in mention rate across the year —
    suggesting slow diversification of tooling expectations in the market.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">Excel — Late Surge</div>
    <div class="finding-title">Significant September Spike</div>
    <p class="finding-body">Excel experienced a significant increase in demand starting around
    September, surpassing both Python and Tableau by year's end. This signals that foundational
    spreadsheet skills remain deeply embedded in hiring expectations, especially in non-tech industries.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">Python &amp; Tableau</div>
    <div class="finding-title">Stable but Essential</div>
    <p class="finding-body">Both Python and Tableau showed relatively stable demand throughout
    the year with some fluctuations. Their persistence in the top 5 confirms they are
    non-negotiable skills for Data Analysts, even as their relative ranking shifts seasonally.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">Power BI — Rising</div>
    <div class="finding-title">Upward Trend Toward Year End</div>
    <p class="finding-body">Power BI, while less demanded than SQL or Excel, showed a slight
    upward trend toward the end of 2023. Its growth reflects increasing adoption of Microsoft
    BI tooling in enterprise environments as an alternative to Tableau.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Salary Tiers (Q3) ────────────────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Salary Distributions by Role — Q3 Results</div>', unsafe_allow_html=True)

st.markdown("""
<div class="salary-grid">

  <div class="salary-card">
    <div class="salary-role">Senior Data Scientist</div>
    <div class="salary-amount">Up to $600K</div>
    <p class="salary-note">Highest salary ceiling of all data roles. Considerable outliers
    on the high end reflecting premium for advanced ML expertise.</p>
  </div>

  <div class="salary-card">
    <div class="salary-role">Senior Data Engineer</div>
    <div class="salary-amount">Up to $375K</div>
    <p class="salary-note">High-end outliers driven by cloud infrastructure and big data
    specializations. Median well above analyst-track roles.</p>
  </div>

  <div class="salary-card">
    <div class="salary-role">Data Scientist</div>
    <div class="salary-amount">~$120–160K</div>
    <p class="salary-note">Broad salary range reflecting wide variance in role scope.
    Seniority and specialization drive significant spread.</p>
  </div>

  <div class="salary-card">
    <div class="salary-role">Data Engineer</div>
    <div class="salary-amount">~$110–150K</div>
    <p class="salary-note">Consistent demand for cloud and pipeline skills keeps median
    salaries firmly above analyst-level compensation.</p>
  </div>

  <div class="salary-card">
    <div class="salary-role">Data Analyst</div>
    <div class="salary-amount">~$65–95K</div>
    <p class="salary-note">Most consistent salary range with fewer outliers. Entry point
    of the data career ladder with clearest skill-to-hire mapping.</p>
  </div>

  <div class="salary-card">
    <div class="salary-role">Highest Paid Skill</div>
    <div class="salary-amount">$200K (dplyr)</div>
    <p class="salary-note">Specialized technical skills — dplyr, Bitbucket, GitLab —
    command premium pay far above high-demand foundational tools.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Optimal Skills Insights (Q4) ─────────────────────────────────────────────────
st.markdown('<hr class="divider"><div class="section-label">Optimal Skills to Learn — Q4 Results</div>', unsafe_allow_html=True)

st.markdown("""
<div class="finding-grid">

  <div class="finding-card">
    <div class="finding-stat">Programming Skills</div>
    <div class="finding-title">Highest Salary Ceiling</div>
    <p class="finding-body">Programming skills (Python, R) cluster at higher salary levels
    compared to other technology categories in the scatter plot, indicating that programming
    expertise offers greater salary upside within the data analytics field.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">Database Skills</div>
    <div class="finding-title">High Pay + Solid Demand</div>
    <p class="finding-body">Oracle and SQL Server are associated with some of the highest
    Data Analyst salaries while maintaining meaningful demand. Database expertise signals
    a level of technical depth that commands a pay premium over general analyst skills.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">Analyst Tools</div>
    <div class="finding-title">Widest Job Market Coverage</div>
    <p class="finding-body">Tableau and Power BI are prevalent across job postings and
    offer competitive salaries. This category is versatile across different types of
    data tasks — the best combination of employability and compensation for most analysts.</p>
  </div>

  <div class="finding-card">
    <div class="finding-stat">The Core Tradeoff</div>
    <div class="finding-title">Demand vs Compensation Gap</div>
    <p class="finding-body">The most in-demand skills (Excel, PowerPoint, SQL) are not
    the highest paid. Data analysts maximizing career potential should build both a
    foundational layer for employability and a specialized layer (Python, cloud, database)
    to push compensation upward.</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Technical Deep Dives ─────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

with st.expander("Q1 — Skill Demand by Role (Code)", expanded=False):
    st.markdown("""
Filtered job postings to the top three role titles, then used a grouped bar chart per role
to show the top five skills by mention count. The loop pattern allows the same logic to
apply cleanly across all three roles without code duplication.
""")
    st.code("""fig, ax = plt.subplots(len(job_titles), 1)

for i, job_title in enumerate(job_titles):
    df_plot = df_skills_count[
        df_skills_count['job_title_short'] == job_title
    ].head(5)

    df_plot.plot(kind='barh', x='job_skills', y='skill_count', ax=ax[i], title=job_title)
    ax[i].invert_yaxis()
    ax[i].set_ylabel('')
    ax[i].legend().set_visible(False)

plt.suptitle('Counts of Top Skills in Data Job Postings', fontsize=15)
plt.tight_layout(h_pad=0.5)
plt.show()""", language="python")

with st.expander("Q2 — Skill Trend Lines Over 2023 (Code)", expanded=False):
    st.markdown("""
Computed monthly skill mention percentages for US Data Analyst postings, then used
seaborn's `lineplot` with direct text labels at each line's endpoint — avoiding a legend
that would clutter the time-series view.
""")
    st.code("""df_plot = df_DA_US_percent.iloc[:, :5]

sns.lineplot(data=df_plot, dashes=False, palette='tab10')
sns.set_theme(style='ticks')
sns.despine()

plt.title('Trending Top Skills for Data Analysts in the US')
plt.ylabel('Likelihood in the Job Posting')
plt.xlabel('2023')
plt.legend().remove()

from matplotlib.ticker import PercentFormatter
ax = plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))

for i in range(5):
    plt.text(11.2, df_plot.iloc[-1, i], df_plot.columns[i])""", language="python")

with st.expander("Q3 — Salary Distributions & Skill Pay (Code)", expanded=False):
    st.markdown("""
Two-panel chart: box plots for salary distributions across the top 6 job titles, and dual
bar charts comparing the 10 highest-paid skills vs. the 10 most in-demand skills for Data
Analysts — both using the same x-axis scale for a direct comparison.
""")
    st.code("""# Salary distributions box plot
sns.boxplot(data=df_US_top6, x='salary_year_avg',
            y='job_title_short', order=job_order)
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}k'))
plt.xlim(0, 600000)

# Highest paid vs most demanded — dual bar chart
fig, ax = plt.subplots(2, 1)

sns.barplot(data=df_DA_top_pay, x='median', y=df_DA_top_pay.index,
            ax=ax[0], hue='median', palette='dark:b_r')
ax[0].set_title("Top 10 Highest Paid Skills for Data Analysts")
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x/1000)}K'))

sns.barplot(data=df_DA_skills, x='median', y=df_DA_skills.index,
            ax=ax[1], hue='median', palette='light:b')
ax[1].set_title('Top 10 Most In-Demand Skills for Data Analysts')
ax[1].set_xlim(ax[0].get_xlim())
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x/1000)}K'))
fig.tight_layout()""", language="python")

with st.expander("Q4 — Optimal Skills Scatter Plot (Code)", expanded=False):
    st.markdown("""
Plotted demand (% of Data Analyst job postings) on the x-axis against median salary on
the y-axis, color-coded by technology category. `adjustText` automatically repositions
skill labels to avoid overlap — critical when many points cluster in the same region.
""")
    st.code("""from adjustText import adjust_text
from matplotlib.ticker import PercentFormatter

sns.scatterplot(data=df_plot, x='skill_percent', y='median_salary', hue='Technology')
sns.despine()
sns.set_theme(style='ticks')

text = []
for i, txt in enumerate(df_DA_skills_high_demand.index):
    text.append(plt.text(
        df_DA_skills_high_demand['skill_percent'].iloc[i],
        df_DA_skills_high_demand['median_salary'].iloc[i],
        txt
    ))

adjust_text(text, arrowprops=dict(arrowstyle="-", color='gray', lw=1.0))

ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}k'))
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))

plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel('Median Yearly Salary ($USD)')
plt.title('Most Optimal Skills for Data Analysts in the US')""", language="python")

with st.expander("Challenges & Lessons Learned", expanded=False):
    st.markdown("""
**Data Inconsistencies** — Handling missing or inconsistent entries across job postings
required careful cleaning decisions before any skill aggregation. Small inconsistencies in
job title strings, for example, had outsized effects on role-level counts.

**Complex Data Visualization** — Designing charts that communicate hierarchy (which skills
rank above others) while also conveying magnitude required iteration. The dual bar chart
for Q3 and the annotated scatter plot for Q4 were particularly involved to get right.

**Balancing Breadth and Depth** — Each of the four questions could justify a full project on its
own. The challenge was deciding where to go deep (skill salary analysis) versus where
a concise summary visualization was sufficient (trend lines), so the overall narrative
stayed coherent.
""")

# ── Overall Conclusions ───────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="section-card">
  <div class="section-title">Overall Insights</div>
  <p class="section-body">
    Skill demand and salary are correlated but not identical. Advanced and specialized skills
    (Python, Oracle, cloud tools) often lead to higher salaries, while foundational skills
    (SQL, Excel) dominate raw job posting counts. The data job market is dynamic — skill
    demand shifted meaningfully even within a single year, making ongoing market literacy
    as important as technical skill itself. Analysts who develop both a strong foundational
    layer and at least one specialized depth area are best positioned for both employment
    and compensation growth.
  </p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="section-card">
  <div class="section-title">Conclusion</div>
  <p class="section-body">
    This exploration into the 2023 US data analyst job market highlights the critical skills
    and compensation dynamics that shape this evolving field. The insights provide actionable
    guidance for anyone targeting a data career: prioritize SQL and Python for broad
    employability, layer in database and cloud skills to push compensation upward, and watch
    visualization tools like Tableau and Power BI for their strong combination of demand
    and salary. As the market continues to evolve, ongoing analysis of job posting data
    will remain essential for staying ahead.
  </p>
</div>
""", unsafe_allow_html=True)

# ── CTA Footer ────────────────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
  <div>
    <div style="font-size: 1rem; font-weight: 600; color: #F5EEDD; margin-bottom: 4px;">
      Explore the full analysis notebook
    </div>
    <div class="secondary-text" style="font-size: 0.9rem;">
      All visualizations, code, and data cleaning steps available on GitHub.
    </div>
  </div>
  <div class="cta-row" style="margin-top: 0;">
    <a class="cta-btn cta-primary" href="https://github.com/Brandon-m-Y" target="_blank">View on GitHub</a>
    <a class="cta-btn cta-secondary" href="https://www.linkedin.com/in/brandon-m-ytuarte/" target="_blank">Connect on LinkedIn</a>
  </div>
</div>
""", unsafe_allow_html=True)
