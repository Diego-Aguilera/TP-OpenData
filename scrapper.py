import re
import pandas as pd
from requests_html import HTMLSession

session = HTMLSession()

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


def getdatosconstruccion(url):

    #algoritmo que permite extraer cada columna relevante del html.

    r2 = session.get('https://tembiapo.mopc.gov.py'+url)

    columnas = r2.html.find('.panel-body .form-group')      #separa todas las columnas en una lista

    datos = []

    for columna in columnas:
        dato = ""
        parrafos = columna.find('p')        #extrae el texto de cada columna, pueden haber varios parrafos
        if parrafos == 1:
            datos.append(parrafos[0].text)
        else:
            for parrafo in parrafos:
                dato = dato + parrafo.text
            datos.append(dato)
    return datos


if __name__ == "__main__":
    r = session.get('https://tembiapo.mopc.gov.py')

    main = r.text #pasa a texto la pagina

    list = re.findall(', url: \'(.+?)\'\}\\)\;', main) #busca dentro del texto mediante un patron una lista donde se encuentran
                                                        # las direcciones web de cada punto y los extrae en una lista.
    construcciones = []

    for url in list:
        datos = getdatosconstruccion(url)
        construcciones.append(datos)

    df = pd.DataFrame(construcciones, columns=['NOMBRE', 'TIPO', 'ESTADO', 'DEPARTAMENTO-CIUDAD', 'INFORMACION', 'CONTRATISTA', 'EXTENSION', 'LOCALIDADES', 'INICIO', 'FIN', 'PLAZO', 'AVANCE', 'FINANCIACION', 'INVERSION'])
    df.to_csv('result.csv', float_format='%.2f', line_terminator='\n', index=False)

    print(construcciones)
