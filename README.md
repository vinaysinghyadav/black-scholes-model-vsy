<<<<<<< HEAD
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
## Input Parameters

The user needs to input the following parameters:

- **Risk-Free Rate (r)**: The risk-free interest rate (e.g., 3% as `0.03`).
- **Spot Price (S)**: The current market price of the underlying asset.
- **Strike Price (K)**: The strike price of the option.
- **Time to Expiry (T)**: The time until the option expires, in years.
- **Volatility (σ)**: The volatility of the underlying asset (annualized standard deviation).
- **Option Type**: Choose between **Call** or **Put** options.

## Results

After entering the parameters, the app will display the following results:

- **Option Price**: The Black-Scholes price for the selected option type.
- **Greeks**: The **Delta**, **Gamma**, **Theta**, **Vega**, and **Rho** for the given option.
- **Visualizations**: Graphs showing the option price and Greeks for different spot prices.


## License

This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- This app was built by **Vinay Singh Yadav**.
- The **Black-Scholes Model** is a widely used model for pricing European options in financial markets.

=======
# black-scholes-model-vsy
>>>>>>> 2e4394e (Merge main into master and resolve conflicts)
