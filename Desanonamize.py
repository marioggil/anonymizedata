import pandas as pd 
import hashlib

#Desanonamize dataset
password="Password"
def Anonamize(txt):
    h = hashlib.sha1()
    txt=txt+password
    h.update(txt.encode('utf-8'))
    return h.hexdigest()

def FusionBases(Publica,NoPublica):
    Pub = pd.read_csv(Publica)
    NoPub = pd.read_csv(NoPublica)
    NoPub["Anon"] = NoPub["link"].apply(Anonamize)
    result = pd.merge(NoPub,Pub, on="Anon")
    return result

F=FusionBases("Publica.csv","NoPublica.csv")
F.to_csv("Fus.csv")