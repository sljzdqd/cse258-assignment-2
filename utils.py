###########################################################
# Author: @Jun0413
# 
# Utility functions for data preprocessing & analytics
###########################################################
import argparse
import gzip
import json
import pandas as pd


"""
Load data from .gz into data frames
"""
def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)


def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')



"""
Prepare text data for sentimental analysis

E.g.
Given fn.json with rating from 1 to 3,
generate fn_1.
"""
def clean_text(text):
    return text.replace('\n', '')


def extract_review_text(path):
    df = getDF(path)
    dir = path.strip('.json.gz')

    # [1.0, 2.0, 3.0, 4.0, 5.0]
    rating_vals = set(df['overall'].tolist())
    print('Ratings are: {}'.format(rating_vals))

    fps = {r: open('%s_%s.txt'%(dir,str(r)), 'w') for r in rating_vals}
    for r in rating_vals:
      reviews = set(df[df['overall']==r]['reviewText'].values) #TODO: why duplicates?
      print('Extracting reviews for rating {}'.format(r))
      for review in reviews:
        fps[r].write(clean_text(review) + '\n')

    for r in fps:
      fps[r].close()
    
    print('Finish extracting reviews!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='path to *.json.gz')
    args = parser.parse_args()
    extract_review_text(args.path)
    pass