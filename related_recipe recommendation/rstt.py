import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
recipe = pd.read_csv("ff.csv")
recipe = recipe[['RecipeName', 'Ingredients', 'Cuisine', 'Course', 'Diet']]
recipe['tags'] = recipe['Cuisine'] + recipe['Course'] + recipe['Diet']
new_data = recipe.drop(columns=['Cuisine', 'Ingredients', 'Course', 'Diet'])

# Vectorize the tags
cv = CountVectorizer(max_features=99, stop_words='english')
vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()

# Compute cosine similarity
similarity = cosine_similarity(vector)

# Streamlit app
st.title('Recipe Recommendation App')

# Recipe input from the user
selected_recipe = st.selectbox('Select a recipe:', new_data['RecipeName'].values)

# Function to recommend recipes
def recommend(recipe):
    index = new_data[new_data['RecipeName'] == recipe].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    st.write("RELATED RECIPES FOR:", recipe)
    st.write("")
    for i in distance[1:6]:
        st.write(new_data.iloc[i[0]].RecipeName)

# Display recommendations when the user selects a recipe
if st.button('Get Recommendations'):
    recommend(selected_recipe)
