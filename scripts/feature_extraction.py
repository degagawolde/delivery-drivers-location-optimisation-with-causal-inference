from haversine import Unit
import haversine as hs
import pandas as pd

class FeatureExtraction:
    def __init__(self) -> None:
        pass
    def distance_from(self,loc1,loc2): 
        dist = hs.haversine(loc1,loc2)
        return round(dist,2)
    
    def distance_from(self,loc1,loc2): 
        dist = hs.haversine(loc1,loc2,unit=Unit.METERS)
        return round(dist,2)

    def cordinate_tupple(self,df,columns):
        for col in columns:
            df[col] = df[col].apply(
                lambda x:(float(x.split(',')[0]),float(x.split(',')[1])))
        return df  

    def convert_to_date(self,df, columns):
        for col in columns:
            df[col] =  df[col].apply(lambda x: pd.to_datetime(x))
        return df