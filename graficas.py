import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('WHO-COVID-19-global-data.xlsx')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

paises = ['Burundi', 'Spain', 'Chile', 'Paraguay', 'China', 
          'Uganda', 'Congo', 'Colombia', 'Costa Rica', 'Cuba']

df = df[df['Country'].isin(paises)]

fig, ax = plt.subplots()
for pais in paises:
    df_pais = df[df['Country'] == pais]
    ax.plot(df_pais['Date_reported'], df_pais['New_cases'], label='Nuevos casos ' + pais)
    ax.plot(df_pais['Date_reported'], df_pais['New_deaths'], label='Nuevas defunciones ' + pais, linestyle='--')
ax.legend()
plt.title('Nuevos casos y defunciones de COVID-19 a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Casos y defunciones')
plt.show()

fig, ax = plt.subplots()
for pais in paises:
    df_pais = df[df['Country'] == pais]
    ax.plot(df_pais['Date_reported'], df_pais['Cumulative_cases'], label='Casos acumulados ' + pais)
    ax.plot(df_pais['Date_reported'], df_pais['Cumulative_deaths'], label='Defunciones acumuladas ' + pais, linestyle='--')
ax.legend()
plt.title('Casos y defunciones acumuladas de COVID-19 a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Casos y defunciones acumuladas')
plt.show()

fig, ax = plt.subplots()
df_total = df.groupby('Country').agg({'Cumulative_cases': 'max', 'Cumulative_deaths': 'max'}).reset_index()
df_total.plot(x='Country', y=['Cumulative_cases', 'Cumulative_deaths'], kind='bar', ax=ax)
plt.title('Total de infecciones y muertes por países')
plt.xlabel('País')
plt.ylabel('Total')
plt.show()

fig, ax = plt.subplots()
df_total.plot(x='Country', y=['Cumulative_cases', 'Cumulative_deaths'], kind='barh', ax=ax)
plt.title('Total de infecciones y muertes por países (horizontal)')
plt.xlabel('Total')
plt.ylabel('País')
plt.show()