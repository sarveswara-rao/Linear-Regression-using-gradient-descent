import numpy as np

def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    M = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += (2/M)*((m_current * x + b_current) - y)
        m_gradient += (2/M)*x*((m_current * x + b_current) - y)

    b_new = b_current - learning_rate * b_gradient
    m_new = m_current - learning_rate * m_gradient
    return b_new, m_new
def gradient_descent_runner(points, learning_rate, initial_b, initial_m, num_iterations):
	b = initial_b
	m = initial_m

	for i in range(num_iterations):
		b, m = step_gradient(b, m, np.array(points), learning_rate)
	return [b, m]
def run():
	points = np.genfromtxt('data.csv', delimiter = ',')
	#hyper parameters
	learning_rate = 0.0001
	# y =mx+b
	initial_b = 0
	initial_m = 0
		
	num_iterations = 1000
	[b, m] = gradient_descent_runner(points, learning_rate, initial_b, initial_m, num_iterations)
	print("b: "+str(b)+ " \nm: "+str(m))

if __name__ == '__main__':
	run()