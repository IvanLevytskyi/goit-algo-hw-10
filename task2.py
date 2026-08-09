import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

NUMBER_OF_POINTS = 5000

def f(x):
    """The function to be integrated"""
    return x ** 3 + x ** 2

def f_antiderivative(x):
    """Antiderivative of f(x)"""
    return (x ** 4) / 4 + (x ** 3) / 3

def integrate_analytically(func, a, b):
    """A function for analytical integration"""
    return func(b) - func(a)

def integrate_scipy(func, a, b):
    """A function for integration using SciPy"""
    result, error = spi.quad(func, a, b)
    return result

def draw_graph(func, a, b, points_inside, points_outside):
    """A function for plotting a graph"""
    # Creating a range of values for x and y
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = func(x)

    # Creating a graph
    fig, ax = plt.subplots()

    # Graphing a function
    ax.plot(x, y, 'r', linewidth=2)

    # Filling the area under the curve
    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    
    # Plotting points from the Monte Carlo method
    points_inside_x, points_inside_y = zip(*points_inside)
    ax.scatter(points_inside_x, points_inside_y, color='blue', s=20)
    
    points_outside_x, points_outside_y = zip(*points_outside)
    ax.scatter(points_outside_x, points_outside_y, color='yellow', s=20)

    # Graph configuration
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Adding integration limits and a graph title
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^3 + x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()
    
def is_inside(func, x, y):
    """Checks whether the point (x, y) lies below the curve"""
    return y <= func(x)

def monte_carlo_method(func, width, height):
    """Monte Carlo method"""
    # Generating random points
    points = [(random.uniform(0, width), random.uniform(0, height)) for _ in range(NUMBER_OF_POINTS)]

    # Selecting points below and above the curve
    points_inside = [point for point in points if is_inside(func, point[0], point[1])]
    points_outside = [point for point in points if not is_inside(func, point[0], point[1])]

    # Number of points below the curve
    M = len(points_inside)

    # Area calculated using the Monte Carlo method
    Sm = (M / NUMBER_OF_POINTS) * (width * height)

    return Sm, points_inside, points_outside

def main():
    # Limits of integration
    a = 0  # Lower bound
    b = 2  # Upper bound

    integral_mc, points_inside, points_outside = monte_carlo_method(f, 2, 12.5)

    print(f"Integral calculated using SciPy: {integrate_scipy(f, a, b)}")
    print(f"Integral calculated analytically: {integrate_analytically(f_antiderivative, a, b)}")
    print(f"Integral calculated using the Monte Carlo method: {integral_mc}")
    
    draw_graph(f, a, b, points_inside, points_outside)

if __name__ == "__main__":
    main()
