# TODO
- Check the influence of changing location to each notebook
- Evaluate the models (LR, SVM, RF) on first person level
- Analyse reflective data and achieve how can we divide the data
- Read paper about 'time period in tweets' to see how researchers dealing with the topic


# Done
- 90-10 train-test set division
- Using AUC and F1 metrics to evaluate the pre-trained model's performance
- Retrain the initial model (from pickle file) and evaluate performance
- Reconstruce the LR model structure in alcohol level 
- Training the LR model and comparing performance with the initial one
- Grid search on LR model
- Cross validation on LR model
- Build SVM and Random Forest model on alcohol dataset

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

## First Person Level
### LR


