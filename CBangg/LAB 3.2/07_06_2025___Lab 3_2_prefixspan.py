# Import necessary libraries
import pandas as pd

# Import necessary libraries
from prefixspan import PrefixSpan

# Load the sample dataset (replace with your dataset file)
df = pd.read_csv("example_sequenceid_dataset.csv")

# Data preprocessing (cleaning, missing value handling, feature selection)
# Example: Removing rows with missing values
df = df.dropna()

# Convert data to a list of sequences
# Assuming your dataset has a column "Actions" with lists of items in each transaction
sequences = df["Actions"].tolist()

# Apply PrefixSpan algorithm to discover sequential patterns
ps = PrefixSpan(sequences)
patterns = ps.frequent(2)  # Discover sequences occurring at least twice

# Print sequential patterns
for pattern in patterns:
    print("Pattern:", pattern)

# Evaluate and filter patterns based on specific criteria
min_support = 2
max_length = 4

filtered_patterns = [pattern for pattern in patterns if pattern[0] >= min_support and pattern[0] <= max_length]

# Print the filtered patterns
print("Filtered Sequential Patterns:")
for pattern in filtered_patterns:
    print("Pattern:", pattern[0], "Support:", pattern[1])

