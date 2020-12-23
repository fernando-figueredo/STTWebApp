# Funções de teste
def calcula_delecor(nmissio):
    return(int(nmissio/2))


def calcula_delefaz(nmissio):
    return(int(nmissio/4))


def calcula_aqa(nmissio):
    return(int(nmissio/8))


def calcula_gru(nmissio):
    return(int(nmissio/2-nmissio/4-nmissio/8)+1)


def dobro(valor):
    return (valor*3)
# Fim das funções de teste


def nomeDelegacia(op):

    if op == '1':
        delegacia = "AQA"

    elif op == '2':
        delegacia = "ARU"

    elif op == '3':
        delegacia = "BRU"

    elif op == '4':
        delegacia = "CAS"

    elif op == '5':
        delegacia = "CZO"

    elif op == '6':
        delegacia = "JLS"

    elif op == '7':
        delegacia = "MII"

    elif op == '8':
        delegacia = "PCA"

    elif op == '9':
        delegacia = "PDE"

    elif op == '10':
        delegacia = "RPO"

    elif op == '11':
        delegacia = "SJE"

    elif op == '12':
        delegacia = "SJK"

    elif op == '13':
        delegacia = "SSB"

    elif op == '14':
        delegacia = "STS"

    elif op == '15':
        delegacia = "SOD"

    elif op == '16':
        delegacia = "DELECOR"

    elif op == '17':
        delegacia = "DELEFAZ"

    elif op == '18':
        delegacia = "DELEMAPH"

    elif op == '20':
        delegacia = "DELEPREV"

    elif op == '22':
        delegacia = "DRE"

    elif op == '23':
        delegacia = "GRCC"

    elif op == '24':
        delegacia = "CONGONHAS"

    elif op == '25':
        delegacia = "GUARULHOS"

    return(delegacia)


def carregaPlanilha(opcao, plan):
    import pandas as pd
    import numpy as np

    if opcao == '1':
        endereco = 'controle_efetivo/data/excel/01 Efetivo DPF AQA/Efetivo Unidade AQA.xlsx'

    elif opcao == '2':
        endereco = 'controle_efetivo/data/excel/02 Efetivo DPF ARU/Efetivo Unidade ARU.xlsx'

    elif opcao == '3':
        endereco = 'controle_efetivo/data/Excel/03 Efetivo DPF BRU/Efetivo Unidade BRU.xlsx'

    elif opcao == '4':
        endereco = 'controle_efetivo/data/excel/04 Efetivo DPF CAS/Efetivo Unidade CAS.xlsx'

    elif opcao == '5':
        endereco = 'controle_efetivo/data/excel/05 Efetivo DPF CZO/Efetivo Unidade CZO.xlsx'

    elif opcao == '6':
        endereco = 'controle_efetivo/data/Excel/06 Efetivo DPF JLS/Efetivo Unidade JLS.xlsx'

    elif opcao == '7':
        endereco = 'controle_efetivo/data/excel/07 Efetivo DPF MII/Efetivo Unidade MII.xlsx'

    elif opcao == '8':
        endereco = 'controle_efetivo/data/Excel/08 Efetivo DPF PCA/Efetivo Unidade PCA.xlsx'

    elif opcao == '9':
        endereco = 'controle_efetivo/data/excel/09 Efetivo DPF PDE/Efetivo Unidade PDE.xlsx'

    elif opcao == '10':
        endereco = 'controle_efetivo/data/excel/10 Efetivo DPF RPO/Efetivo Unidade RPO.xlsx'

    elif opcao == '11':
        endereco = 'controle_efetivo/data/Excel/11 Efetivo DPF SJE/Efetivo Unidade SJE.xlsx'

    elif opcao == '12':
        endereco = 'controle_efetivo/data/excel/12 Efetivo DPF SJK/Efetivo Unidade SJK.xlsx'

    elif opcao == '13':
        endereco = 'controle_efetivo/data/Excel/13 Efetivo DPF SSB/Efetivo Unidade SSB.xlsx'

    elif opcao == '14':
        endereco = 'controle_efetivo/data/excel/14 Efetivo DPF STS/Efetivo Unidade STS.xlsx'

    elif opcao == '15':
        endereco = 'controle_efetivo/data/excel/15 Efetivo DPF SOD/Efetivo Unidade SOD.xlsx'

    elif opcao == '16':
        endereco = 'controle_efetivo/data/Excel/16 Efetivo DPF DELECOR/Efetivo Unidade DELECOR.xlsx'

    elif opcao == '17':
        endereco = 'controle_efetivo/data/excel/17 Efetivo DPF DELEFAZ/Efetivo Unidade DELEFAZ.xlsx'

    elif opcao == '18':
        endereco = 'controle_efetivo/data/Excel/18 Efetivo DPF DELEMAPH/Efetivo Unidade DELEMAPH.xlsx'

    elif opcao == '20':
        endereco = 'controle_efetivo/data/excel/20 Efetivo DPF DELEPREV/Efetivo Unidade DELEPREV.xlsx'

    elif opcao == '22':
        endereco = 'controle_efetivo/data/excel/22 Efetivo DPF DRE/Efetivo Unidade DRE.xlsx'

    elif opcao == '23':
        endereco = 'controle_efetivo/data/Excel/23 Efetivo DPF GRCC/Efetivo Unidade GRCC.xlsx'

    elif opcao == '24':
        endereco = 'controle_efetivo/data/excel/24 Efetivo DPF CONGONHAS/Efetivo Unidade CONGONHAS.xlsx'

    elif opcao == '25':
        endereco = 'controle_efetivo/data/Excel/25 Efetivo DPF GUARULHOS/Efetivo Unidade GUARULHOS.xlsx'

    if plan == '1':
        nomePlanilha = 'Efetivo'
        intervaloColunas = 'D:M'
        pularLinha = 4

    if plan == '2':
        nomePlanilha = 'Missão na Unidade'
        intervaloColunas = 'D:M'
        pularLinha = 4

    if plan == '3':
        nomePlanilha = 'Missão em outra Unidade'
        intervaloColunas = 'D:M'
        pularLinha = 4

    if plan == '4':
        nomePlanilha = 'Afastamentos e Restrições'
        intervaloColunas = 'D:K'
        pularLinha = 4

    if plan == '5':
        nomePlanilha = 'Plantões e Sobreavisos'
        intervaloColunas = 'D:J'
        pularLinha = 4

    if plan == '6':
        nomePlanilha = 'Veículos'
        intervaloColunas = 'D:R'
        pularLinha = 5

    if plan == '7':
        nomePlanilha = 'Efetivo por data'
        intervaloColunas = 'D:J'
        pularLinha = 4

    df = pd.read_excel(endereco, sheet_name=nomePlanilha, skiprows=pularLinha, usecols=intervaloColunas)
    first_row_with_all_NaN = df[df.isnull().all(axis=1) == True].index.tolist()[0]
    df = df.loc[0:first_row_with_all_NaN-1]
    df = df.fillna('-')

    return(df)
