# Gaubin Package

This is a package that contains modules for calculating and visualizing both Gaussian and Binomial Distributions.
It can also add two Gaussian and Binomial Distributions 

The Modules contained in this package include:
    * GaussianDistribution
    * BinomialDistribution
    * General Distribution

GaussianDistribution
    Methods:
        1. read_data_file: Function to read data for our Gaussian distribution
        2. calculate_mean: Function to calculate mean for the distribution
        3. calculate_stdev: Function to calculate the standard deviation for the distribution
        4. plot_histogram: Function that plots the Gaussian distribution
        5. pdf: Function to calculate the probability density function for the Gaussian distribution
        6. plot_histogram_pd: Function to plot the histogram for pdf

BionmialDistribution
    Methods:
        1. read_data_file: Function to read data for our Gaussian distribution
        2. calculate_mean: Function to calculate the mean from p and n
        3. calculate_stdev: Function to calculate the standard deviation from p and n.
        4. replace_stat_with_data: Function to calculate p and n from the data set
        5. plot_bar: Function to output a histogram of the instance variable data using
           matplotlib pyplot library.
        5. pdf: Function to calculate the probability density function for the Gaussian distribution
        6. plot_bar_pdf: Function to plot the histogram for pdf
    
Installation:
    Package can be pip installed.