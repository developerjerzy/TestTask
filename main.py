import pandas as pd
import matplotlib.pyplot as plt



class DrawingPlots:
    """Класс для создания графиков переданных объектов

    Параметры:
    path_pandas_json - путь к файлу в формате json для получения входной информации
    columns - название столбца график которого необходимо построить
    path_plots - список для записи и возврата путей сохранения графиков

    если параметр column указан как None, то функция draw_plots построит графики всех столбцов
    и сохранит их в файле all_plots.
    """


    def __init__(self,path_pandas_json, column,path_plots):
        """Конструктор для передачи параметров """
        self.path_pandas_json = path_pandas_json
        self.column = column
        self.path_plots = path_plots


    def draw_plots(self):
        """Функция для рисования графикa столбца, их сохранения и возврата путей"""
        # Чтение файла в формате json
        patients_df = pd.read_json(self.path_pandas_json)
        # рисование графика. параметр plot стоит по умолчанию
        if self.column != None:
            patients_df[self.column].plot()
            # сохранение последнего графика в заданной папке
            plt.savefig(f'plots/{self.column}.pdf', dpi=600)
            # Запись пути к сохраненному графику в массив и возврат массива
            self.path_plots.append('Путь к сохраненному графику:'+f'plots/{self.column}.pdf')
            return self.path_plots
        elif self.column == None:
            patients_df.plot()
            # сохранение последнего графика в заданной папке
            plt.savefig('plots/all_plots.pdf', dpi=600)
            # Запись пути к сохраненному графику в массив и возврат массива
            self.path_plots.append('Путь к сохраненному графику:'+'plots/all_plots.pdf')
            return self.path_plots



















