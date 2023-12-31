import pandas as pd
recipe=pd.read_csv("ff.csv")
recipe.isnull().sum()
recipe.columns
recipe=recipe[['RecipeName','Ingredients','Cuisine','Course', 'Diet']]
recipe['tags']=recipe['Cuisine']+recipe['Course']+recipe['Diet']
new_data=recipe.drop(columns=['Cuisine','Ingredients','Course','Diet'])
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=99,stop_words='english')
cv
vector=cv.fit_transform(new_data['tags'].values.astype('U')).toarray()
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vector)
similarity
new_data[new_data['RecipeName']=="Kobari Charu recipe - Kobbari Charu Recipe"].index[0]
distance=sorted(list(enumerate(similarity[94])),reverse=True,key=lambda vector:vector[1])
for i in distance[1:6]:
     print(i)
distance=sorted(list(enumerate(similarity[94])),reverse=True,key=lambda vector:vector[1])
for i in distance[1:6]:
    print(new_data.iloc[i[0]].RecipeName)
def recommand(recipe):
    index=new_data[new_data['RecipeName']==recipe].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    print("RELATED_RECIPE : ",recipe)
    print("")
    for i in distance[1:6]:
        print(new_data.iloc[i[0]].RecipeName)
recommand("Kobari Charu recipe - Kobbari Charu Recipe")
recommand('Masala Karela Recipe')