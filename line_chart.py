import pandas as pd
import plotly.express as px
import numpy as np


'''
def data_clean(state, city):
    state_name=state
    city_name=city
    dfa=pd.read_csv(f"data/ahs-cab2014-{state_name.lower()}-{city_name.lower()}.csv")
    s=["state_code","district_code","rural_urban","stratum","test_salt_iodine","record_code_iodine","Sex","usual_residance","Age_Code","Age","date_of_birth","month_of_birth","year_of_birth","Weight_in_kg","Length_height_cm","Haemoglobin_test","Haemoglobin_level","BP_systolic","BP_systolic_2_reading","BP_Diastolic","BP_Diastolic_2reading","Pulse_rate","Pulse_rate_2_reading","Diabetes_test","fasting_blood_glucose_mg_dl","Marital_status","gauna_perfor_not_perfor","duration_pregnanacy","first_breast_feeding","is_cur_breast_feeding","day_or_mn_for_breast_feeding_cd","day_or_month_for_breast_feeding","water_month","ani_milk_month","semisolid_month_or_day","solid_month","vegetables_month_or_day","illness_type","illness_duration"]
    df=dfa[s].sort_values("year_of_birth")
    return df
'''

def avg_height(dataset, gender):
    dataset=dataset[dataset["Sex"]==str(gender.capitalize())]
    year_list=list(dataset[dataset["year_of_birth"]<=1995]["year_of_birth"].sort_values().unique())
    avg_h=[np.mean(dataset[dataset["year_of_birth"]==i]["Length_height_cm"]) for i in year_list]
    height_age_df=pd.DataFrame({"Year":year_list, f"Average_height_{gender}":avg_h})
    return height_age_df.dropna()

def avg_weight(dataset,gender):
    dataset=dataset[dataset["Sex"]==str(gender.capitalize())]
    year_list=list(dataset[dataset["year_of_birth"]<=1995]["year_of_birth"].sort_values().unique())
    avg_w=[np.mean(dataset[dataset["year_of_birth"]==i]["Weight_in_kg"]) for i in year_list]
    weight_age_df=pd.DataFrame({"Year":year_list, f"Average_weight_{gender}":avg_w})
    return weight_age_df.dropna()

def avg_male_female_height(dataset):
    datafr=pd.DataFrame({"Year": avg_height(dataset,"male")["Year"], "Male": avg_height(dataset, "male")["Average_height_male"], "Female": avg_height(dataset, "female")["Average_height_female"]})
    return datafr

def avg_male_female_weight(dataset):
    datafr=pd.DataFrame({"Year": avg_weight(dataset, "male")["Year"], "Male": avg_weight(dataset, "male")["Average_weight_male"], "Female": avg_weight(dataset, "female")["Average_weight_female"]})
    return datafr

