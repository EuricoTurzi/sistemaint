import pandas as pd


atualizaçao = pd.read_excel(r"C:\Users\sidnei\Desktop\iccid\Atualizaçao BI 16.08 v01.xlsx")
amarela = pd.read_excel(r"C:\Users\sidnei\Desktop\iccid\COPIA PLANILHA GERAL AMARELA.xlsx")


atualizacao = atualizaçao [['ID','DATA SAIDA / ORIGEM' ,'DATA ENTRADA / DESTINO']]
amarela = amarela [['ID','Data - Ligado','Data - Abertura de Porta']]

if 'ID' in amarela.columns and 'ID' in atualizacao.columns:
    print('ok')
    # Mesclando as tabelas com base no 'ID'
    mesclado = amarela.merge(atualizacao, on='ID', how='left')

    # Identificando IDs duplicados
    duplicadas = mesclado[mesclado.duplicated('ID', keep=False)]

    # Criando a coluna 'DUPLICADA' que contém as datas dos IDs duplicados
    mesclado['DUPLICADA'] = duplicadas['DATA SAIDA / ORIGEM'].astype(str) + ' / ' + duplicadas['DATA ENTRADA / DESTINO'].astype(str)
    mesclado['DUPLICADA'] = duplicadas['Data - Abertura de Porta'].astype(str) + ' / ' + duplicadas['Data - Abertura de Porta'].astype(str)

    print(mesclado)
    # Salvando o resultado em um novo arquivo Excel
    mesclado.to_excel('teste2.xlsx', index=False)
else:
    print('erro')