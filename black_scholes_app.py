import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

def calculate_option_price(spot, strike, rate, time_to_expiry, volatility, option_type="c"):
    d1 = (np.log(spot/strike) + (rate + volatility**2/2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)
    try:
        if option_type == "c":
            option_price = spot * norm.cdf(d1) - strike * np.exp(-rate * time_to_expiry) * norm.cdf(d2)
        elif option_type == "p":
            option_price = strike * np.exp(-rate * time_to_expiry) * norm.cdf(-d2) - spot * norm.cdf(-d1)
        return option_price
    except:
        st.sidebar.error("Please check all input parameters.")

def calculate_delta(spot, strike, rate, time_to_expiry, volatility, option_type="c"):
    d1 = (np.log(spot/strike) + (rate + volatility**2/2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    try:
        if option_type == "c":
            return norm.cdf(d1)
        elif option_type == "p":
            return -norm.cdf(-d1)
    except:
        st.sidebar.error("Please check all input parameters.")

def calculate_gamma(spot, strike, rate, time_to_expiry, volatility):
    d1 = (np.log(spot/strike) + (rate + volatility**2/2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    try:
        return norm.pdf(d1) / (spot * volatility * np.sqrt(time_to_expiry))
    except:
        st.sidebar.error("Please check all input parameters.")

def calculate_theta(spot, strike, rate, time_to_expiry, volatility, option_type="c"):
    d1 = (np.log(spot/strike) + (rate + volatility**2/2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)
    try:
        if option_type == "c":
            return -((spot * norm.pdf(d1) * volatility) / (2 * np.sqrt(time_to_expiry))) - rate * strike * np.exp(-rate * time_to_expiry) * norm.cdf(d2)
        elif option_type == "p":
            return -((spot * norm.pdf(d1) * volatility) / (2 * np.sqrt(time_to_expiry))) + rate * strike * np.exp(-rate * time_to_expiry) * norm.cdf(-d2)
    except:
        st.sidebar.error("Please check all input parameters.")

def calculate_vega(spot, strike, rate, time_to_expiry, volatility):
    d1 = (np.log(spot/strike) + (rate + volatility**2/2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    try:
        return spot * np.sqrt(time_to_expiry) * norm.pdf(d1) * 0.01
    except:
        st.sidebar.error("Please check all input parameters.")

def calculate_rho(spot, strike, rate, time_to_expiry, volatility, option_type="c"):
    d1 = (np.log(spot/strike) + (rate + volatility**2/2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)
    try:
        if option_type == "c":
            return 0.01 * strike * time_to_expiry * np.exp(-rate * time_to_expiry) * norm.cdf(d2)
        elif option_type == "p":
            return 0.01 * -strike * time_to_expiry * np.exp(-rate * time_to_expiry) * norm.cdf(-d2)
    except:
        st.sidebar.error("Please check all input parameters.")

# Streamlit configuration and input section
st.set_page_config(page_title="Black-Scholes Option Calculator", layout="wide")

# Add custom styling for backgrounds and fonts
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #FF7F50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stMarkdown {
        font-size: 18px;
        font-weight: bold;
    }
    h1 {
        font-size: 48px;
        text-align: center;
        background-color: #FF7F50;
        color: white;
        padding: 20px 0;
    }
    .footer {
        font-size: 16px;
        text-align: center;
        color: #555;
        margin-top: 30px;
    }
    .header {
        font-size: 24px;
        text-align: center;
        margin-top: 20px;
        font-weight: bold;
        color: #FF7F50;
    }
    </style>
    """, unsafe_allow_html=True)

# Add the Streamlit logo to the sidebar (with smaller size)
st.sidebar.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)

# Add the header with background color and larger size
st.markdown("<h1>Black-Scholes Option Calculator</h1>", unsafe_allow_html=True)

# Add the "Made by Vinay Singh Yadav" below the header and center-align it
st.markdown("<div class='header'>Made by Vinay Singh Yadav</div>", unsafe_allow_html=True)

# Sidebar: User Inputs
st.sidebar.header("Input Parameters")
r = st.sidebar.number_input("Risk-Free Rate", min_value=0.0, max_value=1.0, step=0.001, value=0.03, help="Risk-free interest rate")
S = st.sidebar.number_input("Spot Price", min_value=1.0, step=0.1, value=100.0, help="Current market price of the asset")
K = st.sidebar.number_input("Strike Price", min_value=1.0, step=0.1, value=100.0, help="Option strike price")
expiry_days = st.sidebar.number_input("Time to Expiry (in days)", min_value=1, step=1, value=180, help="Time to expiry in days")
sigma = st.sidebar.number_input("Volatility", min_value=0.0, max_value=1.0, step=0.01, value=0.25, help="Volatility of the underlying asset")
option_type_input = st.sidebar.selectbox("Option Type", ["Call", "Put"], help="Select the option type")

option_type = "c" if option_type_input == "Call" else "p"
T = expiry_days / 365

# Generate prices and Greeks
prices = [calculate_option_price(i, K, r, T, sigma, option_type) for i in range(1, int(S)+50)]
deltas = [calculate_delta(i, K, r, T, sigma, option_type) for i in range(1, int(S)+50)]
gammas = [calculate_gamma(i, K, r, T, sigma) for i in range(1, int(S)+50)]
thetas = [calculate_theta(i, K, r, T, sigma, option_type) for i in range(1, int(S)+50)]
vegas = [calculate_vega(i, K, r, T, sigma) for i in range(1, int(S)+50)]
rhos = [calculate_rho(i, K, r, T, sigma, option_type) for i in range(1, int(S)+50)]

# Plotting with Seaborn and Matplotlib
sns.set_style("darkgrid")

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=range(1, int(S)+50), y=prices, color='tab:blue', label="Price", linewidth=2)
ax1.set_xlabel('Spot Price', fontsize=14)
ax1.set_ylabel('Option Price', fontsize=14)
ax1.set_title('Option Price (Black-Scholes)', fontsize=16)
ax1.grid(True)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=range(1, int(S)+50), y=deltas, color='tab:green', label="Delta", linewidth=2)
ax2.set_xlabel('Spot Price', fontsize=14)
ax2.set_ylabel('Delta', fontsize=14)
ax2.set_title('Option Delta', fontsize=16)
ax2.grid(True)

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=range(1, int(S)+50), y=gammas, color='tab:orange', label="Gamma", linewidth=2)
ax3.set_xlabel('Spot Price', fontsize=14)
ax3.set_ylabel('Gamma', fontsize=14)
ax3.set_title('Option Gamma', fontsize=16)
ax3.grid(True)

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=range(1, int(S)+50), y=thetas, color='tab:red', label="Theta", linewidth=2)
ax4.set_xlabel('Spot Price', fontsize=14)
ax4.set_ylabel('Theta', fontsize=14)
ax4.set_title('Option Theta', fontsize=16)
ax4.grid(True)

fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=range(1, int(S)+50), y=vegas, color='tab:purple', label="Vega", linewidth=2)
ax5.set_xlabel('Spot Price', fontsize=14)
ax5.set_ylabel('Vega', fontsize=14)
ax5.set_title('Option Vega', fontsize=16)
ax5.grid(True)

fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=range(1, int(S)+50), y=rhos, color='tab:brown', label="Rho", linewidth=2)
ax6.set_xlabel('Spot Price', fontsize=14)
ax6.set_ylabel('Rho', fontsize=14)
ax6.set_title('Option Rho', fontsize=16)
ax6.grid(True)

# Display the results in the layout
st.subheader("Option Pricing and Greeks")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"**Option Price**: {calculate_option_price(S, K, r, T, sigma, option_type):.2f}")
    st.markdown(f"**Delta**: {calculate_delta(S, K, r, T, sigma, option_type):.2f}")
    st.markdown(f"**Gamma**: {calculate_gamma(S, K, r, T, sigma):.2f}")
    st.markdown(f"**Theta**: {calculate_theta(S, K, r, T, sigma, option_type):.2f}")
    st.markdown(f"**Vega**: {calculate_vega(S, K, r, T, sigma):.2f}")
    st.markdown(f"**Rho**: {calculate_rho(S, K, r, T, sigma, option_type):.2f}")

with col2:
    st.subheader("Visualizations")
    st.pyplot(fig1)
    st.pyplot(fig2)
    st.pyplot(fig3)
    st.pyplot(fig4)
    st.pyplot(fig5)
    st.pyplot(fig6)

# Footer Section
st.markdown('<div class="footer">Made by Vinay Singh Yadav</div>', unsafe_allow_html=True)