import sys
import os
import colorama 

sys.path.append('../')
from controller.historialComandoDaoControl import HistorialComandoDaoControl
from model.historial_comando import HistorialComando
from controller.historialComandoControl import HistorialComandoControl

colorama.init()

def limpira_consola():
    os.system('cls||cls||clear')

#--------------------------------------------------------------------

if __name__ == "__main__":
    hc = HistorialComandoControl()
    hcd = HistorialComandoDaoControl()
    
    try:
        pass 
        # hcd._historial_comando = HistorialComando() 
        # hcd._historial_comando._id = hc.generate_id()
        # hcd._historial_comando._nombre_comando = "node main.js"
        # hcd.save
        
        # hcd._historial_comando = HistorialComando() 
        # hcd._historial_comando._id = hc.generate_id()
        # hcd._historial_comando._nombre_comando = "node app.js"
        # hcd.save
                

    except Exception as error:
        print(error)
    