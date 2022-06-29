import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Grafico:
    
    def __init__(self,df: object, utensilio: str, nombre_mp: str):
        self.df = df
        self.utensilio = utensilio
        self.nombre_mp = nombre_mp
        
    def graficar(self):
        data = self.df[(self.df['Utensilio'] == self.utensilio)&(self.df['Nombre MP'] == self.nombre_mp)]
        pp = data['Peso perdida']
        pt = data['Perdida teorica']
        dif = data['Muestreo ']
        fig, ax = plt.subplots()
        sns.scatterplot(x=pp,y=pp.index,alpha=0.8,hue=dif)
        ax.axvline(x=np.mean(pp),color='red',linestyle='--',label='Promedio real '+str(round(np.mean(pp)*1000,0))+' gr')
        ax.axvline(x=np.mean(pt),color='green',linestyle='--',label='Peso teorico '+str(round(np.mean(pt)*1000,0))+' gr')
        ax.set_title(str(self.nombre_mp)+' - '+str(self.utensilio),size=16)
        ax.set_xlabel('gr',size=18)
        ax.set_ylabel('Muestras',size=18)
        ax.legend()
        ax.grid()
        plt.show()
    
def run():
    df = pd.read_excel('Muestras_planta.xlsx')
    M1 = Grafico(df, 'Bacha rectangular grande', 'Crema pastelera naranja mel').graficar()

if __name__ == '__main__':
    run()