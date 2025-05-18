# utility functions for data processing and visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data(countries):
    df_list = []
    for country in countries:
        path = f"src/notebooks/data/{country.lower().replace(' ', '_')}_clean.csv"
        try:
            df = pd.read_csv(path, parse_dates=["Timestamp"])
            df["Country"] = country
            df_list.append(df)
        except FileNotFoundError:
            st.error(f"Data for {country} not found at {path}")
    return pd.concat(df_list, ignore_index=True)

def plot_ghi_boxplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x="Country", y="GHI", palette="Set2", ax=ax)
    ax.set_title("GHI Distribution")
    ax.set_ylabel("Global Horizontal Irradiance")
    ax.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)

def get_summary_table(df):
    summary = df.groupby("Country")["GHI"].agg(["mean", "median", "std"]).round(2).reset_index()
    summary.columns = ["Country", "Mean GHI", "Median GHI", "Std Dev"]
    return summary
