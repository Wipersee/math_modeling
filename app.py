import streamlit as st
from multiapp import MultiApp
from pre_work import pre_work
from regression import regression

st.set_page_config(page_title='Polynomial regression', page_icon='🖖')
st.subheader("Прогнозування викиду вуглецю залежно від об‘єму двигуна автомобіля в Канаді на основі поліноміальної регресії.")
st.markdown("Зробив студент групи КМ-81 Піткевич Ілля")

app = MultiApp()
app.add_app("Опис даних", pre_work)
app.add_app("Регресія", regression)

if __name__ == "__main__":
	app.run()
