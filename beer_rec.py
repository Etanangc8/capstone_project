import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity
import sys

#read in data
df = pd.read_csv('./data/km_data.csv')

user_sub = sys.argv[0]

#Lowercased items in 'beer_style' column
df['beer_style'] = df['beer_style'].map(lambda x: x.strip().lower())

pivot = df.pivot_table(index='beer_style', columns='review_profilename', values='km_labels')

pivot_sparse = sparse.csr_matrix(pivot.fillna(0))

#cosine similarity
col_recommender = pairwise_distances(pivot_sparse, metric='cosine')
#new df with pivot sparce
recommender_df = pd.DataFrame(col_recommender, index=pivot.index, columns=pivot.index)

beer_style = df['beer_style']

# def beer_list(search):
#     search = df['beer_style']
#     #for beer in beerlist:
#     return np.random.choice(search, 5, replace=False).tolist()


def recommender(search, recommender_df, itemlist=beer_style):
#     search = search.lower()
#     itemlist = [beer.lower() for beer in itemlist]    
#   beers = km_df[km_df['beer_style'].str.contains(q)]['beer_style']
#     beer_style = km_df['beer_style']
    # beerlist = []
    # for beer in beers:
    #     beers.append(beer)
    # for q in beers:
    #     return np.random.choice(wines_with_words, 5, replace=False).tolist()
    sublist = []  
    for item in itemlist:
        try:
            if item.index(search) >= 0:
                sublist.append(item)
        except:
            pass
    
for i in sublist:
        print(i)
        print('5 Most Similar beers:')
        print(recommender_df.loc[i.lower()].sort_values()[1:6])
        print('')
print(recommender(q, recommender_df))








if __name__ == '__main__':
    user_input = sys.argv[1]


