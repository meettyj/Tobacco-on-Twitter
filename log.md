
# Done
- 90-10 train-test set division
- Using AUC and F1 metrics to evaluate the pre-trained model's performance
- Retrain the initial model (from pickle file) and evaluate performance
- Reconstruce the LR model structure in alcohol level 
- Training the LR model and comparing performance with the initial one
- Grid search on LR model
- Cross validation on LR model
- Build SVM and Random Forest model on alcohol dataset
- Evaluate the models (LR, SVM, RF) on first person level
- Evaluate the models (LR, SVM, RF) on behavior level
- Analyse reflective data and achieve how can we divide the data
- Read paper about 'time period in tweets' to see how researchers dealing with the topic
- Summarize what questions do the current survey have.
- Reading paper about "Causal Discovery". Trying to match experiments and define our problem.
- Check Twitter API

# Results
## Alcohol Level
Conclusion: After setting specific parameters of tf-idf. All of these three classifiers achieve almost the same performance. It seems the difference between various classifier is small.
### LR
- Paper: 0.86 in F1, 0.87 in AUC
- Initial model in Testing set:  0.87 in F1, 0.87 in AUC
- Reconstructed model in Testing set:  0.89 in F1, 0.89 in AUC
- It seems the classifier with updated parameters is already the best we can get from grid search. After update specific parameters, model is hard to find the best parameters in grid search.
- cross validation has little effect on the performance. The fit function within the pipeline is robust.
### SVM
- Paper: 0.85 in F1, 0.85 in AUC
- Reconstructed model in Testing set:  0.88 in F1, 0.88 in AUC
### RF
- Paper: 0.82 in F1, 0.84 in AUC
- Reconstructed model in Testing set:  0.87 in F1, 0.86 in AUC

P.S. We can get almost 1 F1 score and AUC score by directly testing performance of initial model (LR) on whole dataset before re-training, which is useless since it was trained on whole dataset. Just for recording.

## First Person Level

### LR
- Paper: 0.76 in F1, 0.70 in AUC
- Reconstructed model in Testing set:  0.79 in F1, 0.74 in AUC

### SVM
- Paper: 0.72 in F1, 0.66 in AUC
- Initial model in Testing set:  0.79 in F1, 0.73 in AUC
- Reconstructed model in Testing set:  0.78 in F1, 0.72 in AUC

### RF
- Paper: 0.77 in F1, 0.63 in AUC
- Reconstructed model in Testing set:  0.74 in F1, 0.66 in AUC
- The performance in training set is really good (almost 1). However, the performance in test set is not so well. Besides, the improvement after parameters updated (from initial model) is small. Maybe grid search and cross validation may help improve the performance

P.S. We can get 0.83 F1 score and 0.84 AUC score by directly testing performance of initial model (SVM) on first Person Level dataset before re-training. Just for recording.

## Behavior Level (current, looking, reflecting)

### LR
- Paper: [0.72, 0.64, 0.53] in F1, [0.81, 0.79, 0.77] in AUC
- Initial model in Testing set:  [0.69, 0.57, 0.40] in F1, [0.75, 0.79, 0.75] in AUC
- Reconstructed model in Testing set: [0.71, 0.58, 0.40] in F1, [0.75, 0.79, 0.75] in AUC
- Conclusion: Actually, I successfully made the performance same as the initial one, but still much lower than paper statement. I have no idea how Jason generate the result in paper. Using the model he leaved and retraining, only got the same performance as what I did in grid search. So weird.

### SVM
- Paper: [0.68, 0.54, 0.44] in F1, [0.78, 0.74, 0.60] in AUC
- Reconstructed model in Testing set: [0.70, 0.57, 0.44] in F1, [0.74, 0.78, 0.74] in AUC

### RF
- Paper: [0.70, 0.53, 0.21] in F1, [0.72, 0.73, 0.55] in AUC
- Reconstructed model in Testing set: [0.72, 0.53, 0.34] in F1, [0.73, 0.76, 0.71] in AUC

## Other thoughts

Maybe we can compare our analysis with the survey report. 
- For the entire 80k tweets data, which is collected in June 2015, maybe we can check the frequency of people drink in a month. (e.g. if the result of our survey is high, we can say the social media is a good resource to reveal people living state)

