import plotly.graph_objects as go
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import streamlit as st


def regression():
	st.sidebar.header('')
	fig = go.Figure()
	chart_visual = st.sidebar.selectbox('Вибір функціоналу',
										('2-го порядку', '3-го порядку', 'Передбачення'))
	df = pd.read_csv("FuelConsumption.csv")
	cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
	if True:
		fig.add_trace(go.Scatter(x=cdf.ENGINESIZE, y=cdf.CO2EMISSIONS, mode='markers', ))
		fig.update_layout(title=f'Вихідні дані',
						  xaxis_title='Розмір двигуна',
						  yaxis_title='Викиди')
		st.plotly_chart(fig, use_container_width=True)

		msk = np.random.rand(len(df)) < 0.8
		train = cdf[msk]
		test = cdf[~msk]

		train_x = np.asanyarray(train[['ENGINESIZE']])
		train_y = np.asanyarray(train[['CO2EMISSIONS']])

		test_x = np.asanyarray(test[['ENGINESIZE']])
		test_y = np.asanyarray(test[['CO2EMISSIONS']])

		fig = go.Figure()
		if chart_visual == '2-го порядку':
			poly = PolynomialFeatures(degree=2)
			train_x_poly = poly.fit_transform(train_x)
			clf = linear_model.LinearRegression()
			train_y_ = clf.fit(train_x_poly, train_y)
			# The coefficients
			st.markdown(f'Коефіцієнти: {clf.coef_}')
			st.markdown(f'Перетин: {clf.intercept_}')

			fig.add_trace(go.Scatter(x=cdf.ENGINESIZE, y=cdf.CO2EMISSIONS, mode='markers', name="Initial Data"))
			XX = np.arange(0.0, 10.0, 0.1)
			yy = clf.intercept_[0] + clf.coef_[0][1] * XX + clf.coef_[0][2] * np.power(XX, 2)
			fig.add_trace(go.Scatter(x=XX, y=yy,
									 mode='lines',
									 name='Polynomial Regression'))

		elif chart_visual == '3-го порядку':
			poly3 = PolynomialFeatures(degree=3)
			train_x_poly3 = poly3.fit_transform(train_x)
			clf3 = linear_model.LinearRegression()
			train_y3_ = clf3.fit(train_x_poly3, train_y)
			# The coefficients
			st.markdown(f'Коефіцієнти: {clf3.coef_}')
			st.markdown(f'Перетин: {clf3.intercept_}')
			fig.add_trace(go.Scatter(x=cdf.ENGINESIZE, y=cdf.CO2EMISSIONS, mode='markers', name="Initial Data"))
			XX = np.arange(0.0, 10.0, 0.1)
			yy = clf3.intercept_[0] + clf3.coef_[0][1] * XX + clf3.coef_[0][2] * np.power(XX, 2) + clf3.coef_[0][
				3] * np.power(
				XX, 3)
			fig.add_trace(go.Scatter(x=XX, y=yy,
									 mode='lines',
									 name='Polynomial Regression'))

		elif chart_visual == 'Передбачення':
			poly3_ = PolynomialFeatures(degree=3)
			train_x_poly3 = poly3_.fit_transform(train_x)
			clf3_ = linear_model.LinearRegression()
			train_y3_ = clf3_.fit(train_x_poly3, train_y)
			st.header("Передбачення")
			number = st.number_input("Введіть об'єм двигуна", value=2)
			test_x_poly3 = poly3_.fit_transform([[number]])
			test_y3_ = clf3_.predict(test_x_poly3)
			st.text(f"Розмір викидів ~ {test_y3_}")

		if chart_visual != 'Передбачення':
			fig.update_layout(title=f'Поліномільна регресія {chart_visual}',
							  xaxis_title='Розмір двигуна',
							  yaxis_title='Викиди')

			st.plotly_chart(fig, use_container_width=True)