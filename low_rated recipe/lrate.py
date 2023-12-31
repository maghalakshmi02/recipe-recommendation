import pandas as pd
# Data Loading 
recipe_df = pd.read_csv(r"ff.csv")
rating_df=pd.read_csv(r"rating.csv")
#renaming the column name
recipe_df.rename(columns={'RecipeId':'recipe_id'},inplace=True)
# combining the df (which users voted for recipe_id=1)
df = pd.merge(recipe_df,rating_df,on='recipe_id')
#checking for null values
combined_df = df.dropna()
#calculating no_of_user voted for each recipe--(v)
no_of_votes=(combined_df.groupby(by=['recipe_id'])['rating'].count().reset_index().
rename(columns = {'rating': 'totalRatingCount'})
[['recipe_id', 'totalRatingCount']])
#calculating avg(mean)_of_rating for each recipe--(r)
ratings_avg=(combined_df.groupby(by=['recipe_id'])['rating'].mean().reset_index().
rename(columns = {'rating': 'avg'})
[['recipe_id', 'avg']])
no_of_votes['RecipeName']=recipe_df['RecipeName']
no_of_votes['average']=ratings_avg['avg']
no_of_votes['URL']=recipe_df['URL']
v=no_of_votes['totalRatingCount']#no.of votes for each recipe
m=no_of_votes['totalRatingCount'].quantile(0.70)#minimum votes required for each recipe
r=no_of_votes['average']#avg of the ratings for each recipe
c=no_of_votes['totalRatingCount'].mean()#mean vote across the whole report
#weighted_average calculation
no_of_votes['weighted_avg']=((r*v)+(c*m))/(v+m)
fdf=no_of_votes.set_index('recipe_id')
#weighted Rate sorted
recipe=fdf.sort_values('weighted_avg',ascending=True)
lists=recipe[['RecipeName','weighted_avg','URL']]
existing_df=lists.head()