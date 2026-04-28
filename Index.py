import streamlit as st
import numpy as np
import plotly.graph_objects as go

# 1. إعداد الصفحة وتغيير الثيم للأسود الاحترافي
st.set_page_config(page_title="IF Simulator Pro", layout="wide")

# 2. إضافة CSS لتجميل الخطوط والأزرار
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .main { background-color: #0e1117; }
    .title-text {
        font-family: 'Orbitron', sans-serif;
        color: #00FBFF;
        text-align: center;
        text-shadow: 0px 0px 10px #00FBFF;
        font-size: 3rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #00FBFF;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        height: 3em;
    }
    .stNumberInput label { color: #00FBFF !important; font-size: 1.2rem; }
    </style>
    <h1 class="title-text">IFT DIGITAL INTERFACE</h1>
    """, unsafe_allow_html=True)

# 3. تنظيم العناصر في أعمدة (Layout)
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### ⚙️ PARAMETERS")
    # مدخلات الأرقام بشكل منظم
    base_f =
