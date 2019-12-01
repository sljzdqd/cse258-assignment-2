# cse258-assignment-2

[Amazon Review Data (Office Product)](http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Office_Products_5.json.gz)

1. Make a folder called `data`
2. Download the .json.gz using above link into `data`

## baseline v0

1. Extract review from data
2. Generate label (0,1) for each review. Rating 1-3 => 0; rating 4-5 => 1.
3. Shuffle data and split train, dev and test data. (train: 70%, dev: 15%, test: 15%)
4. Generate X vector by count vector from sklearn.
5. Fit X vector and labels into logistic regression.
6. Use class_weight='balanced' and get accuract 0.88.

## baseline v1

1. Build new balanced train, dev and test data. The ratio between positive and negative sample is 1:1.
2. Fit the new data into logistic regression model.
3. The accuracy is 0.85.

## rating baseline
1. Build balanced train, dev and test data. The number of rating 4 and 5 is still slightly bigger than other rating.
2. Fit into linear regression model.
3. Use MSE as evaluation metric. The MSE is 1.48.

## rating-latent factor model
1. Simple (bias only) latent factor-based recommender: MSE 1.289
2. Complete latent factor-based recommender: MSE 1.289

## rating-BPR model(The implementation of the model is from Cornac)
1. Constuct object train_set from train data and Cornac Dataset class
2. Train the BPR model
3. Predict using predict_rating() function. MSE: 0.845
