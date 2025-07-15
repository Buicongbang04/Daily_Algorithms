# Import necessary libraries
import pandas as pd

# Import necessary libraries
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

# Load the sample dataset (replace with your dataset file)
df = pd.read_csv("example_features_dataset.csv")

# Data preprocessing (cleaning, missing value handling, feature selection)
# Example: Removing rows with missing values
df = df.dropna()

# Assuming your dataset is already preprocessed and features are selected
# Assuming you have selected two features "Feature1" and "Feature2"
data = df[["Feature1", "Feature2"]]

# Apply K-Means clustering to the data
kmeans = KMeans(n_clusters=3)  # Specify the number of clusters
kmeans.fit(data)
df["Cluster"] = kmeans.labels_  # Assign clusters to data points

# Visualize the clusters (optional)
plt.scatter(data["Feature1"], data["Feature2"], c=df["Cluster"], cmap='viridis')
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()

# Evaluate the quality of clusters using silhouette score
silhouette_avg = silhouette_score(data, df['Cluster'])
print("Silhouette Score:", silhouette_avg)

# You can also calculate within-cluster sum of squares (WCSS) to help choose the number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

# Print the WCSS values
print("WCSS:")
for i, value in enumerate(wcss):
    print(f"Cluster {i+1}: {value}")


