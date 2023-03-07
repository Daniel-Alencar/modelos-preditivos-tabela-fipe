import pandas as pd
import statistics

data = pd.read_csv("data_without_null.csv")

selecao = data['Modelo']=='LOGAN Authentique Hi-Flex 1.0 16V 4p'
data_model = data[selecao]

meses_to_predict = 7
initial_mes = 24
final_mes = 35

for value in data_model.iloc:
  values_to_predict = []

  for i in range(initial_mes, final_mes + 1):

    values_to_predict.append(floavalue[f'Mes {i}'])
    print(value[f'Mes {i}'])
  
  # Fazer a predição do mês "final_mes + 1"
  mean_value = statistics.mean(values_to_predict)
  print(mean_value)
  
  initial_mes -= 1
  final_mes -= 1
