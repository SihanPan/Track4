# ACC102 Track4: Interactive Financial Analysis Tool (WRDS Data)
Student name: Sihan Pan

Student ID: 2471700

Module: ACC102

Track: 4

## 1. Problem & User
This tool helps finance students and analysts quickly visualize and compare key financial ratios from WRDS corporate data.

## 2. Data
- Source: WRDS Compustat (funda, annual fundamentals)
- Access date: 2026-04-21
- Variables: sale, at, ni, seq, ROE, Profit Margin, Leverage, Asset Turnover

## 3. Methods
- Data loading & cleaning with Pandas
- Financial ratio calculation
- Interactive visualization with Streamlit
- Bar charts for cross-company comparison

## 4. Key Findings
- Technology firms generally show high ROE and profit margins
- Profitability varies significantly across sectors
- Interactive filtering improves decision efficiency

## 5. How to Run
1. Install dependencies: pip install -r requirements.txt
2. Run: streamlit run app.py

## 6. Product Link
[Your Streamlit Cloud Link Here]

## 7. Limitations & Improvements
- Only 2023 data included
- Future: add time-series analysis & WRDS real-time connection
