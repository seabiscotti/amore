import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("./venues.csv")

# Calculate the average price per person
average_price_per_person = df['price'].sum() / df['max_capacity'].sum()

# Create a slider for the number of people
num_people = st.slider('Number of people', 1, 500, 100)

# Create a slider for rating
rating = st.slider('Rating', 1, 5, 3)

# Calculate the estimated price
estimated_price = num_people * average_price_per_person

# Display the estimated price in bold
st.markdown(f'**The estimated price for a wedding with {num_people} people is ${estimated_price:.2f}**')

# Query the wedding venue name and get a general rate
venue_name = st.text_input('Enter a venue name')
if venue_name:
    venue = df[df['name'] == venue_name]
    if not venue.empty:
        st.write(f"The general rate for {venue_name} is ${venue['price'].values[0]}")
    else:
        st.write(f"{venue_name} not found in the dataset.")

# Plot a scatterplot of prices vs. max_capacity
fig, ax = plt.subplots()
ax.scatter(df['price'], df['max_capacity'], alpha=0.5)
ax.set_xlabel('Price')
ax.set_ylabel('Max Capacity')
st.pyplot(fig)

# Display venues that match the selected capacity and rating
matching_venues = df[(df['max_capacity'] >= num_people) & (df['rating'] >= rating)]
matching_venues = matching_venues.nsmallest(5, 'price')
st.write("Venues that can accommodate the selected number of people and have at least the selected rating:")
st.write(matching_venues)




