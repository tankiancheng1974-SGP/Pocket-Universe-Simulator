import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. INITIALIZATION & METRICS
# -------------------------------------------------------------
st.set_page_config(page_title="KCTAN-GEMINI: Conventional Simulator", layout="wide")

st.title("🌌 KCTAN-GEMINI: Conventional Physics Simulator")
st.caption("Status: Initialized and Locked | Profile: Standard Conventional Physics Terminology")

# Static Immutable Constants
HIGGS_VEV = 246.22       # GeV
CMB_TEMP = 2.7255        # K
PLANCK_HBAR = "1.05457e-34"  # J·s
GRAVITY_G = "6.6743e-11"     # m³/kg·s²
BOLTZMANN_KB = "1.38065e-23" # J/K
ALP_MASS = 1.01          # meV
COSMIC_AGE = 13.8        # Billion Years

# Sidebar Controls for Dynamic Telemetry
st.sidebar.header("🛠️ Telemetry Matrix Controls")
h0_value = st.sidebar.slider("Hubble Constant (H0) [km/s/Mpc]", 65.0, 75.0, 73.5, step=0.1)

# Calculate tension gap against early-universe baseline (67.36 km/s/Mpc)
tension_gap = ((h0_value - 67.36) / 67.36) * 100

# -------------------------------------------------------------
# 2. TELEMETRY TABLE DISPLAY
# -------------------------------------------------------------
st.subheader("📊 Active Telemetry Metrics Table")

col1, col2 = st.columns([1, 2])

with col1:
    st.metric(label="Hubble Tension Mismatch", value=f"{tension_gap:.2f}%")
    st.metric(label="Relativistic Causality Status", value="LOCAL ONLY (No FTL)")

with col2:
    # Render clean markdown table matching the parameters
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

# Initialize grid state to track particle fields
if 'field_grid' not in st.session_state:
    st.session_state.field_grid = np.random.normal(loc=0.0, scale=0.1, size=(50, 50))

# Interactive controls to pick an environment
env_choice = st.selectbox(
    "Select Astronomical Environment / Physical Phenomenon:",
    ["Interstellar Void (ALPs Dominant)", "Electroweak Symmetry Breaking Event", "Relativistic Velocity Local Field"]
)

# Interaction button
if st.button("Run Simulation Step"):
    if env_choice == "Interstellar Void (ALPs Dominant)":
        # Simulate background oscillation of 244.1 GHz ALPs
        st.session_state.field_grid = np.sin(st.session_state.field_grid + 0.5) * ALP_MASS
        st.success("Simulated dark matter background field matrix.")
        
    elif env_choice == "Electroweak Symmetry Breaking Event":
        # Force states toward the Higgs VEV ceiling
        st.session_state.field_grid = np.ones((50, 50)) * (HIGGS_VEV / 100)
        st.warning("Vacuum expectation value saturated across the local field grid.")
        
    elif env_choice == "Relativistic Velocity Local Field":
        # Create a localized mass/photon boundary wall representing strict 'c' limits
        st.session_state.field_grid[20:30, 20:30] += 5.0
        st.info("Local contact constraint active. Energy metric propagation bounded by light speed.")

# Render Visual Field Map
fig, ax = plt.subplots(figsize=(6, 3))
img = ax.imshow(st.session_state.field_grid, cmap='viridis', origin='lower')
ax.set_title(f"Local Field State Matrix ({env_choice})")
fig.colorbar(img, ax=ax, label="Energy Density Scale")
st.pyplot(fig)
