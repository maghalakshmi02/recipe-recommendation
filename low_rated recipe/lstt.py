import streamlit as st
import pandas as pd
import lrate as r

# Assuming you have an existing DataFrame named existing_df
# Extract relevant columns
selected_columns = ['RecipeName', 'weighted_avg', 'URL']
df = r.existing_df[selected_columns].copy()

# Set 'RecipeName' column as the index
df.set_index('RecipeName', inplace=True)

# Streamlit app
st.title('Top Rated Recipes')
st.header('Explore and Discover Delicious Recipes')

# Display the list of recipes with weighted average and URL
st.write('Here are the recipes:')
st.table(df[['weighted_avg']])

# Additional features - you can customize the display
selected_recipe = st.selectbox('Select a recipe to view details:', df.index)

# Display details for the selected recipe
selected_row = df.loc[selected_recipe]
st.write(f'Details for {selected_recipe}:')
#st.write(f'Weighted Average Rating: {selected_row["weighted_avg"]}')
st.write(f'URL: {selected_row["URL"]}')
