# main Streamlit application script

import streamlit as st
from utils import load_data, plot_ghi_boxplot, get_summary_table

st.set_page_config(page_title="Solar Insights Dashboard", layout="centered")

st.title("Solar Irradiance Insights Dashboard")

# Sidebar
st.sidebar.header("Controls")
countries = ["Benin", "SierraLeone", "Togo"]
selected_countries = st.sidebar.multiselect("Select countries:", countries, default=countries)

if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()

# Load data
df_all = load_data(selected_countries)

# Boxplot
st.subheader("GHI Distribution by Country")
plot_ghi_boxplot(df_all)

# Summary Table
st.subheader("GHI Summary Statistics")
summary_df = get_summary_table(df_all)
st.dataframe(summary_df)
