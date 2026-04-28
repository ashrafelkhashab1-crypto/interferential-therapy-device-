import streamlit as st
import time
import os

# 1. إعداد واجهة البرنامج لتكون عريضة ومظلمة (Dark Mode) مثل الأجهزة الطبية الحديثة
st.set_page_config(page_title="IFT Digital Simulation", layout="wide", initial_sidebar_state="collapsed")

# تصميم الهيدر بشكل محايد واحترافي
st.markdown("""
    <style>
    .main-title { font-size: 40px; color: #00FBFF; text-align: center; font-weight: bold; }
    .stNumberInput label, .stSlider label { color: #00FBFF !important; }
    </style>
    <div class="main-title">INTERFERENTIAL THERAPY (IFT) SIMULATOR</div>
    <p style='text-align: center; color: #888;'>جهاز محاكاة العلاج بالتداخل الترددي - إصدار 2026</p>
    """, unsafe_allow_html=True)

st.markdown("---")

# 2. تقسيم الشاشة (المدخلات على اليسار والمخرجات على اليمين)
col_controls, col_display = st.columns([1, 2])

with col_controls:
    st.subheader("⚙️ إعدادات الجهاز")
    
    # مدخلات الأرقام (تظهر كما طلبتِ)
    base_freq = st.number_input("التردد الأساسي (Base Freq) - Hz", 1000, 10000, 4000)
    beat_freq = st.number_input("تردد النبضات (Beat Freq) - Hz", 1, 250, 100)
    
    st.markdown("---")
    st.write("📈 شدة القنوات (Intensity)")
    ch1 = st.slider("Channel 1 (mA)", 0, 60, 15)
    ch2 = st.slider("Channel 2 (mA)", 0, 60, 15)
    
    t_time = st.number_input("وقت الجلسة (Min)", 1, 60, 15)
    
    # الأزرار
    st.write("")
    start_btn = st.button("RUN SIMULATION | تشغيل", type="primary", use_container_width=True)
    stop_btn = st.button("STOP | إيقاف", use_container_width=True)

with col_display:
    st.subheader("📺 شاشة المحاكاة التفاعلية")
    
    # مكان الأنيميشن (Animation Zone)
    # يمكنك وضع رابط GIF حقيقي هنا لشكل الموجات
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqZ254Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKMGpxxcaNgsj8A/giphy.gif", 
             caption="محاكاة تداخل الموجات الجاري الآن", use_column_width=True)

    # Logic العداد التنازلي والنتائج
    if start_btn:
        if ch1 == 0 or ch2 == 0:
            st.warning("⚠️ يرجى رفع الشدة لبدء المحاكاة.")
        else:
            placeholder = st.empty()
            st.success(f"المحاكاة تعمل الآن بناءً على تردد نبضات {beat_freq} Hz")
            
            # عداد وقت بسيط
            for i in range(5, 0, -1): # تجربة لمدة 5 ثوانٍ فقط للمعاينة
                placeholder.metric("الوقت المتبقي للجلسة", f"{i} ثوانٍ")
                time.sleep(1)
            
            placeholder.empty()
            st.balloons()
            st.info("تمت المحاكاة بنجاح.")

# تذييل بسيط
st.markdown("---")
st.caption("النسخة التجريبية لمشروع المحاكاة الجديد")
