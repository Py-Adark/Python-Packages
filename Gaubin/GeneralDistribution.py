class Distribution:
    """Distribution class for calculating and visualizing the Guassian Distribution

   Attributes:
       mean(float): representing the mean of the distribution
       stdev(float): representing the standard deviation of the distribution
       data_list(list): contains floats extracted from a dataset
   """
    def __init__(self, mean=0, stdev=1):
        self.mean = mean
        self.stdev = stdev
        self.data = []

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
