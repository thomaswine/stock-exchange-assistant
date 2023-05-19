import matplotlib.pyplot as plt

class GraphModule:

    def createGraph(self, x_data, y_data, title, x_name, y_name ):

        tick_label = x_data
        
        plt.bar(x_data, y_data, tick_label = tick_label, width=0.5, color = ['green'])
        
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        
        plt.title(f'{title} Net Income by Quarters')
        
        plt.savefig(f'./Graphs/{title}_net_income.png')
        
        plt.show()