import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt


st.title("Lab3")

st.header("Display data")

st.subheader("Matplotlib chart")


data1 = pd.read_csv("https://raw.githubusercontent.com/CSE5544/data/main/ClimateData.csv")
data = pd.DataFrame(data1)
data.replace({'..': '0'}, inplace=True)
data

#prepare the data
countries = data['Country\\year']
df_data_country = data.iloc[:,2:]
df_data_country = df_data_country.apply(pd.to_numeric, errors='coerce')
country_stats = pd.DataFrame({'country': countries, 'mean': df_data_country.mean(axis=1),
                       'std': df_data_country.std(axis=1)})


st.header("Show Heatmaps")
st.text('These heatmaps show that emission of countries by years.')


chart_data = data.drop(columns=['Non-OECD Economies'])
chart_data = pd.melt(chart_data, id_vars=['Country\year'], var_name='year')
chart_data['value'] = chart_data['value'].apply(pd.to_numeric, errors='coerce')
chart_data.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)

#render using altair
st.subheader("Heatmap1")
st.text("For the first heatmap I choose to a color scheme 'orangered'.\n'orangered' belongs to sequential multi-hue schemes.")

heatmap = alt.Chart(chart_data).mark_rect().encode(
    x=alt.X('country:N', title = 'country'),
    y=alt.Y('year:O', title = 'year'),
    #color='emission:Q',
    color = alt.Color('emission:Q', scale=alt.Scale(scheme='orangered')),
    tooltip=['country', 'year', 'emission']
)

st.altair_chart(heatmap, use_container_width = True)


st.subheader("Heatmap2")
st.text("For the second heatmap I try to use 'orangered' scheme to color the heatmap2.\n'orangered' belongs to categorical schemes.")

heatmap2 = alt.Chart(chart_data).mark_rect().encode(
    x=alt.X('country:N', title = 'country'),
    y=alt.Y('year:O', title = 'year'),
    #color='emission:Q',
    color = alt.Color('emission:Q', scale=alt.Scale(scheme='category20')),
    tooltip=['country', 'year', 'emission']
)

st.altair_chart(heatmap2, use_container_width = True)
