# Select Lybreries
import pandas as pd
import numpy as np

def Prepocess():

    #Create A Datafream
    Immo_Data=pd.read_csv("DELIVERABLE.csv", sep=",")

    #Checking rows/Avelable rows & columns (8291, 17)
    Immo_Data.shape

    # Drop duplicates
    Immo_Data.drop_duplicates(inplace=True) 

    # After droping duplicate Datasets rows& columns (5751, 7) 

    #Count all NaN in a DataFrame (both columns & Rows)
    Immo_Data.isnull().sum().sum()

    # Change dtype of columns price, surface, bedrooms.count and Construction Year
    Immo_Data['classified.price'] = pd.to_numeric(Immo_Data['classified.price'],errors = 'coerce')
    Immo_Data['classified.land.surface'] = pd.to_numeric(Immo_Data['classified.land.surface'],errors = 'coerce')
    Immo_Data['classified.bedroom.count'] = pd.to_numeric(Immo_Data['classified.bedroom.count'],errors = 'coerce')
    Immo_Data['NOTRclassified.building.constructionYear'] = pd.to_numeric(Immo_Data['NOTRclassified.building.constructionYear'],errors = 'coerce')
    Immo_Data.dtypes

    # Selecting only required columns
    Immo_Data=Immo_Data[["classified.subtype","classified.price","classified.land.surface","classified.bedroom.count","classified.atticExists","classified.outdoor.terrace.exists","classified.wellnessEquipment.hasSwimmingPool"]]


    # Using Dropna method to delete 'None' value/ avalable Rows & Columns (5499, 7)
    Immo_Data =Immo_Data.dropna()

    #Creat New datasets without "house group"
    New_Immo= Immo_Data[Immo_Data['classified.subtype']]!= 'house group'
    # Change Columns name
    New_df = New_Immo.rename(columns={'classified.subtype':'House_Type', 
                                    'classified.price':'Price',
                                    'classified.land.surface':'Serface', 
                                  'classified.bedroom.count':  'No. of Bed-Room',
                                   'classified.atticExists' :  'AtticExists',
                                  'classified.outdoor.terrace.exists': 'TerraceExists',
                                  'classified.wellnessEquipment.hasSwimmingPool' :  'SwimmingPoolExists'})

    # Create New CSV File 
    New_Immo.to_csv("New-ImmoElliza.csv")