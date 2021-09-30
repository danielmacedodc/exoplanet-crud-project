#!/usr/bin/env python
# coding: utf-8

# # Projeto de Catálogo de Exoplanetas 

# #### O projeto a seguir se destina a criar um sistema de CRUD de exoplanetas utilizando 6 características identificadoras, tais como:
# ----
# 1. Nome do Exoplaneta
# 2. Distância da Terra (anos-luz)
# 3. Massa do Planeta
# 4. Magnitude Estelar
# 5. Tipo do Planeta
# 6. Data de Descobrimento
# ----

# #### Import de Bibliotecas e Módulos

# In[204]:


import os.path
import ast
import matplotlib.pyplot as plt


# #### Função Checklist
# 
# Essa função destina-se a identificar se um determinado termo já se encontra no arquivo

# In[11]:


def checkList(nameFile, name):
    proceed = True
    dicList = getPlanets(nameFile)
    #recolhe a chave contendo o nome do planeta
    item = [key for key in dicList if key.strip() == name]
    for k in item:
        #indica se o item já existe
        proceed = False
    
    #caso não exista, prossiga o processo
    return proceed
    


# #### Função Registro
# 
# Essa função se destina a atribuir a um dicionário o nome do planeta(chave) e os atributos(valor).

# In[59]:


def register(dic, atributes):
    name = input('a) Insert the name of the Planet: ')
    atributes['distance (Light-Year)'] = input('b) Set the distance from Earth in light-years: ')
    atributes['mass'] = input('c) Enter the mass of the planet: ')
    atributes['stellar magnitude'] = input('d) Enter the stellar magnitude: ')
    atributes['typo'] = input('e) Set the classification of the planet: ')
    atributes['date'] = input('f) Discovery date (year): ')
    dic[name] = atributes 


# #### Função de Coleta de Dados
# 
# Esta função se propõe a ler os dados de um arquivo .txt e atribuí-los a um dicionário e depois retorná-lo.

# In[13]:


def getPlanets(nameFile):
    divisor = []
    dic = {}
    fil = open(nameFile, 'r')
    lines = fil.readlines()
    for line in lines:
        #remove caracteres '\n' do arquivo
        line.strip()
        #Divide os dados da string numa lista
        divisor = line.split(':',maxsplit=1)
        #Atribui os valores da lista a um dicionário
        key = divisor[0].strip()
        dic[key] = divisor[1].strip()
    fil.close()
    
    return dic


# #### Função Listar Todos os Elementos
# 
# Esta função permite que todos os itens do arquivo sejam listados

# In[78]:


def listAllElements(nameFile):
    #averigua se já existe o arquivo
    if os.path.isfile(nameFile):
        dicList = getPlanets(nameFile)
        for k, v in dicList.items():
            #lê-se a chave do conjunto do dicionário
            print(f'Name: {k}')
            #converte a string do dicionário em dicionário
            v = ast.literal_eval(v)
            for key, value in v.items():
                #impressão dos pares chave-valor
                print(f'{key.capitalize()}: {value}', end=' | ')
            print('\n')
            for i in range(110):
                print('*', end='')
            print('\n')
    else:
        print("There's no directory!\n")
    


# #### Função Listar por Nome
# 
# Neste caso teremos uma função que lista um objeto pelo seu nome. Como cada planeta possui como característica única o seu nome, utilizou-se essa chave para busca. No entanto, caso outro atributo fosse utilizado, bastaria iterar cada dicionário nos pares e apresentar o valor.

# In[15]:


def findByName(nameFile):
    if os.path.isfile(nameFile):
        founded = False
        dicList = getPlanets(nameFile)
        name = input('Enter the name of the planet: ')
        planet = [key for key in dicList if key.strip() == name]
        for k in planet:
            print(f'Name: {k}')
            #módulo converte a string em dicionário
            v = ast.literal_eval(dicList[k])
            for key, value in v.items():
                #impressão do par chave-valor
                print(f'{key.capitalize()}: {value}', end=' | ')
            print('\n')
            founded = True
        if not founded:
            print('Planet not founded!')
    else:
        print("There's no directory!\n")


# #### Função Adicionar Planeta
# 
# Esta função adiciona novos itens na nos dicionários e salva no arquivo.

# In[38]:


