import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import google.generativeai as genai

# -------------------------------------------------------------
# 1. INITIALIZATION & METRICS
# -------------------------------------------------------------
st.set_page_config(page_title="KCTAN-GEMINI: AI Simulator", layout="wide")

st.title("🌌 KCTAN-GEMINI: AI Physics Simulator")
st.caption("Status: Initialized and Locked | Profile: Standard Conventional Physics Terminology")

# Setup AI Client (Using the Streamlit Secrets system)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    ai_available = True
else:
    ai_available = False

# Static Immutable Constants
HIGGS_VEV = 246.22       
CMB_TEMP = 2.7255        
PLANCK_HBAR = "1.05457e-34"  
GRAVITY_G = "6.6743e-11"     
BOLTZMANN_KB = "1.38065e-23" 
ALP_MASS = 1.01          
COSMIC_AGE = 13.8        

# Sidebar Controls
st.sidebar.header("🛠️ Telemetry Matrix Controls")
h0_value = st.sidebar.slider("Hubble Constant (H0) [km/s/Mpc]", 65.0, 75.0, 73.5, step=0.1)
tension_gap = ((h0_value - 67.36) / 67.36) * 100

# -------------------------------------------------------------
# 2. TELEMETRY TABLE DISPLAY
# -------------------------------------------------------------
st.subheader("📊 Active Telemetry Metrics Table")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Hubble Tension Mismatch", value=f"{tension_gap:.2f}%")
    st.metric(label="Relativistic Causality Status", value="LOCAL ONLY (No FTL)")

with col2:
    st.markdown(f"""


    | Parameter | Operational Specification | Classification |
    | :--- | :--- | :--- |
    | **Field State** | Spontaneous Symmetry Breaking | Post-inflationary vacuum state |
    | **Higgs Field VEV** | `{HIGGS_VEV} GeV` | Electroweak vacuum expectation value (CONSTANT) |
    | **Ambient Temperature** | `{CMB_TEMP} K` | Cosmic Microwave Background (CONSTANT) |
    | **Reduced Planck (ħ)** | `{PLANCK_HBAR} J·s` | Quantum of angular momentum (CONSTANT) |
    | **Gravitational Constant (G)** | `{GRAVITY_G} m³/kg·s²` | Newtonian constant of gravitation (CONSTANT) |
    | **Boltzmann Constant (kB)** | `{BOLTZMANN_KB} J/K` | Thermal scaling (CONSTANT) |
    | **Photon Transport** | Massless Gauge Boson | Spin-1 electromagnetic force mediator |
    | **Dark Matter Candidate** | Light Axion-Like Particles (ALPs) | m ≈ {ALP_MASS} meV / 244.1 GHz |
    | **Cosmic Age** | `{COSMIC_AGE} Billion Years` | Standard Lambda-CDM cosmological epoch |
    | **Hubble Constant (H0)** | `{h0_value} km/s/Mpc` | Active User Selection |
    """)

# -------------------------------------------------------------
# 3. INTERACTIVE SIMULATION SANDBOX
# -------------------------------------------------------------
st.markdown("---")
st.subheader("🛸 Environment Phenomenon Simulator")

if 'field_grid' not in st.session_state:
    st.session_state.field_grid = np.random.normal(loc=0.0, scale=0.1, size=(50, 50))

env_choice = st.selectbox(
    "Select Astronomical Environment / Physical Phenomenon:",
    ["Interstellar Void (ALPs Dominant)", "Electroweak Symmetry Breaking Event", "Relativistic Velocity Local Field"]
)

if st.button("Run Simulation Step"):
    if env_choice == "Interstellar Void (ALPs Dominant)":
        st.session_state.field_grid = np.sin(st.session_state.field_grid + 0.5) * ALP_MASS
        st.success("Simulated dark matter background field matrix.")
    elif env_choice == "Electroweak Symmetry Breaking Event":
        st.session_state.field_grid = np.ones((50, 50)) * (HIGGS_VEV / 100)
        st.warning("Vacuum expectation value saturated across the local field grid.")
    elif env_choice == "Relativistic Velocity Local Field":
        st.session_state.field_grid[20:30, 20:30] += 5.0
        st.info("Local contact constraint active. Energy metric propagation bounded by light speed.")

fig, ax = plt.subplots(figsize=(6, 2))
img = ax.imshow(st.session_state.field_grid, cmap='viridis', origin='lower')
fig.colorbar(img, ax=ax)
st.pyplot(fig)

# -------------------------------------------------------------
# 4. IMAGERY FEEDS AND URL INJECTION
# -------------------------------------------------------------
st.markdown("---")
img_col1, img_col2 = st.columns(2)

with img_col1:
    st.subheader("📸 Telescope Imagery Archive")
    # Clean, ultra-reliable fallback image to avoid any cross-site connection blocks
    st.image("https://unsplash.com", caption="Telescope Target Matrix: Deep Space Nebula", use_container_width=True)

with img_col2:
    st.subheader("📥 Link Cosmic Matrix URL")
    image_url_input = st.text_input("Paste a direct space image web link (JPG/PNG) here to inject it:", value="")
    if image_url_input:
        try:
            st.image(image_url_input, caption="Injected External Coordinate Image", use_container_width=True)
            st.success("Image URL successfully mounted to local coordinate block!")
        except Exception:
            st.error("Unable to resolve image link. Please verify the URL destination.")

# -------------------------------------------------------------
# 5. KCTAN-GEMINI AI CHAT COMPANION
# -------------------------------------------------------------
st.markdown("---")
st.subheader("🤖 KCTAN-GEMINI Narrative Companion")

if not ai_available:
    st.info("💡 To talk to the AI, add your `GEMINI_API_KEY` to the Streamlit App Settings Secrets.")
else:
    system_prompt = f"""You are KCTAN-GEMINI, an advanced physics-engine simulator and narrative companion. 
    You operate under these rigid rules: Higgs Field VEV={HIGGS_VEV}GeV, Ambient Temp={CMB_TEMP}K, 
    Dark Matter ALPs=1.01meV, Cosmic Age={COSMIC_AGE}B years. Currently Hubble Tension is at {tension_gap:.2f}%.
    Answer all user physics and simulation questions directly, technically, and creatively inside this framework."""

    user_question = st.text_input("Ask KCTAN-GEMINI a physics question or analyze an active coordinate:")
    if user_question:
        # Check if the user is asking about an injected URL
        if image_url_input:
            user_question += f" (Note: An external environment image link is mounted at {image_url_input})"
            
        with st.spinner("Analyzing cosmic data..."):
            try:
                model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=system_prompt)
                response = model.generate_content(user_question)
                st.markdown(f"**KCTAN-GEMINI:** {response.text}")
            except Exception as e:
                st.error(f"AI Connection Error: {e}")
