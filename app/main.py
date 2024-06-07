import utils
import read_csv
import chars

def run():
  data = read_csv.read_csv('data.csv')
  ## Esto es para tomas los datos de una columna
  #Continent = input('Type Country => ')
  data = list(filter(lambda item : item['Continent'] == 'South America' ,data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  chars.generate_pie_chart(countries, percentages)
  
  #### Esto es para tomas los datos de una fila
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    chars.generate_bar_chart(labels, values)
  

if __name__ == '__main__':
  run()