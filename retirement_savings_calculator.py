import streamlit as st
import numpy as np

# Define the calculation function with exception handling
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

# Streamlit UI
st.title('Retirement Planning Calculator')

# Input fields
current_age = st.number_input('Current Age:', min_value=0, max_value=100, value=30)
retirement_age = st.number_input('Retirement Age:', min_value=current_age, max_value=100, value=65)
current_savings = st.number_input('Current Savings ($):', min_value=0, value=10000)
annual_contribution = st.number_input('Annual Contribution ($):', min_value=0, value=5000)
return_rate = st.number_input('Expected Annual Return Rate (as a decimal):', min_value=0.0, max_value=1.0, value=0.05)

# Calculate button
if st.button('Calculate'):
    future_savings = calculate_retirement_savings(current_age, retirement_age, current_savings, annual_contribution, return_rate)
    if future_savings is not None:
        st.write(f'Estimated Retirement Savings: ${future_savings:,.2f}')
    else:
        st.write('Unable to calculate retirement savings due to input error.')

# Note: Run this application by entering "streamlit run retirement_savings_calculator.py" in the terminal window.
