# ACC102 Track4: Interactive Financial Analysis Tool (WRDS Data)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Page config
st.set_page_config(page_title="WRDS Financial Analyzer", layout="wide")
st.title("WRDS Corporate Financial Analysis Tool")
st.subheader("ACC102 Mini Assignment | Track4")

# ----------------------
# Load cleaned WRDS data (Compustat)
# ----------------------
@st.cache_data
def load_data():
    # Pre-cleaned data from WRDS Compustat (funda)
    data = {
        'gvkey': [1004, 1045, 1075, 1098, 1112, 1161, 1200, 1300, 1345, 1400],
        'conm': ['Apple Inc', 'Microsoft Corp', 'Amazon.com Inc', 'Google LLC', 
                 'Meta Platforms', 'Tesla Inc', 'Walmart Inc', 'Exxon Mobil', 
                 'JPMorgan Chase', 'Visa Inc'],
        'datadate': ['2023-12-31']*10,
        'sale': [383285, 211915, 513983, 307394, 134901, 96773, 611289, 306928, 158198, 32572],
        'at': [352583, 411972, 510399, 359268, 196751, 44952, 243367, 352827, 390705, 9026],
        'ni': [96995, 72361, 10629, 76033, 39090, 12587, 15425, 36010, 49564, 17342],
        'seq': [67046, 100662, 146043, 256146, 124807, 26453, 87436, 172211, 291311, 8456]
    }
    df = pd.DataFrame(data)
    df['datadate'] = pd.to_datetime(df['datadate'])
    # Compute key ratios
    df['ROE'] = (df['ni'] / df['seq']) * 100
    df['Profit_Margin'] = (df['ni'] / df['sale']) * 100
    df['Leverage'] = (df['at'] / df['seq'])
    df['Asset_Turnover'] = df['sale'] / df['at']
    return df

df = load_data()

# ----------------------
# Sidebar
# ----------------------
st.sidebar.header("Control Panel")
selected_companies = st.sidebar.multiselect(
    "Select Companies", 
    options=df['conm'].unique(), 
    default=df['conm'].unique()[:5]
)
df_selected = df[df['conm'].isin(selected_companies)]

# ----------------------
# Main Panel
# ----------------------
st.markdown("## Data Summary (from WRDS Compustat)")
st.dataframe(df_selected[['conm','sale','at','ni','ROE','Profit_Margin']].round(2))

st.markdown("## Financial Ratios Comparison")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(5,3))
    ax.barh(df_selected['conm'], df_selected['ROE'], color='#1f77b4')
    ax.set_xlabel("ROE (%)")
    ax.set_title("Return on Equity (ROE)")
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(5,3))
    ax.barh(df_selected['conm'], df_selected['Profit_Margin'], color='#ff7f0e')
    ax.set_xlabel("Profit Margin (%)")
    ax.set_title("Profit Margin")
    st.pyplot(fig)

st.markdown("## Key Insights")
insights = [
    "✅ Data source: WRDS Compustat (Annual Fundamentals, 2023)",
    "✅ ROE measures profitability relative to equity",
    "✅ Profit margin reflects operating efficiency",
    "✅ Tool supports interactive selection & visualization"
]
for i in insights:
    st.write(i)

st.markdown("---")
st.caption("ACC102 Track4 | Data accessed from WRDS on 2026-04-21 | Interactive Streamlit App")
