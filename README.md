phonepe_project/
│
├── app.py              # Main navigation (Home & Analysis)
├── map.py              # Map visualization module
├── analysis.py         # SQL-based analysis module
├── data/               # PhonePe dataset (JSON)
└── README.md

###  Database Overview ###

The PhonePe dataset contains multiple tables.
However, this project focuses on three core tables for analysis:

# Tables Used in Dashboard
aggregated_user
aggregated_transaction
map_user
# Key Columns
year, quarter
state, district
user_count
transaction_amount
registered_users
app_opens
# Features
 Map Visualization (state-wise insights)
 Multiple Analysis Scenarios
User Analysis
Transaction Analysis
Growth Analysis
Top & Bottom Analysis
 Interactive Filters
Year
Quarter
# Dynamic Charts
Bar charts
Line charts
Pie charts
# Key Insights
 User Growth
Steady increase in users over time
Significant growth observed after 2020
 Transaction Trends
High transaction volume concentrated in a few states
Major contribution from urban regions
 Engagement Analysis
Engagement varies across states
High users do not always mean high activity
 # Regional Insights
Top states: Maharashtra, Karnataka, Telangana
Lower adoption in rural areas
