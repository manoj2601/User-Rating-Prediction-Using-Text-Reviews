# User-Rating-Prediction-Using-Text-Reviews
Implementation of a Naive Bayes classification model to predict Yelp ratings from text reviews.  
  

### Problem Statement : (Text Classification)

In this problem, we will use the Naı̈ve Bayes algorithm for text classification. The dataset for this problem is a subset of the Yelp dataset and has been obtained from this website ([https://www.yelp.com/dataset]). Given a users review, task is to predict the stars given by the reviewer. Read the website for more details about the dataset. You have been provided with separate training and test files containing 534K reviews (samples) and 133K reviews respectively. Data is available at this link ([https://csciitd.sharepoint.com/sites/2001-COL774MACHINELEARNING2/Class%20Materials/A2/col774_yelp_data.zip]). A review comes from one of the five categories (class label). Here, class label represents stars given by the user along with the review. Please refer to README in data directory for more details.

1. Implement the Naı̈ve Bayes algorithm to classify each of the articles into one of the given categories. Report the accuracy over the training as well as the test set. In the remaining parts below, we will only worry about test accuracy.  
Notes:  
	* Make sure to use the Laplace smoothing for Naı̈ve Bayes (as discussed in class) to avoid any zero probabilities. Use c = 1.
	* You should implement your algorithm using logarithms to avoid underflow issues.
	* You should implement Naı̈ve Bayes from the first principles and not use any existing Matlab/Python modules.
2. What is the test set accuracy that you would obtain by randomly guessing one of the categories as the target class for each of the review (random prediction). What accuracy would you obtain if you simply predicted the class which occurs most of the times in the training data (majority prediction)? How much improvement does your algorithm give over the random/majority baseline?
3. Read about the confusion matrix. Draw the confusion matrix for your results in the part (a) above (for the test data only). Which category has the highest value of the diagonal entry? What does that mean? What other observations can you draw from the confusion matrix? Include the
confusion matrix in your submission and explain your observations.
4. The dataset provided to is in the raw format i.e., it has all the words appearing in the original set of articles. This includes words such as ‘of’, ‘the’, ‘and’ etc. (called stopwords). Presumably, these words may not be relevant for classification. In fact, their presence can sometimes hurt the performance of the classifier by introducing noise in the data. Similarly, the raw data treats different forms of the same word separately, e.g., ‘eating’ and ‘eat’ would be treated as separate words. Merging such variations into a single word is called stemming.  
	* Read about stopword removal and stemming (for text classification) online.
	* Use the script provided with the data to you to perform stemming and remove the stop-words in the training as well as the test data. You are free to use other tools as well.
	* Learn a new model on the transformed data. Again, report the accuracy.
	* How does your accuracy change over test set? Comment on your observations.

5. Feature engineering is an essential component of Machine Learning. It refers to the process of manipulating existing features/constructing new features in order to help improve the overall accuracy on the prediction task. For example, instead of using each word as a feature, you may treat bi-grams (two consecutive words) as a feature. Come up with at least two alternative features and learn a new model based on those features. Add them on top of your model obtained in part (d) above. Compare with the test set accuracy that you obtained in parts (a) and parts (d). Which features help you improve the overall accuracy? Comment on your observations.  
  

Implemented by:  
Manoj Kumar