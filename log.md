# TODO
- Build SVM and Random Forest model on alcohol dataset
- Evaluate the models (LR, SVM, RF) on first person level
- Analyse reflective data and achieve how can we divide the data
- Read paper about 'time period in tweets' to see how researchers dealing with the topic


# Done
- 90-10 train-test set division
- Using AUC and F1 metrics to evaluate the pre-trained model's performance
- Retrain the initial model (from pickle file) and evaluate performance
- Reconstruce the LR model structure in alcohol level 
- Training the LR model and comparing performance with the initial one

# Results
## LR
- Paper: 0.86 in F1, 0.87 in AUC
- Initial model in Testing set:  0.87 in F1, 0.81 in AUC
- Reconstructed model in Testing set:  0.89 in F1, 0.82 in AUC
