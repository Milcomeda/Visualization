import plotly_express as px

df = px.data.gapminder()

graph = px.choropleth(df, locations='iso_alpha', color='gdpPercap', animation_frame='year')
graph.show()