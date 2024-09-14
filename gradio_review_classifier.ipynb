import gradio as gr
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# List of reviews and their associated ratings
reviews_data = [
    {"review": "The food was amazing and the service was excellent!", "rating": 5},  # Example of a positive review with a high rating
    {"review": "It was okay, not the best experience but not bad.", "rating": 3},   # Neutral review with an average rating
    {"review": "The staff was friendly and the food was delicious.", "rating": 4},  # Positive review with a good rating
    {"review": "The atmosphere was cozy and the food was decent.", "rating": 3},    # Neutral review with a decent rating
    {"review": "The food was terrible, and I had to wait for an hour!", "rating": 1},  # Negative review with a low rating
    {"review": "Nice place, I enjoyed the food and the atmosphere.", "rating": 4},  # Positive review with a good rating
    {"review": "The service was poor, but the food was decent.", "rating": 2}  # Negative review due to poor service, but food was okay
]

# Create a DataFrame from the reviews_data
reviews_df = pd.DataFrame(reviews_data)

def classify_review(user_review):
    # Loop through each review in the reviews_data list
    for review_data in reviews_data:
        # Check if the user's review text is contained in any of the existing reviews (partial match is enough)
        if user_review.lower() in review_data["review"].lower():
            rating = review_data["rating"]  # Get the rating for the matched review
            # If the rating is 4 or higher, classify it as "Positive", otherwise classify as "Negative"
            return "Positive" if rating >= 4 else "Negative"
    return "Review not found."  # If no match is found, return this message

# Plot the distribution of ratings
def plot_rating_distribution():
    # Extract the ratings from the reviews_data
    ratings = [review["rating"] for review in reviews_data]
    plt.figure(figsize=(6, 4))  # Set the size of the plot
    # Create a count plot to show the distribution of ratings (from 1 to 5)
    sns.countplot(x=ratings, order=[1, 2, 3, 4, 5])
    plt.title('Distribution of Ratings')  # Set the plot title
    plt.xlabel('Rating')  # Set the x-axis label
    plt.ylabel('Count')  # Set the y-axis label
    plt.tight_layout()  # Adjust layout to prevent overlap
    return plt.gcf()  # Return the current figure for display

# Function to allow users to preview the dataset as a DataFrame
def preview_dataset():
    return reviews_df  # Return the DataFrame

# Gradio interface for classifying reviews
review_interface = gr.Interface(
    fn=classify_review,  # Function to classify the review
    inputs=gr.Textbox(lines=2, placeholder="Enter your review here", label="Review"),  # Input textbox for the user to enter a review
    outputs="text",  # The output will be displayed as text (either "Positive" or "Negative")
    title="Simple Review Classifier",  # Title of the interface
    description="Enter a review to classify it as positive or negative based on the rating."  # Description of the interface
)

# Gradio interface for plotting the distribution of ratings
plot_interface = gr.Interface(
    fn=plot_rating_distribution,  # Function to generate the plot
    inputs=[],  # No inputs are required for this function
    outputs="plot",  # The output will be a plot showing the rating distribution
    title="Rating Distribution",  # Title of the interface
    description="Shows the distribution of ratings in the dataset."  # Description of the interface
)

# Gradio interface for previewing the dataset as a DataFrame
preview_interface = gr.Interface(
    fn=preview_dataset,
    inputs=[],  # No inputs are required for this function
    outputs="dataframe",  # The output will be a DataFrame
    title="Preview Restaurant Reviews Dataset",
    description="Displays the entire dataset as a DataFrame."
)

# Combine both interfaces (Review Classifier and Rating Distribution) using tabs
tabbed_interface = gr.TabbedInterface(
    [review_interface, plot_interface, preview_interface],  # Add both interfaces to tabs
    ["Review Classifier", "Rating Distribution" , "Dataset Preview"]  # Tab names
)

# Launch the Gradio interface
tabbed_interface.launch()