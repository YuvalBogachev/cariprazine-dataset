from drugscom import DrugsCom
import pandas as pd

# Create scraper iterator and setup dict for dataframe
data = DrugsCom('https://www.drugs.com/comments/cariprazine/')
dict_to_df = {'text': [], 'dosage/duration': [], 'score': [], 'likes': []}

# Iterate over the web pages
for page in data:
    for review in page:
        text, dosage_duration, score, likes = review
        dict_to_df['text'].append(text)
        dict_to_df['dosage/duration'].append(dosage_duration)
        dict_to_df['score'].append(score)
        dict_to_df['likes'].append(likes)

# Export
df = pd.DataFrame(data=dict_to_df)
df.to_csv('cariprazine_data.csv')
df.to_parquet('cariparzine_data.parquet')