def addNewPlanet(nameFile):
    dic = {}
    atributes = {}
    register(dic, atributes)
    #verifica se existe arquivo. Caso sim, adiciona. Do contrário cria um e adiciona.
    if os.path.isfile(nameFile):
        fil = open(nameFile, 'a')
        for key, values in dic.items():
            if checkList(nameFile, key):
                #escreve no arquivo o par chave-valor inserido
                fil.write(f'{key.lower()}:{values}\n')
                print('Planet registered.')
            else:
                print('Planet already exists!\n')
        fil.close()
    else:
        #caso em que não há arquivo .txt no diretório
        fil = open(nameFile, 'w')
        for key, values in dic.items():
            if checkList(nameFile, key):
                fil.write(f'{key.lower()}:{values}\n')
                print('Planet registered.')
            else:
                print('Planet already exists!\n')
        fil.close()


# #### Função Update
# 
# Funciona de forma similar à criação de elemento. Faz checagem se há ou não um item para update.

# In[17]:


def updatePlanet(nameFile):
    founded = False
    dicList = getPlanets(nameFile)
    name = input('Enter the name of the planet: ')
    #adiciona a chave do item solicitado
    remove = [key for key in dicList if key.strip() == name]
    for k in remove:
        print('Planet founded!\n')
        founded = True
        del dicList[k]
    if not founded:
        print('Planet not founded!')
    else:
        fil = open(nameFile, 'w')
        for key, values in dicList.items():
            fil.write(f'{key.lower()}:{values}\n')
        fil.close()
        addNewPlanet(nameFile)    


# #### Função Delete
# 
# Esta função delete o item solicitado, caso exista, por meio da chave 'distance'. A função varre o dicionário dos valores para depois excluir o par.

# In[320]:


def deletePlanet(nameFile):
    if os.path.isfile(nameFile):
        founded = False
        dicList = getPlanets(nameFile)
        distance = input('Enter the distance (ly) from Earth of the planet to be deleted: ')
        #remove = [key for key in dicList if key.strip() == name]
        for keys, values in dicList.items():
            #converte os valores de string para dicionário
            v = ast.literal_eval(dicList[keys])
            for val in v.values():
                if val.strip() == distance:
                    print('Planet deleted!\n')
                    founded = True
                    #salva a chave do item a ser deletado
                    key = keys
        if not founded:
            print('Planet not founded!')
        else:
            #identifica o item e o exclui
            del dicList[key]
            #reescreve no arquivo os itens restantes
            fil = open(nameFile, 'w')
            for key, values in dicList.items():
                fil.write(f'{key.lower()}:{values}\n')
            fil.close()
    else:
        print("There's no directory!\n")


# #### Funções para Gerar Gráficos
# 
# As seguintes funções geram gráficos de pizza, ponto e de barras para indicar características importantes sobre os exoplanetas descobertos.

# In[326]:


def typeChart(nameFile):
    numbers = []
    typos = ['Gas Giant', 'Neptune-like', 'Super Earth', 'Terrestrial','Unidentified']
    color = ['pink','indigo','cyan','g','gray']
    for i in range(5):
        numbers.append(0)
    if os.path.isfile(nameFile):
        dicList = getPlanets(nameFile)
        for keys, values in dicList.items():
            v = ast.literal_eval(dicList[keys])
            for k, val in v.items():
                # Identifica as chaves do tipo mostrado e conta os valores correspondentes
                if k == 'typo':
                    if val.strip() == 'Gas Giant':
                        numbers[0] += 1
                    elif val.strip() == 'Neptune-like':
                        numbers[1] += 1
                    elif val.strip() == 'Super Earth':
                        numbers[2] += 1
                    elif val.strip() == 'Terrestrial':
                        numbers[3] += 1
                    else:
                        numbers[4] += 1
        
        # exibe gráfico pizza
        plt.figure(figsize=(12, 6), dpi=90)
        plt.pie(numbers,labels=typos,colors=color,startangle=90,shadow=True,explode=(0,0,0,0.1,0))
        plt.savefig('piePlanets.png', transparent = True)
        plt.show()
    
    else:
        print("There's no directory!\n")
    
            


# In[327]:


