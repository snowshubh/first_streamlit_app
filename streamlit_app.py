import streamlit
streamlit.header('Breakfast Favorites')

streamlit.text('🥣 omega 3 & Bulebeery oatmeal')

streamlit.text('🥗 kale, Spinac & Rocket Smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')
   
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
