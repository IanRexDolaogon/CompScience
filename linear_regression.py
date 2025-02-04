x = [
    [1, 2, 8, 1],
    [1, 3, 7, 2],
    [1, 4, 6, 2],
    [1, 5, 7, 3],
    [1, 6, 8, 4]
]

y = [50, 60, 70, 80, 90]

beta = [0, 0, 0, 0]

alpha = 0.01
e = 1000
m = len(y)

for _ in range(e):
    y_predictions = [beta[0] + beta[1] * x[i][1] + beta[2] * x[i][2] + beta[3] * x[i][3] for i in range(m)]
    error = [y_predictions[i] - y[i] for i in range(m)]

    beta[0] -= alpha * (1/m) * sum(error)
    beta[1] -= alpha * (1/m) * sum(error[i] * x[i][1] for i in range(m))
    beta[2] -= alpha * (1/m) * sum(error[i] * x[i][2] for i in range(m))
    beta[3] -= alpha * (1/m) * sum(error[i] * x[i][3] for i in range(m))

print(f"Coeficients: b0 = {beta[0]}, b1 = {beta[1]}, b2 = {beta[2]}, b3 = {beta[3]}")

def predict_result(hours_studied, sleep_hours, reviews):
    return beta[0] + beta[1] * hours_studied + beta[2] * sleep_hours + beta[3] * reviews

new_data = [4, 7, 3]

predict_score = predict_result(new_data[0], new_data[1], new_data[2])
print(f"Predicted Exam Score: {predict_score}")
