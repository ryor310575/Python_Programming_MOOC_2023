# tee ratkaisu tänne
# Write your solution here
# we will need the function sqrt from the math module 
import math

#*******************************************************
#*********  Convertir un archivo a diccionario  ********
#*******************************************************

def get_station_data(fle_name:str)->dict:
    file_info = {} #Abre un diccionario vacio
    with open(fle_name) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "Longitude": # Obvia la cabecera
                continue
            arg_list=[]
            for arg in parts: # Evaluamos si los argimentos son numeros y los evaluamos como numeros si son cadenas los evaluamos como cadenas
                try:
                    arg_list.append(float(arg)) # 
                except:
                    arg_list.append(arg.strip())
            arg_tuple=(arg_list[0],arg_list[1])
            file_info[parts[3]] = arg_tuple # Crear el diccionario de estudiantes la primera columba como Key y el resto como lista
    return file_info
#*******************************************************
#********  Calcular distancia entre estaciones  ********
#*******************************************************
def distance(stations: dict, station1: str, station2: str)-> int:
    coord1=stations[station1]
    coord2=stations[station2]
    # longitude1=float(coord1[0])
    # longitude2=float(coord2[0])
    # latitude1=float(coord1[1])
    # latitude2=float(coord2[1])
    x_km = (float(coord1[0]) - float(coord2[0])) * 55.26
    y_km = (float(coord1[1]) - float(coord2[1])) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
#*******************************************************
#*********   Calcular la distancia mas larga    ********
#*******************************************************
def greatest_distance(stations: dict):
    station_distances={}
    distance_pair=0
    station_key_list=list(stations.keys())
    for station1 in stations.keys():
        for station2 in station_key_list:
            if station1 == station2:
                continue
            else:
                distance_pair=distance(stations,station1,station2)
                station_distances[distance_pair]=[station1,station2]
        station_key_list.pop(0)
    max_distance=max(list(station_distances.keys()))
    return (station_distances[max_distance][0],station_distances[max_distance][1],max_distance)





# You can test your function by calling it within the following block
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    stations = get_station_data('stations3.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)