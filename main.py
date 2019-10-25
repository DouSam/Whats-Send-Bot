import requests, os, time, re
from selenium import webdriver
import config, sheets

dir_path = os.getcwd()#Pegando o directorio da pasta na qual o programa está sendo rodado
print(dir_path)
chrome = dir_path+'\chromedriver.exe' #Abrindo o driver do google.
option = webdriver.ChromeOptions() #Fazendo com que o nosso driver do google tenha uma config específica
option.add_argument(r"user-data-dir="+dir_path+"profile\wpp")#Especificamos o que queremos salvar na config e onde
#Usando essa 'option' não precisamos ficar logando no wpp
driver = webdriver.Chrome(chrome,chrome_options=option)#Abrimos uma instancia do chrome com nossas configs
time.sleep(5)#Apenas para ter certeza de que deu tempo de abrir corretamente
tem_contato_nao_contactado=True #Uma variavel que vai definir quando parar o while.
'''
Com o chrome aberto agora eu preciso pegar os dados, como o site que iremos ir, o texto, número, nomes e assim vai
Lembrando que na primeira vez na qual vamos abrir o site, é necessário escanear o QR code com o celular
As outras ele já abre automaticamente mas não é possível usar em outro wpp Web, se atente a isso.
Modificação, vou colocar dentro de um while, assim eu vou percorrer a planilha toda e enviar mensagem para todos e
Somente quando acabar o programa irá fechar.
'''
while tem_contato_nao_contactado:
    linha,nome,numero,contrato = sheets.pega_dados() 
    print("\n"+str(linha),nome,str(numero),contrato+"\n")
    if nome != "":
        texto = config.mensagem_com_contrato.format(nome,contrato)
        numero = "+5516" + str(numero)#Não esqueça de mudar o DDD, no meu caso é o 16
        abre_wpp = driver.get(config.url_mensagem.format(numero,texto))#Essa parte abre o site no driver
        #Agora que ele abre o site e já está com a mensagem para ser mandada, temos que fazer ele clicar
        driver.implicitly_wait(30) #Esse comando faz com que ele espere 30 segundos até achar o elemento
        time.sleep(10)
        botao_enviar = driver.find_element_by_class_name('_3M-N-') #Explicação mais abaixo.
        botao_enviar.click()#Agora nossa mensagem foi enviada
        #Agora que enviamos a mensagem precisamos informar na planilha que a pessoa foi contactada e que agora queremos a próxima.
        sheets.mudaContactado(linha)
    else:
        tem_contato_nao_contactado = False
    
driver.quit()

'''
Para você achar qual o elemento, basta apertar o crtl + shift + c e posicionar sobre o botao de enviar
Com um pouco de conhecimneto em html fica mais fácil, depois disso você pega a class do botão e deixa 
Identificado, dessa forma achamos onde está o botão. Agora só precisamos acionar o click para enviar
'''
