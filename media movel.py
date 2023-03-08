import pandas as pd
import statistics

import locale
locale.setlocale(locale.LC_ALL, '')

data = pd.read_csv("data.csv")
modelo = 'LOGAN Authentique Hi-Flex 1.0 16V 4p'
ano_modelo = 2015
meses_to_predict = 7
initial_mes = 24
final_mes = 35

# Functions
def selection(data, modelo, ano_modelo):
  selecao = data['Modelo'] == modelo
  data = data[selecao]
  selecao = data['Ano-modelo'] == ano_modelo
  data = data[selecao]

  return data

def convert_data_in_list(data_line, mes_inicial, mes_final):
  values_to_predict = []

  print(f"Verificando valores de {mes_inicial} à {mes_final}")
  for i in range(mes_inicial, mes_final + 1):
    values_to_predict.append(locale.atof(data_line[f'Mes {i}']))
  
  return values_to_predict

def prediction(values_to_predict):
  # Fazer a predição do mês "mes_final + 1"
  mean_value = statistics.mean(values_to_predict)  
  return mean_value





# Resultados
data = selection(data, modelo, ano_modelo)
print(data)

model = data.iloc[0]

values_to_predict = convert_data_in_list(model, initial_mes, final_mes)

for i in range(meses_to_predict):
  prediction_value = prediction(values_to_predict)

  initial_mes -= 1
  final_mes -= 1


# # Fazer a base da predição com a média móvel
# columns = []
# for i in range(final_mes + 1 - initial_mes):
#   columns.append(f"X{i + 1}")
# columns.append("Y")
# print(columns)


# model = data_model.iloc[0]


# predictions_list = []
# mes_predito_list = []
# for i in range(meses_to_predict):
#   values_to_predict = []

#   print(f"Verificando valores de {initial_mes} à {final_mes}")
#   for i in range(initial_mes, final_mes + 1):
#     values_to_predict.append(locale.atof(model[f'Mes {i}']))
  
#   # Fazer a predição do mês "final_mes + 1"
#   mean_value = statistics.mean(values_to_predict)
#   print(f"Média para o mês {final_mes + 1}: {mean_value}")
#   values_to_predict.append(mean_value)
#   mes_predito_list.append(f"Mês {final_mes + 1}")

#   predictions_list.append(values_to_predict)
  
#   initial_mes -= 1
#   final_mes -= 1

# medias_movels = pd.DataFrame(predictions_list, columns=columns)

# medias_movels["Mês predicto"] = mes_predito_list
# print(medias_movels)

# medias_movels.to_csv(f"Modelo {modelo}.csv")