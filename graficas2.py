import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('WHO-COVID-19-global-data.xlsx')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

paises = ['Burundi', 'Spain', 'Chile', 'Paraguay', 'China', 
          'Uganda', 'Congo', 'Colombia', 'Costa Rica', 'Cuba']

df = df[df['Country'].isin(paises)]

df['Year'] = df['Date_reported'].dt.year

fig, ax = plt.subplots()
df_year = df.groupby(['Country', 'Year']).agg({'Cumulative_cases': 'max'}).reset_index()
df_year_pivot = df_year.pivot(index='Country', columns='Year', values='Cumulative_cases')
df_year_pivot.plot(kind='bar', stacked=True, ax=ax)
plt.title('Acumulado de infectados por año del total de infectados')
plt.xlabel('País')
plt.ylabel('Total de infectados')
plt.show()

fig, ax = plt.subplots()
df_year_pivot.plot(kind='bar', ax=ax)
plt.title('Comparativo por año de las infecciones de los países')
plt.xlabel('País')
plt.ylabel('Infecciones')
plt.show()

fig, ax = plt.subplots()
df_year_deaths = df.groupby(['Country', 'Year']).agg({'Cumulative_deaths': 'max'}).reset_index()
df_year_deaths_pivot = df_year_deaths.pivot(index='Country', columns='Year', values='Cumulative_deaths')
df_year_deaths_pivot.plot(kind='bar', ax=ax)
plt.title('Muertes por año por país')
plt.xlabel('País')
plt.ylabel('Muertes')
plt.show()