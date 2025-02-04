data = [
    (10, 6, 3, 'Pass'),
    (8, 5, 2, 'Pass'),
    (3, 8, 1, 'Fail'),
    (6, 7, 2, 'Pass'),
    (2, 6, 1, 'Fail')
]

def prior_prob(data, target_class):
    return sum(1 for row in data if row[-1] == target_class) / len(data)

def mean_variance(data, target_class):
    filtered = [row[:-1] for row in data if row[-1] == target_class]
    N = len(filtered)
    means = [sum(feature) / N for feature in zip(*filtered)]
    variances = [sum((x - m) ** 2 for x in feature) / N for feature, m in zip(zip(*filtered), means)]
    return means, variances

def gaus(x, mean, variance):
    if variance == 0:
        return 1 if x == mean else 1e-10
    exponent = ((x - mean) ** 2) / (2 * variance)
    return (2.718 ** -exponent) / (variance ** 0.5 * (2 * 3.1416) ** 0.5)

def posterior_prob(features, data, target_class):
    means, variances = mean_variance(data, target_class)
    prob = prior_prob(data, target_class)
    for i in range(len(features)):
        prob *= gaus(features[i], means[i], variances[i])
    return prob

def predict(features, data):
    return max(set(row[-1] for row in data), key=lambda c: posterior_prob(features, data, c))

test_sample = (5, 6, 2)
print("Predicted Class:", predict(test_sample, data))
