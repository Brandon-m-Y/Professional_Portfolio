import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Brandon Ytuarte",
    page_icon="images/BMY_Logo_cropped 2.jpg",
    layout="wide",
)

# ── Force dark background + global styles ─────────────────────────────────────
st.markdown("""
<style>
  /* Page background */
  [data-testid="stAppViewContainer"] {
      background: radial-gradient(circle at top left, #3A3A3A 0%, #2F2F2F 45%, #242424 100%);
  }
  [data-testid="stHeader"] {
      background-color: #2B2B2B;
  }
  [data-testid="stSidebar"] {
      background-color: #262626;
  }

  /* Hide Streamlit default top padding */
  .block-container {
      padding-top: 2.5rem;
      padding-bottom: 3rem;
      max-width: 1200px;
      padding-left: 2.5rem;
      padding-right: 2.5rem;
  }

  /* Base text */
  html, body, [class*="css"] {
      color: #F5EEDD;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }
  /* Keep bio text readable in both light/dark themes */
  [data-testid="stMarkdownContainer"] .bio-text {
      color: #F5EEDD !important;
  }
  .bio-text {
      font-size: 16px;
      color: #F5EEDD !important;
      line-height: 1.8;
      margin: 0 0 0.25rem;
  }
  .secondary-text {
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
  }

  /* ── Avatar ── */
  .avatar {
      width: 90px;
      height: 90px;
      border-radius: 50%;
      background-color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      font-weight: 600;
      color:#FFFFFF;
      flex-shrink: 0;
  }

  /* ── Skill / tag pills ── */
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
  .tag-status {
      background: #4A4A4A;
      border-color: #8A8073;
      color: #F5EEDD;
  }

  /* ── Stat cards ── */
  .stat-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin: 1.5rem 0;
  }
  .stat-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1.25rem 1.25rem 1rem;
  }
  .stat-number {
      font-size: 26px;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 4px;
  }
  .stat-label {
      font-size: 14px;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
  }

  /* ── Section label ── */
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

  /* ── Project cards ── */
  .project-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 1.5rem;
  }
  .project-card {
      background: linear-gradient(145deg, #3F3F3F 0%, #343434 100%);
      border: 1px solid #5A5349;
      border-radius: 12px;
      padding: 1.1rem 1.25rem;
  }
  .project-title {
      font-size: 15px;
      font-weight: 600;
      color: #F5EEDD;
      margin-bottom: 6px;
  }
  .project-desc {
      font-size: 13px;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      line-height: 1.6;
      margin-bottom: 10px;
  }

  /* ── Divider ── */
  .divider {
      border: none;
      border-top: 1px solid #5A5349;
      margin: 1.5rem 0;
  }

  /* ── Links section ── */
  .link-row {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 14px;
      background: linear-gradient(180deg, #A39A88 0%, #756E61 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent !important;
      -webkit-text-fill-color: transparent;
      padding: 8px 0;
      border-bottom: 1px solid #4C463E;
      text-decoration: none;
  }
  .link-row:last-child { border-bottom: none; }
  .link-icon { color: #8A8073 !important; flex-shrink: 0; }
</style>
""", unsafe_allow_html=True)


import base64

def get_img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_img_base64("images/LinkedIn_Picture.jpg")

