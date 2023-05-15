from geopy.distance import geodesic
import pandas as pd

class Find_NS:
    def __init__(self, target_locate, station_csv, line_csv, company_csv):
        self.STATION_CSV = station_csv
        self.LINE_CSV = line_csv
        self.COMPANY_CSV = company_csv
        self.target_locate = target_locate

    def load_station_data(self):
        df_station = pd.read_csv(self.STATION_CSV)
        df_line = pd.read_csv(self.LINE_CSV)
        df_company = pd.read_csv(self.COMPANY_CSV)

        df_station = pd.merge(df_station,
                            df_line[["line_cd", "company_cd", "line_name"]],
                            how="left",
                            on="line_cd")

        df_station = pd.merge(df_station,
                            df_company[["company_cd", "company_name"]],
                            how="left",
                            on="company_cd")

        df_station = df_station[["station_name", "lon", "lat", "line_name", "company_name"]]
        
        return df_station

    def get_distance(self, ll_1, ll_2):
        return geodesic(ll_1, ll_2).km
    
    def get_nearest_station(self, df_station):
        df_station["distance"] = df_station.apply(lambda x: self.get_distance(self.target_locate, [x["lat"], x["lon"]]), axis=1)
        nearest_station = df_station[df_station["distance"] == df_station["distance"].min()]
        nearest_station = nearest_station.drop(["lon", "lat", "distance", "company_name"], axis=1)
        return nearest_station
    
    def output_nearest_station(self, nearest_station):
        station_name = nearest_station["station_name"].to_string(index=False)
        line_name = nearest_station["line_name"].to_string(index=False)
        nearest_station_line_list = list()
        nearest_station_name = nearest_station["station_name"].head(1).to_string(index=False, header=False)
        for line in nearest_station["line_name"]:
            nearest_station_line_list.append(line)
        return nearest_station_name, nearest_station_line_list


    def main(self):
        df_station = self.load_station_data()
        nearest_station = self.get_nearest_station(df_station)
        nearest_station_name, nearest_station_line_list = self.output_nearest_station(nearest_station)
        return nearest_station_name, nearest_station_line_list