import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="IF Therapy Simulator", layout="centered")

st.title("⚡ IF Therapy Simulator")

# Controls
f1 = st.slider("Channel 1 Frequency (Hz)", 3000, 5000, 4000)
f2 = st.slider("Channel 2 Frequency (Hz)", 3000, 5000, 4100)
intensity = st.slider("Intensity", 1, 50, 20)

beat = abs(f1 - f2)
st.markdown(f"### Beat Frequency: {beat} Hz")

# Placeholder for animation
chart = st.empty()

# Time axis
x = np.linspace(0, 1, 800)

t = 0

# Animation loop
for _ in range(200):

    y1 = np.sin(2*np.pi*f1*(x + t))
    y2 = np.sin(2*np.pi*f2*(x + t))
    y3 = (y1 + y2) * (intensity / 20)

    fig, ax = plt.subplots()

    ax.plot(x, y1, label="Channel 1", linewidth=1)
    ax.plot(x, y2, label="Channel 2", linewidth=1)
    ax.plot(x, y3, label="Interference", linewidth=2)

    ax.set_facecolor("black")
    fig.patch.set_facecolor("#06141c")

    ax.set_xticks([])
    ax.set_yticks([])

    ax.legend(loc="upper right")

    chart.pyplot(fig)
    plt.close(fig)

    t += 0.01
    time.sleep(0.03)