# ── Hero: avatar + name + tags ─────────────────────────────────────────────────
st.markdown(f"""
<div style="display: flex; align-items: flex-start; gap: 1.5rem; padding-bottom: 1.5rem;">
  <img src="data:image/jpeg;base64,{img}"
       style="border-radius:50%; width:90px; height:90px; object-fit:cover; flex-shrink:0;">
  <div style="padding-top: 6px;">
    <div style="font-size: 28px; font-weight: 700; color: #F5EEDD; margin-bottom: 4px;">
      Brandon Ytuarte
    </div>
    <div class="secondary-text" style="font-size: 16px; margin-bottom: 14px;">
      Data Scientist &amp; Business Analyst
    </div>
    <div>
      <span class="tag">Python</span>
      <span class="tag">Machine Learning</span>
      <span class="tag">Data Science</span>
      <span class="tag tag-status">Data Analytics</span>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── Bio ────────────────────────────────────────────────────────────────────────
st.markdown("""
<p class="bio-text">

My name is Brandon Ytuarte. I am passionate about data science and analytics, and I love building data-driven solutions that help businesses unlock the full potential of their data.
            
My journey began with a strong foundation in business strategy, which gave me a broad understanding of how organizations operate. Over time, I’ve shifted my focus toward mining data for actionable, specific insights. 

This path has been incredibly rewarding, and I am thrilled to be completing my Master of Science in Business Analytics (MSBA) — graduating in just three weeks.

My expertise lies in data science, machine learning, and advanced analytics, with a growing specialization in marketing analytics. 
Through my upcoming Marketing Analytics internship, I am excited to make my official pivot into the analytics industry.

This professional portfolio showcases the projects I’m most proud of — each one reflecting my technical skills, analytical thinking, and ability to deliver meaningful business value through data.
I thrive on continuous learning and tackling complex challenges, and I’m genuinely excited for the next chapter in my analytics career.

</p>
""", unsafe_allow_html=True)


# ── Stat cards ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-number">12</div>
    <div class="stat-label">Projects</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">3</div>
    <div class="stat-label">Years experience</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">∞</div>
    <div class="stat-label">Curiosity</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Featured projects ──────────────────────────────────────────────────────────
st.markdown("""
<div class="section-label">Featured Projects</div>
<div class="project-grid">
  <div class="project-card">
    <div class="project-title">MSBA Capstone Project</div>
    <div class="project-desc">
      End-to-end data analysis project, marketing segmentation, and
            classification using the Bank Marketing data set from UCI ML Repository.
    </div>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Python</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">ML</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Agglomerative Clustering</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Streamlit</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Classification</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Hyper-Parameter Tuning</span>
  </div>
            
  <div class="project-card">
    <div class="project-title">Project 3 Placeholder</div>
    <div class="project-desc">
      End-to-end data analysis project, marketing segmentation, and
            classification using the Bank Marketing data set from UCI ML Repository.
    </div>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Python</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">ML</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Agglomerative Clustering</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Streamlit</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Classification</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Hyper-Parameter Tuning</span>
  </div>         
  
  <div class="project-card">
    <div class="project-title">Marketing Segmentation App</div>
    <div class="project-desc">
      Interactive Streamlit application for real-time data analysis and marketing segmentation.
    </div>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Python</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">ML</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Kmeans</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Streamlit</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Data Analysis</span>
  </div>
            
  <div class="project-card">
    <div class="project-title">Project 4 Placeholder</div>
    <div class="project-desc">
      Interactive Streamlit application for real-time data analysis and marketing segmentation.
    </div>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Python</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">ML</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Kmeans</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Streamlit</span>
    <span class="tag" style="font-size:12px; padding:3px 10px;">Data Analysis</span>
  </div>          
</div>

<hr class="divider">
""", unsafe_allow_html=True)


# ── Links ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-label">Find me online</div>

<a class="link-row" href="https://github.com/Brandon-m-Y" target="_blank">
  <svg class="link-icon" width="16" height="16" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="2">
    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61
             c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77
             A5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48
             a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1
             A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78
             c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
  </svg>
  github.com/brandonytuarte
</a>

<a class="link-row" href="https://www.linkedin.com/in/brandon-m-ytuarte/" target="_blank">
  <svg class="link-icon" width="16" height="16" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="2">
    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2
             2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
    <rect x="2" y="9" width="4" height="12"/>
    <circle cx="4" cy="4" r="2"/>
  </svg>
  linkedin.com/in/brandonytuarte
</a>
""", unsafe_allow_html=True)