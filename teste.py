import pandas as pd
import openpyxl


gerais = pd.read_excel(r"C:\Users\sidnei\Desktop\iccid\IDS Gerais 24.07.24.xlsx")
pra_corte = pd.read_excel(r"C:\Users\sidnei\Desktop\iccid\JCLOG 13.08.24.xlsx")

print(pra_corte)
gerais = gerais[['ID','ICCID']]
print(gerais)

pra_corte = pra_corte[['ID','ICCID']]
print(pra_corte)
pra_corte.rename(columns={'Id':'ID'})
print(pra_corte)

if 'ID' in gerais.columns and  'ID' in pra_corte.columns:
    print('ok')
    mesclado = pra_corte.merge(gerais, on='ID')
    print(mesclado)
    mesclado.to_excel('teste.xlsx',index=False)
else:
    print('erro')

