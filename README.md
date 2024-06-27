# Retirement Savings Calculator

Welcome to the **Retirement Savings Calculator**! 🎉 This is your one-stop-shop for planning your future nest egg. Let's dive into what this repository has to offer.

## About the Project

This nifty tool helps you calculate your retirement savings with just a few clicks. It takes into account your current age, desired retirement age, current savings, annual contributions, and the expected annual return rate. Voilà! You'll get an estimate of your future savings.

## What's Inside?

The repository contains a single file:
- **`retirement_savings_calculator.py`**: The magic happens here. This Python script uses Streamlit and NumPy to crunch the numbers and give you the results.

## How It Works

Here's a peek under the hood at the key components of our calculator:

### Importing Libraries
```python
import streamlit as st
import numpy as np
```

### The Calculation Function
This function handles the heavy lifting and ensures everything runs smoothly.
```python
def calculate_retirement_savings(current_age, retirement_age, current_savings, annual_contribution, return_rate):
    try:
        years_to_retirement = retirement_age - current_age
        if years_to_retirement <= 0:
            raise ValueError("Retirement age must be greater than current age.")

        future_value = current_savings
        
        for _ in range(years_to_retirement):
            future_value += annual_contribution
            future_value *= (1 + return_rate)
        
        return future_value
    
    except ValueError as e:
        st.error(f"Value Error: {e}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None
```

### Streamlit UI
The user-friendly interface that makes it all possible.
```python
st.title('Retirement Planning Calculator')

current_age = st.number_input('Current Age:', min_value=0, max_value=100, value=30)
retirement_age = st.number_input('Retirement Age:', min_value=current_age, max_value=100, value=65)
current_savings = st.number_input('Current Savings ($):', min_value=0, value=10000)
annual_contribution = st.number_input('Annual Contribution ($):', min_value=0, value=5000)
return_rate = st.number_input('Expected Annual Return Rate (as a decimal):', min_value=0.0, max_value=1.0, value=0.05)

if st.button('Calculate'):
    future_savings = calculate_retirement_savings(current_age, retirement_age, current_savings, annual_contribution, return_rate)
    if future_savings is not None:
        st.write(f'Estimated Retirement Savings: ${future_savings:,.2f}')
    else:
        st.write('Unable to calculate retirement savings due to input error.')
```

## Getting Started

To run this application, you'll need Python and Streamlit installed on your machine. If you haven't already, install Streamlit with:
```bash
pip install streamlit
```

Then, clone this repository:
```bash
git clone https://github.com/yourusername/retirement_savings_calculator.git
cd retirement_savings_calculator
```

Finally, run the app:
```bash
streamlit run retirement_savings_calculator.py
```

## Enjoy Your Journey to Retirement!

Play around with the numbers and see how your savings can grow over time. Happy planning! 🏖️

## Contributing

Found a bug or have an idea for a cool new feature? Feel free to open an issue or submit a pull request.


---

Thanks for checking out the **Retirement Savings Calculator**! May your retirement be as fabulous as you've always dreamed. 🎉
