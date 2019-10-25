import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import os

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope) #Esse arquivo você pega ele no console de api do seu projeto no google developer.
#client = gspread.authorize(creds) #Fazendo login e pegando um token
#sheet = client.open("clientesTeste").sheet1  #Escolhendo a planilha para abrir
#data = sheet.get_all_records()  #Pegando os dados da planilha


def pega_dados():#Essa função vai pegar os dados da pessoa na planilha para eu contactar
    client = gspread.authorize(creds) #Fazendo login e pegando um token
    sheet = client.open("clientesTeste").sheet1  #Escolhendo a planilha para abrir
    data = sheet.get_all_records()  #Pegando os dados da planilha
    linha = 0
    nome = ''
    numero = ''
    contrato = ''
    while linha < len(data):#Aqui eu passo linha a linha vendo se a pessoa já foi contatada
        if data[linha]['Contactado'] == "":
            nome = data[linha]['Nome']
            numero = data[linha]['Telefone']
            contrato = data[linha]['Contrato']
            return linha,nome,numero,contrato
        else:
            linha = linha + 1
    return linha,nome,numero,contrato

def mudaContactado(linha):
    client = gspread.authorize(creds) #Fazendo login e pegando um token
    sheet = client.open("clientesTeste").sheet1  #Escolhendo a planilha para abrir
    data = sheet.get_all_records()  #Pegando os dados da planilha

    linha = linha + 2 #Pois em programação começa pelo 0 mas na planilha começa no 1 e a primeira linha da planilha é desconsiderada.
    sheet.update_cell(linha,6,"Contatado") #Agora atualizamos a linha e a situação do cliente
    
