def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance ** 0.5  

def init_centriod(data, k):
    centriods = []
    used_indices = set()
    while len(centriods) < k:
        index = int(len(data) * (len(centriods) / k))
        if index not in used_indices:
            centriods.append(data[index])
            used_indices.add(index)
    return centriods

def assign_clusters(data, centriods):
    clusters = [[] for _ in range(len(centriods))]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centriods]
        nearest_centroid_index = distances.index(min(distances))
        clusters[nearest_centroid_index].append(point)
    return clusters

def update(clusters):
    centroids = []
    for cluster in clusters:
        if not cluster:
            centroids.append([0] * len(clusters[0][0]))
            continue
        centroid = [0] * len(cluster[0])
        for point in cluster:
            for i in range(len(point)):
                centroid[i] += point[i]
        centroid = [coord / len(cluster) for coord in centroid]
        centroids.append(centroid)
    return centroids

def k_mean(data, k, max=100):
    centroids = init_centriod(data, k)
    
    for _ in range(max):
        clusters = assign_clusters(data, centroids)
        new_centroids = update(clusters)
        
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return clusters, centroids

if __name__ == "__main__":
    # Sample data
    data = [
        [1, 2],
        [2, 3],
        [3, 3],
        [6, 8],
        [7, 8],
        [8, 9]
    ]
    
    # Number of clusters
    k = 2
    
    clusters, centroids = k_mean(data, k)
    
    print("Final Clusters:")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}: {cluster}")
    print("\nFinal Centroids:")
    for i, centroid in enumerate(centroids):
        print(f"Centroid {i + 1}: {centroid}")
