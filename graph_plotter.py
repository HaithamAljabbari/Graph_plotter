import matplotlib.pyplot as plt

def plot_graph(x_values, y_values, x_label, y_label, title):
    plt.plot(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

# Get user input
x_str = input("Enter x values (comma-separated): ")
y_str = input("Enter y values (comma-separated): ")
x_label = input("Enter x-axis label: ")
y_label = input("Enter y-axis label: ")
title = input("Enter graph title: ")

# Convert input strings to lists
x = [float(value) for value in x_str.split(",")]
y = [float(value) for value in y_str.split(",")]

# Call the plot_graph function with user input
plot_graph(x, y, x_label, y_label, title)
