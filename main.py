import pandas as pd
import streamlit as st

# Load the dataset
@st.cache_data  # Cache the dataframe to speed up app performance
def load_data():
    return pd.read_csv("events.csv")

def main():
    st.title("Historical Events Finder")

    # Load the dataset
    df = load_data()

    # Input date from the user
    date_input = st.text_input("Enter a date (e.g., '19 December'):").strip().lower()

    if date_input:
        # Filter dataframe based on user input
        filtered_df = df[df["Date"].str.contains(date_input, case=False)]

        # Display events for the input date
        if not filtered_df.empty:
            st.header(f"Events for {date_input.capitalize()}:")
            for i, row in filtered_df.iterrows():
                st.subheader(f"Event {i + 1}:")
                st.write(row["Event 1"])
                st.write(row["Event 2"])
                st.write(row["Event 3"])
        else:
            st.write("No events found for the entered date.")

if __name__ == "__main__":
    main()

    