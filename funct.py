from dash import html
import pandas as pd
import plotly.express as px

def get_df(state, city):
    dataframe = pd.read_csv(f"data/ahs-cab2014-{state.lower()}-{city.lower()}.csv")
    ##adding new code
    s=["state_code","district_code","rural_urban","test_salt_iodine","record_code_iodine","Sex","usual_residance","Age_Code","Age","date_of_birth","month_of_birth","year_of_birth","Weight_in_kg","Length_height_cm","Haemoglobin_test","Haemoglobin_level","BP_systolic","BP_systolic_2_reading","BP_Diastolic","BP_Diastolic_2reading","Pulse_rate","Pulse_rate_2_reading","Diabetes_test","fasting_blood_glucose_mg_dl","Marital_status"]

    dataframe = dataframe[s].sort_values("year_of_birth")
    ##Till here
    return dataframe

def generate_table(state,city,max_rows=10):

    dataframe = get_df(state, city)
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

def plot_data(df):
    
    fig = px.scatter(
        df, x="Length_height_cm", y="Weight_in_kg", color="Sex",
        color_continuous_scale=df,
        render_mode="webgl", title="Tips")

    return fig

from line_chart import avg_male_female_height, avg_male_female_weight

def plot_line_height(df):
    dx=avg_male_female_height(df)

    fig=px.line(dx, x="Year", y=["Male", "Female"],render_mode="webgl")

    return fig

def plot_line_weight(df):
    dx=avg_male_female_weight(df)

    fig=px.line(dx, x="Year", y=["Male", "Female"],render_mode="webgl")

    return fig
# print(get_df("assam","sonitpur"))
