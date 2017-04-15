def hypothesis(x, theta):
	return theta[0] + theta[1] * x


def cost(x, y, theta):
	cost = 0
	m = len(x)
	for i in range(m):
		cost += pow(hypothesis(x[i], theta) - y[i], 2)
	cost /= 2 * m

	return cost


def gradient(x, y, theta):
	grad = [0, 0]
	m = len(x)
	for i in range(m):
		grad[0] += hypothesis(x[i], theta) - y[i]
		grad[1] += (hypothesis(x[i], theta) - y[i]) * x[i]
	grad[0] /= m
	grad[1] /= m

	return grad


def gradientDescent(x, y):
	theta = [1, 1]
	alpha = 0.01		# learning rate
	prevCost = 0
	currCost = 999999
	while abs(currCost - prevCost) > 0.000001:
		prevCost = currCost
		grad = gradient(x, y, theta)
		theta[0] -= alpha * grad[0]
		theta[1] -= alpha * grad[1]
		currCost = cost(x, y, theta)

	return theta + [currCost]


x = list(map(int, input("X = ").split(' ')))
y = list(map(int, input("Y = ").split(' ')))

learnedData = gradientDescent(x, y)

print("\nTheta0 = %f" %learnedData[0])
print("Theta1 = %f" %learnedData[1])
print("Cost = %f" %learnedData[2])