def distanceChart(nameFile):
    dTerrestrial = []
    dGasG = []
    dNepLike = []
    dSuperE = []
    unknown = []
    toBeAdd = 0.0
    number = ''
    if os.path.isfile(nameFile):
        dicList = getPlanets(nameFile)
        for keys, values in dicList.items():
            v = ast.literal_eval(dicList[keys])
            for k, val in v.items():
                # averigua a distância em anos-luz e converte apenas os dígitos da string
                if k == 'distance (Light-Year)':
                    for word in val.split():
                        if word.isdigit() or word == '.':
                            number = number + word
                    toBeAdd = float(number)
                    number = ''
                    
                # após converter, logo em seguida verifica o tipo de planeta e associa o valor
                if k == 'typo':
                    if val.strip() == 'Gas Giant':
                        dGasG.append(toBeAdd)
                    elif val.strip() == 'Neptune-like':
                        dNepLike.append(toBeAdd)
                    elif val.strip() == 'Super Earth':
                        dSuperE.append(toBeAdd)
                    elif val.strip() == 'Terrestrial':
                        dTerrestrial.append(toBeAdd)
                    else:
                        unknown.append(toBeAdd)
        
        # plota gráfico de pontos com os planetas e suas distâncias
        plt.figure(figsize=(12, 6), dpi=90)
        plt.plot(dGasG,dGasG, 'rs', label="Gas Giant")
        plt.plot(dNepLike,dNepLike, 'bo', label="Neptune-like")
        plt.plot(dSuperE,dSuperE, 'm*', label="Super Earth")
        plt.plot(dTerrestrial,dTerrestrial, 'g^', label="Terrestrial")
        plt.legend(loc="upper left")
        plt.ylabel('Distances (Light-years)')
        plt.title('Planetarian Distances')
        ax = plt.gca()
        ax.minorticks_on()
        plt.grid(color = 'green', linestyle = '-', linewidth = 1)
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.savefig('distance.png', transparent = True)
        plt.show()
    else:
        print("There's no directory!\n")


# In[328]:


def stellarMag(nameFile):
    vis = 0
    notVis = 0
    unknown = 0
    if os.path.isfile(nameFile):
        dicList = getPlanets(nameFile)
        for keys, values in dicList.items():
            v = ast.literal_eval(dicList[keys])
            for k, val in v.items():
                # em processo similar aos anteriores, averigua as magnitudes e armazena
                if k == 'stellar magnitude':
                    if float(val.strip()) <= 6:
                        vis += 1
                    elif float(val.strip()) > 6:
                        notVis += 1
                    else:
                        unknown += 1
                        
        # plota gráfico barras
        yAxis = [notVis,vis,unknown]
        plt.bar([1,2,3], yAxis, color='black')
        plt.xticks([1,2,3], ['Visible','Not Visible','Unknown'])
        plt.ylabel('Stellar Magnitude')
        plt.title('Stellar System Visibility')
        plt.savefig('stellar-magnitude.png', transparent = True)
        plt.show()
    
    else:
        print("There's no directory!\n")


# In[329]:


# função similar à anterior
def discoveryDate(nameFile):
    recent = 0
    firstDecade = 0
    secondDecade = 0
    before = 0
    unknown = 0
    if os.path.isfile(nameFile):
        dicList = getPlanets(nameFile)
        for keys, values in dicList.items():
            v = ast.literal_eval(dicList[keys])
            for k, val in v.items():
                if k == 'date':
                    if 2021 <= int(val.strip()):
                        recent += 1
                    elif 2011 <= int(val.strip()) < 2021:
                        secondDecade += 1
                    elif 2001 <= int(val.strip()) < 2011:
                        firstDecade += 1
                    elif 1991 <= int(val.strip()) < 2001:
                        before += 1
                    else:
                        unknown += 1
        plt.figure(figsize=(12, 6), dpi=90)
        yAxis = [recent, secondDecade, firstDecade, before, unknown]
        plt.bar([1,2,3,4,5], yAxis)
        plt.xticks([1,2,3,4,5], ['Today - 2021','2020 - 2011','2010 - 2001', '2000 - Before', 'Unknown'])
        plt.ylabel('Planets Discovered')
        plt.xlabel('Year Interval')
        plt.title('Discovery Date')
        plt.savefig('discovery-date.png', transparent = True)
        plt.show()
    
    else:
        print("There's no directory!\n")


# ### Função Menu 

# In[324]:


fileName = input('Insert the file name (.txt): ')
fileName = fileName + '.txt'
print(fileName)
option = 1
options = ['1','2','3','4','5','6','7']

while option != '7':
    print('----------------------------------')
    print('               MENU')
    print('----------------------------------\n')
    print('1 -- List All Planets')
    print('2 -- Search Planet By Name')
    print('3 -- Add New Planet')
    print('4 -- Update Planet')
    print('5 -- Delete Planet')
    print('6 -- Generate Stats Charts')
    print('7 -- Exit')
    print('----------------------------------')
    option = input('Insert your option: ')
    print('----------------------------------')
    
    if option not in options:
        print('Invalid option. Try again.\n')
    elif int(option) == 1:
        listAllElements(fileName)
    elif int(option) == 2:
        findByName(fileName)
    elif int(option) == 3:
        addNewPlanet(fileName)
    elif int(option) == 4:
        updatePlanet(fileName)
    elif int(option) == 5:
        deletePlanet(fileName)
    elif int(option) == 6:
        typeChart(fileName)
        distanceChart(fileName)
        stellarMag(fileName)
        discoveryDate(fileName)
        

