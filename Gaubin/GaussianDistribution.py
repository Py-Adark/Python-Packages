import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

class Gaussian(Distribution):
    """Gaussian class for calculating and visualizing the Guassian Distribution

    Attributes:
        mean(float): representing the mean of the distribution
        stdev(float): representing the standard deviation of the distribution
        data_list(list): contains floats extracted from a dataset
    """

    def __init__(self, mean=0, stdev=1):
        Distribution.__init__(self, mean, stdev)

    def calculate_mean(self):
        """Function to calculate mean for the distribution

        Arg:
            None

        Attributes:
            None

        Returns:
            float: mean of the data
        """
        average = 1.0 * sum(self.data) / len(self.data)
        self.mean = average
        return self.mean

    def calculate_stdev(self, sample=True):
        """Function to calculate the standard deviation for the distribution

        Arg:
            sample

        Attributes:
            None

        Returns:
            float: standard deviation for the data
        """
        if sample:
            N = len(self.data) - 1
        else:
            N = len(self.data)

        mean = self.mean
        my_list = [(x - mean) ** 2 for x in self.data]
        standard_deviation = math.sqrt(sum(my_list) / N)
        self.stdev = standard_deviation

        return self.stdev

    def read_data_file(self, file_name, sample=True):
        """Function to read data for our Gaussian distribution
        Arg:
            file_name(str): name of file to read from

        Returns:
            None
        """
        with open(file_name) as my_file:
            data_list = []
            line = my_file.readline()
            while line:
                data_list.append(int(line))
                line = my_file.readline()
        my_file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """Function that plots the Gaussian distribution
        Arg:
            None

        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('Data')
        plt.ylabel('Count')

    def pdf(self, x):
        """Function to calculate the pdf for the Gaussian distribution
        Arg:
            x(float): point for calculating the pdf

        Returns:
            float: pdf output
        """
        pd = (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * (((x - self.mean) / self.stdev) ** 2))
        return pd

    def plot_histogram_pd(self, n_spaces = 50):
        """Function to plot the histogram for pdf

        Arg:
            n_spaces(int): number of data points

        Returns:
            List(x, y): x and y values for the plot
        """

        mean = self.mean
        stdev = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):
        """Function to add two Gaussian distributions

        Arg:
            other(Gaussian distribution): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution
        """
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt((self.stdev ** 2) + (other.stdev ** 2))

        return result

    def __repr__(self):
        """Function to output Gaussian Characteristics

        Arg:
            None

        Returns:
            string
        """
        return 'Mean: {}   Standard Deviation: {}'.format(self.mean, self.stdev)



