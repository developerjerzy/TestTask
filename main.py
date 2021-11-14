import pandas as pd
import matplotlib.pyplot as plt



class DrawingPlots:
    """Class for drawing plots.

    Parameters:
    path_pandas_json - path to file json
    columns - name column
    path_plots - list for recording and return path
    """


    def __init__(self,path_pandas_json, column,path_plots):
        """Constructor for recording parameters."""
        self.path_pandas_json = path_pandas_json
        self.column = column
        self.path_plots = path_plots


    def draw_plots(self):
        """Function for drawing """
        # reading file json
        patients_df = pd.read_json(self.path_pandas_json)
        # drawing plots
        if self.column != None:
            patients_df[self.column].plot()
            # save last plot in "plots"
            plt.savefig(f'plots/{self.column}.pdf', dpi=600)
            # recording path in list path plots
            self.path_plots.append('Path to file:'+f'plots/{self.column}.pdf')
            return self.path_plots
        elif self.column == None:
            # if columns == None - function must drawing all plots in the same place
            patients_df.plot()
            plt.savefig('plots/all_plots.pdf', dpi=600)
            self.path_plots.append('Path for file:'+'plots/all_plots.pdf')
            return self.path_plots



















