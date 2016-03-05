# Implement Logistic Regression

from data_import import *

"""
Logistic regression finds a relation among the input and the output. You have been given

theta (vector initialised to all zeros)
X (input array/matrix)
Y(output array corresponding to each input).
m is the number of training data.
n is the number of features in the training data.

Feel free to optimise and use upgradations for bonus points.

"""
theta, X, y, m, n = get_data()


def sigmoid(X):
    """
    TODO
        This function calculates the sigmoid and returns the sigmoid output.

    """

    return z


def gradient_descent(theta, X, y):
    """
    TODO
            This function calculates the gradient descent and returns the gradient output.
            It takes as input the theta, X and Y vectors.
            It calculates the partial differential with respect to all the theta[i]s records
            and updates the values of those thetas.
            You have to implement the partial differentials, and return the gradient
            in this function. 

    """

    return grad


def hypothesis(theta, X):
    """
    TODO
            This function takes in the X and theta vector and is responsible for calculating
            (theta).(X) where theta has to be transposed.

            You have to implement this function and return the value of hypothesised 'y'

    """

    return y


def compute_cost(theta, X, y):
    """
    TODO
            This function is calculating the loss for hypopthesis at each
            of the points by tracking the difference between
            their original outputs and their hypothesised outputs.

            Implement this function to return the value of cost as 'J'

    """

    return J


def regularised_cost(X):
    """
    TODO
            Regularisation mostly used with linear regression is l2 regularisation which
            is the sum of squares of all the values in the input matrix.

            Implement the regularised cost function. Choose input and output according
            to your convinience.

    """

    return J


def regularised_gradient_descent(X):
    """
    TODO
            Implement the regularised gradient descent. Choose input and output according
            to your convinience.

    """

    return grad


def predict(x):
    """
    TODO
            once done with the Logistic regression, input another array or numbers to get
            a prediction of outputs.

            return the an array 'y' with the predicted values.

    """

    return y


def plot_graph(X, y, hyp):
    """
    TODO: OPTIONAL

            use matplotlib and ggplot to get a relation among the input and output.
            Plot the relation in a graph.

            Also make a graph of the hypothesis line with the points on the plane.
    """

    pass
