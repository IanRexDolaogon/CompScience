def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance ** 0.5  

def k_nearest_neighbors(training_data, test_point, k):
    distances = []
    for train_point, label in training_data:
        dist = euclidean_distance(test_point, train_point)
        distances.append((dist, label))
    
    n = len(distances)
    for i in range(n):
        for j in range(0, n-i-1):
            if distances[j][0] > distances[j+1][0]:
                distances[j], distances[j+1] = distances[j+1], distances[j]
    k_nearest = distances[:k]
    
   
    class_votes = {}
    for dist, label in k_nearest:
        if label in class_votes:
            class_votes[label] += 1
        else:
            class_votes[label] = 1
    
    # Return the class with the most votes
    max_votes = 0
    predicted_class = None
    for label, votes in class_votes.items():
        if votes > max_votes:
            max_votes = votes
            predicted_class = label
    return predicted_class

if __name__ == "__main__":
    training_data = [
        ([1, 2], 0),
        ([2, 3], 0),
        ([3, 3], 0),
        ([6, 8], 1),
        ([7, 8], 1),
        ([8, 9], 1)
    ]
    

    test = [5, 7]
    
    k = 3
    
    predicted_class = k_nearest_neighbors(training_data, test, k)
    print(f"The predicted class for the test point {test} is: {predicted_class}")