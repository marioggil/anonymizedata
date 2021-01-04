import pandas as pd 
import hashlib

T=pd.read_csv('SalidaCompleta.csv')
df2 = pd.DataFrame(T, columns =['Name', 'link', "DateIn", "allText","Nombre","Ubicacion","Contactos","Descripcion","Resumen","Estudios","Trabajos"]) 
password="Password"
def Anonamize(txt):
    h = hashlib.sha1()
    txt=txt+password
    h.update(txt.encode('utf-8'))
    return h.hexdigest()

df2["Anon"]=df2["link"].apply(Anonamize)
def Limpiezacelda(txt):
    try:
        return txt.replace(";",",")
    except:
        return txt
def LimpiezaParaCSV(dataframe):
    columnas=dataframe.columns
    for i in columnas:
        dataframe[i]=dataframe[i].apply(Limpiezacelda)
    return dataframe
df2=LimpiezaParaCSV(df2)
Tabla1=df2[['Name', 'link','allText', 'Nombre']]
Tabla1=Tabla1.sample(frac = 1).reset_index(drop=True)
Tabla2=df2[['Ubicacion', 'Contactos','Descripcion', 'Resumen', 'Estudios', 'Trabajos', 'Anon',"DateIn"]]#,"Sex"]]
Tabla1.to_csv("NoPublica.csv")
Tabla2.to_csv("Publica.csv")