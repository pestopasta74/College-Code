# Standard pi calculation
def standardPiCalc():
    import numpy
    return numpy.pi

# Monte Carlo pi calculation
def monteCarloPiCalc(numPoints):
    import random
    insideCircle = 0
    for _ in range(numPoints):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            insideCircle += 1
    pi = 4 * insideCircle / numPoints
    return pi


# Leibniz pi calculation
def leibnizPiCalc(numTerms):
    pi = 0
    for i in range(numTerms):
        pi += ((-1) ** i) / (2 * i + 1)
    pi *= 4
    return pi


# Wallis pi calculation
def wallisPiCalc(numTerms):
    pi = 2
    for i in range(1, numTerms):
        pi *= (4 * i**2) / (4 * i**2 - 1)
    return pi

# Graph the error values
def graphErrorValues(numIterations, y1, y2, y3):
    import matplotlib.pyplot as plt
    plt.plot(numIterations, y1, label='Monte Carlo')
    plt.plot(numIterations, y2, label='Leibniz')
    plt.plot(numIterations, y3, label='Wallis')
    plt.xlabel('Number of iterations')
    plt.ylabel('Difference from pi (%)')
    plt.title('Difference of pi calculation methods')
    plt.legend()
    plt.show()

def main():
    # Create empty lists
    numIterations = []
    monteCarloError = []
    leibnizError = []
    wallisError = []

    # Calculate pi using standard method
    standardPi = standardPiCalc()

    # Calculate pi using different methods and store the error
    for i in range(2000, 100000, 1000):
        numIterations.append(i)
        monteCarloError.append(calculateError(standardPi, monteCarloPiCalc(i)))
        leibnizError.append(calculateError(standardPi, leibnizPiCalc(i)))
        wallisError.append(calculateError(standardPi, wallisPiCalc(i)))

    graphErrorValues(numIterations, monteCarloError, leibnizError, wallisError)

# Calculate the error
def calculateError(exactValue, approxValue):
    error = ((approxValue - exactValue) / exactValue) * 100
    return error


main()