# Black-Scholes Option Pricing Calculator

This project provides an interactive calculator for pricing European options using the **Black-Scholes Model**. Built with **Python** and **Streamlit**, it allows users to calculate option prices and their Greeks (Delta, Gamma, Theta, Vega, and Rho), and visualize how these metrics change with different spot prices.

## Features

- **Black-Scholes Model**: For pricing European call and put options.
- **Option Greeks**: Calculates Delta, Gamma, Theta, Vega, and Rho.
- **Interactive UI**: Built with Streamlit for easy use.
- **Visualizations**: Plots how option price and Greeks change with varying spot prices.
- **Real-Time Input**: Users can adjust parameters like spot price, volatility, and time to expiry, and see results immediately.

## Installation

Ensure you have **Python 3.x** installed and then install the necessary dependencies:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/black-scholes-option-calculator.git
    cd black-scholes-option-calculator
    ```

2. Install the required libraries:

    ```bash
    pip install streamlit numpy scipy matplotlib seaborn
    ```

## Usage

To run the application, use the following command in your terminal:

```bash
streamlit run app.py
```
