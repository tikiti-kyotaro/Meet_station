import geocoder
import geopy
import reverse_geocoder as rg

class Equal_locate:
    def __init__(self, location_list):
        self.location_list = location_list
        self.not_address = False
        self.lat_sum = 0
        self.lng_sum = 0
    
    def get_location_info(self):
        logging_list = list()
        for i, locate in enumerate(self.location_list):
            ret = geocoder.osm(locate, timeout=5.0)
            if ret.latlng is None:
                self.not_address = True
                sentence = f'場所{i+1}の場所に対応する住所がありません。'
                print(f'場所{i+1}の場所に対応する住所がありません。')
                logging_list.append(sentence)
            else:
                sentence = f'場所{i+1}   住所:{ret.address}, 緯度:{round(ret.latlng[0], 4)}, 経度:{round(ret.latlng[1], 4)}'
                print(f'場所{i+1}   住所:{ret.address}, 緯度:{ret.latlng[0]}, 経度:{ret.latlng[1]}')
                logging_list.append(sentence)

                self.lat_sum += ret.latlng[0]
                self.lng_sum += ret.latlng[1]
        return logging_list
    
    def search_location(self):
        return self.lat_sum / len(self.location_list), self.lng_sum / len(self.location_list)

    def main(self):
        logging_list = self.get_location_info()
        if self.not_address:
            return None, None, logging_list, None
        else:
            lat, lng = self.search_location()
            coordinates = (lat, lng)
            results = rg.search(coordinates)
            print(f'すべての地点から等しい距離にあるのは、住所:{results[0]["admin1"]}, {results[0]["name"]}, 緯度:{lat}, 経度:{lng}')
            target_ll_info = f'住所:{results[0]["admin1"]}, {results[0]["name"]}, 緯度:{round(lat, 4)}, 経度:{round(lng, 4)}'
            return lat, lng, logging_list, target_ll_info