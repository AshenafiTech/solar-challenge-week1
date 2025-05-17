# Solar Dashboard Deployment Notes

This folder contains scripts and notes related to the deployment and management of the solar insights dashboard.

## Deployment Instructions (Streamlit Community Cloud)

1. Push to GitHub branch `dashboard-dev`.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your repo and select `app/main.py` as the entry point.
4. Set up `.streamlit/secrets.toml` if needed.
5. Ensure `data/` folder is not pushed – app expects local files.

## Notes

- The dashboard visualizes solar irradiance data (GHI) across selected countries.
- The user can choose countries and view boxplots and summary statistics.
