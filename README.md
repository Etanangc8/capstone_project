# Beer Recommender System
## Problem Statement
Can we recommend 5 similar beers based on your preference in taste, aroma, appearance, and even your palate? 

Original [dataset](https://www.kaggle.com/rdoume/beerreviews?select=beer_reviews.csv) was downloaded from Kaggle. 1.5 Million user ratings (171 MB). Only used 1% random sample of data. 

The dataset includes a large variety of unique beers that were rated from thousands of unique users. Users rated each beer based on the following criteria: 
- Aroma
- Palate
- Taste
- Appearance
- Overall Rating

Each category can be rated anywhere between 1 (bad, not good, not preferred) and 5 (good, preferred). 

The output will be about 5-7 beer recommendations based on the criteria provided (above).

## Cluster & Recommender System
Used KMeans & DBSCAN to try to produce the best silhouette score. KMeans had a lower score than DBSCAN every time. However, KMeans had less clusters. DBSCAN received higher silhouette scores, however it would produce hundreds of clusters. 

Used KNN to evaluate the model. Used KMeans data to feed into recommender system. 

Recommender system used Sci-Kit Learn's Pairwise_distances & cosine_similarity

## Next Steps
- Completion of the Flask Application for full functionality
- Scrape my own data for more current data
- Use the Surprise Library as the alternative to Pairwise distribution & Cosine Similarity, for the recommender. For further documentation [Surprise Library](http://surpriselib.com/)

## Further Plans for This Project:
- Create and use own dataset by creating my own survey
- Implement a music genre recommender to the beer recommender 
**For Example: Input: preferred music genre (“I am currently listening to jazz”)
               Output: recommended beer style (i.e. Pale Ale, IPA, etc.)**



