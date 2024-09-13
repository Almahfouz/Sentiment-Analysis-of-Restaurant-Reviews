# Sentiment-Analysis-of-Restaurant-Reviews-Using-Hugging-Face-and-Gradio

This project demonstrates the integration of Hugging Face's sentiment analysis models with Gradio to classify restaurant reviews and visualize review ratings. Users can submit a restaurant review and receive a predicted rating, a classification of the review's sentiment (positive or negative), and an accuracy score.

## Key Features:
- **Sentiment Classification**: Classifies reviews as positive or negative using a Hugging Face model (`distilbert-base-uncased-finetuned-sst-2-english`).
- **Rating Prediction**: Predicts the rating based on fuzzy matching with pre-existing review data.
- **Review Search**: Uses fuzzy matching to find the best matching review from the dataset.
- **Rating Distribution**: Visualizes the distribution of ratings in the dataset.

## Components:
- **`basic_sentiment_analysis.py`**: Demonstrates basic sentiment analysis using a Hugging Face pipeline on two sample reviews.
- **`gradio_review_classifier.py`**: Implements a simple Gradio interface with hardcoded reviews and their ratings.
- **`full_review_sentiment_analysis.py`**: Full implementation with Gradio integration, performing both sentiment analysis and review classification using the dataset.
- **`Restaurant_reviews.csv`**: The dataset containing restaurant reviews and ratings.

## Installation

### Requirements:
- Python 3.x
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/Almahfouz/Sentiment-Analysis-of-Restaurant-Reviews
   cd Sentiment-Analysis-of-Restaurant-Reviews
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the full implementation with Gradio:
   ```bash
   python full_review_sentiment_analysis.py
   ```

4. Link to the Hugging Face Space: [Sentiment Analysis of Restaurant Reviews](https://huggingface.co/spaces/Almahfouz/Sentiment-Analysis-of-Restaurant-Reviews-Using-Hugging-Face-and-Gradio)


## Usage:
- **Submit a review**: Enter a restaurant review in the Gradio interface. The system will provide:
  - A predicted rating based on fuzzy matching with existing reviews.
  - Sentiment classification (positive/negative) using Hugging Face.
  - Confidence score for the sentiment analysis.

- **Rating distribution**: The app also shows a visual distribution of the ratings from the dataset.

## Expected Outputs:
- When a user submits a review, the Gradio interface returns:
  - **Predicted Rating**: 1 to 5 based on review match.
  - **Sentiment Classification**: Positive or negative sentiment prediction.
  - **Confidence Score**: Accuracy of the model's sentiment prediction.

## Dataset:
- **Restaurant_reviews.csv**: The dataset used in this project contains the following columns:
  - **Restaurant**: Name of the restaurant.
  - **Reviewer**: Name of the reviewer.
  - **Review**: Text of the review.
  - **Rating**: Rating given by the reviewer (1-5).
  - **Metadata**: Additional details like the number of reviews and followers.
  - **Time**: Date and time of the review.
  - **Pictures**: Number of pictures associated with the review.

## Video Walkthrough:
[Link to the video walkthrough] – A 3-5 minute video showing how the project works and a detailed walkthrough of the Gradio interface.

---

### License:
This project is licensed under the MIT License - see the LICENSE file for details.

### Author:
Created by Abdullah, and Faisal (GitHub: [Almahfouz](https://github.com/Almahfouz))

