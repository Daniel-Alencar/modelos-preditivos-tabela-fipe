import pandas as pd
import statistics

import locale
locale.setlocale(locale.LC_ALL, '')

data = pd.read_csv("data copy.csv")
modelo = 'Q3 2.0 TFSI Quat. 211/220cv S-tronic 5p'
ano_modelo = 2017
mes_inicial = 1
mes_final = 15
lista_de_previsoes = []

# Functions
def selection(data, modelo, ano_modelo):
  selecao = data['Modelo'] == modelo
  data = data[selecao]
  selecao = data['Ano-modelo'] == ano_modelo
  data = data[selecao]

  return data

def convert_data_in_list(data_line):
  values_to_predict = []
  nulls_indexes = []
  mes_inicial = 1
  mes_final = 36

  for i in range(mes_inicial, mes_final + 1):
    try:
      value = locale.atof(data_line[f'Mes {i}'])
    except:
      value = None
      nulls_indexes.append(i)
    values_to_predict.append(value)
  
  print(f"Quantidade de meses: {len(values_to_predict)}")
  return values_to_predict, nulls_indexes

def prediction(values_to_predict, mes_inicial, mes_final):

  values_to_predict = values_to_predict[mes_inicial - 1: mes_final]

  # Fazer a predição do mês "mes_final + 1"
  mean_value = statistics.mean(values_to_predict)
  print(f"Média do mês {mes_inicial} até mês {mes_final}: {mean_value}")
  return mean_value






# Resultados
data = selection(data, modelo, ano_modelo)
print(data)

model = data.iloc[0]
values_to_predict, nulls_indexes = convert_data_in_list(model)

print("")
print(nulls_indexes)
print("")

columns = []
for i in range(mes_final + 1 - mes_inicial):
  columns.append(f"X{i + 1}")
columns.append("Range")
columns.append("Y")

line_count = 0

while(True):
  occurances = 0
  for i in range(mes_inicial, mes_final + 1):
    occurances += nulls_indexes.count(i)
  
  print(f"Quantidade de valores nulos para Mês {mes_inicial} - Mês {mes_final}: {occurances}")

  if(mes_final == 36):
    break

  if(occurances == 0):
    prediction_value = prediction(values_to_predict, mes_inicial, mes_final)

    line_value = values_to_predict[mes_inicial - 1: mes_final].copy()
    line_value.append(f"Mês {mes_inicial} - Mês {mes_final}")
    line_value.append(prediction_value)
    lista_de_previsoes.append(line_value)
    line_count += 1

    values_to_predict[mes_final + 0] = prediction_value

  mes_inicial += 1
  mes_final += 1

medias_base = pd.DataFrame(lista_de_previsoes, columns=columns)
medias_base["Modelo"] = [modelo for i in range(line_count)]
medias_base["Ano-modelo"] = [ano_modelo for i in range(line_count)]
print(medias_base)

# medias_base.to_csv(f"Modelo {modelo}.csv")