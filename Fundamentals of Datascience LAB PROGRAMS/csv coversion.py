import pandas as pd

# Sample customer feedback dataset
feedback_data = [
    "Great product, I love it!",
    "The service was terrible.",
    "This is exactly what I needed.",
    "Could be better.",
    "I'm satisfied with my purchase.",
    "Not recommended."
]

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame({'feedback': feedback_data})
df.to_csv('data.csv', index=False)
