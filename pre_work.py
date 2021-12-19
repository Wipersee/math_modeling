import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def pre_work():
	st.sidebar.header('')
	SHOW_DESCRIBE_DATA = st.sidebar.checkbox("Показати опис даних")
	SHOW_EXPLORATORY_DATA = st.sidebar.checkbox("Показати розвідувальний аналіз")
	fig = go.Figure()
	df = pd.read_csv("FuelConsumption.csv")
	st.dataframe(df.head(50))

	def draw_histograms(dataframe, features, rows, cols):
		fig = plt.figure(figsize=(20, 20))
		for i, feature in enumerate(features):
			ax = fig.add_subplot(rows, cols, i + 1)
			dataframe[feature].hist(bins=20, ax=ax, facecolor='midnightblue')
			ax.set_title(feature + " Distribution", color='DarkRed')
			ax.set_yscale('log')
		st.pyplot(fig)

	if SHOW_DESCRIBE_DATA:
		st.header("DATA QUALITY CHECK")

		st.caption("Відсоток відсутніх значень у кожному стовпці")
		st.code(round(100 * (df.isnull().sum() / len(df)), 2).sort_values(ascending=False))

		st.caption("Відсоток відсутніх значень у кожному рядку")
		st.code(round(100 * (df.isnull().sum(axis=1) / len(df)), 2).sort_values(ascending=False))

		st.caption("Опис стовпців")
		st.markdown("""
		- **MODELYEAR** (рік, в якому випущена автівка), наприклад 2013
		- **MAKE** (марка) наприклад Toyota
		- **MODEL** (модель), наприклад HILUX
		- **VEHICLE CLASS** (тип автівки), наприклад кроссовер 
		- **ENGINE SIZE** (об‘єм двигуна), наприклад 4.2
		- **CYLINDERS** (кількість циліндрів), наприклад 6
		- **TRANSMISSION** (трансміссія), наприклад А6
		- **FUEL CONSUMPTION in CITY**(L/100 km) (споживання топлива в місті на 100 км) 
		- **FUEL CONSUMPTION in HWY** (L/100 km) (споживання топлива на автомагістралі на 100 км) 
		- **FUEL CONSUMPTION COMB** (L/100 km)(споживання топлива комбіноване на 100 км) 
		- **CO2 EMISSIONS** (g/km) (викид вуглецю грам/км)
		""")

	if SHOW_EXPLORATORY_DATA:
		st.header("EXPLORATORY DATA ANALYSIS")

		st.caption("Надає описову статистику, яка узагальнює центральну тенденцію, дисперсію та форму.")
		st.code(df.describe())

		draw_histograms(df, ["FUELCONSUMPTION_COMB", "FUELCONSUMPTION_HWY", "FUELCONSUMPTION_CITY",
							 "CO2EMISSIONS", "CYLINDERS"], 8, 4)

		fig = plt.figure()
		sns.heatmap(df.corr(), annot=True)
		st.pyplot(fig)