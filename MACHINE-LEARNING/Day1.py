# what is machine learning
# Ml is a branch of AI that enables system to learn from data and improve their performance over time without being explicitly programmed.

# diff btw supervised or unsupervised learning
# supervised learning:- algorithm learns from labeled data. it aims to learn a mapping function from input variables to output variables
# unsupervised learning:- it deals with unlabeled data, where algorithm tries to patterns or structures present in the input data without any explicit feedback.

# bias variance tradeoff:- its refers to an dilemma in ML where increasing model complexity(reducing bias) typically leads to increase in variance and vice versa. a blance mut be struck to minimize both sources of error for optimal model performance

# types of ML
# 1- supervised learning(eg. regression, classification)
# 2- unsupervised learning(eg. clustering, dimensionality, reduction)
# 3- reinforcement learning(eg. learning from interaction with an environment)

# steps involved in ML project
# • data collection
# • data processing(cleaning, transformation, normalization)
# • feature engineering(selecting or creating relevant features)
# • model selection and training
# • evaluation(using metrices like accuracy, precision, recall)
# • tuning(optimizing hypermeters)
# • deployment and monitoring

# overfitting and how to prevent it?
# overfitting occurs when a model learns too well from noise or specific details in the training data, leading to poor generalization on new data. to prevent overfitting, techniques like cross-validation, regularization(eg. L1/L2 regularization), and using more data or simpler models can be employed

# cross-validation
# it is technique used to assess how well a model generalizes to an independent dataset. it involves partitioning the data into subsets., training the model on some subsets and validating it on the remaining subset. this process helps to estimate the model performance and identify potential issues like overfitting

# feature scaling:- Feature scaling is important in machine learning to ensure that features contribute equally to the model training process. It helps algorithms that are sensitive to the scale of input features (e.g., gradient descent-based algorithms) converge faster and perform better.

# role of regularization:- Regularization is a technique used to prevent overfitting by adding a penalty term to the model's loss function. It discourages the model from fitting the training data too closely and encourages simpler models that generalize better to unseen data. L1 (Lasso) and L2 (Ridge) regularization are common techniques used in linear models

# supervised learning:- Supervised Learning is a type of machine learning where algorithms learn from labeled data, making predictions or decisions based on input-output pairs.

# regression:- Regression predicts continuous outputs (e.g., predicting house prices)
# Classification:- Classification predicts discrete labels (e.g., spam detection).

# bias-variance tradeoff:- Bias measures how well a model approximates the true relationship between inputs and outputs. Variance measures how much the model's predictions vary with different training datasets. Tradeoff refers to the challenge of minimizing both bias and variance simultaneously to achieve optimal model performance.

# common algorithm used in supervised learning is:-  Linear Regression, Logistic Regression, Decision Trees, Support Vector Machines (SVM), Naive Bayes, K-Nearest Neighbors (KNN), and Neural Networks

# Cross-Validation:- Cross-Validation is a technique to assess how the results of a statistical analysis will generalize to an independent dataset. It helps in evaluating model performance by training and testing on different subsets of the data, ensuring the model doesn't overfit or underfit.

# Overfitting:- Overfitting occurs when a model learns too much noise from the training data, leading to poor performance on new data. Techniques to prevent overfitting include using simpler models, regularization (e.g., L2 regularization), and cross-validation.

# Confusion Matrix:- A Confusion Matrix is a table used to evaluate the performance of a classification model. It summarizes the number of correct and incorrect predictions, breaking them down by class.

# purpose of feature scaling:- Feature Scaling ensures that numeric features are on a similar scale, preventing features with larger ranges from dominating the learning process. Common techniques include Normalization (scaling features to a [0, 1] range) and Standardization (scaling features to have a mean of 0 and a standard deviation of 1).