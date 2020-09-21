import pandas as pd

# Load and clean data
hk = pd.read_csv('./data/hk_auctions.csv', header=0)
hk['sales_dollar'].fillna('0', inplace=True)
hk.drop(hk[hk.sales_dollar == '[not communicated]'].index, inplace=True)

# Convert data types to numeric
hk['sales_dollar'] = hk['sales_dollar'].apply(pd.to_numeric)

# Add calculated fields
hk['avg_estimate_dollar'] = hk.high_estimate_dollar - hk.low_estimate_dollar
hk['diff_est_actual'] = hk.sales_dollar - hk.avg_estimate_dollar
