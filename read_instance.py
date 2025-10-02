
import numpy as np
import os
import pandas as pd

import osmnx as ox


### REQUIRE
truck_speed = 11.2      # m/s
drone_speed = 31.3      # m/s

def process_location_data(test_instance=None):
        """ Return      locations
                        num_nodes
                        travel time matrix of the truck delta_T
                        travel time matrix of the drone delta_D

            Input       test_instance name
        """

        if test_instance is not None:

            # Define folder paths
            problems_folder = f"{test_instance}/tbl_locations.csv"
            output_distance = f"{test_instance}/tbl_truck_travel_data_PG.csv"

            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_distance), exist_ok=True)

            # Read data from the input file
            # Define the column names
            column_names = ['nodeID', 'nodeType', 'latDeg', 'lonDeg', 'altMeters', 'parcelWtLbs']
            data = pd.read_csv(problems_folder, header=None, names=column_names, skiprows=1)

            # Extract locations and parcel weights
            locations = data[['latDeg', 'lonDeg']].values
            parcel_weight = data['parcelWtLbs'].values

            # Check if the distance file exists
            if os.path.exists(output_distance):
                # Load CSV file
                df = pd.read_csv(output_distance, header=None, names=["from", "to", "time", "distance"], skiprows=1)
                df.columns = df.columns.str.strip()

                # Get the number of unique locations
                unique_locations = sorted(df["from"].unique())
                n = len(unique_locations)

                # Initialize travel time matrix
                time_matrix = np.zeros((n, n))

                # Populate the matrix with travel times
                for _, row in df.iterrows():
                    i, j = int(row["from"]), int(row["to"])
                    time_matrix[i, j] = row["distance"]/(truck_speed)


        num_nodes = len(locations)

        euclidean_distance_matrix = np.zeros((num_nodes, num_nodes))

        # Calculate great-circle distance between each pair of points
        for i in range(num_nodes):
            for j in range(i+1, num_nodes):
                start_point = locations[i]
                end_point = locations[j]
                
                # Compute great-circle distance in kilometers
                distance = ox.distance.great_circle(start_point[0], start_point[1], end_point[0], end_point[1]) # in meters
                euclidean_distance_matrix[i, j] = distance
                euclidean_distance_matrix[j, i] = distance  # Symmetric matrix

        # Compute travel time matrices
        delta_T = time_matrix
        delta_D = euclidean_distance_matrix / drone_speed
        
        # Checking travel matrix
        for i in range(len(delta_T)):
            for j in range(i+1, len(delta_T)):
                if delta_D[i,j] > delta_T[i,j]:
                    print("Check travel time matrix at node({},{}): Drone time = {}, Truck time = {}".format(i,j,delta_D[i,j],delta_T[i,j]))
            

        return locations, num_nodes, parcel_weight, delta_T, delta_D



### Using 
l,n, p, T, D = process_location_data("Ulsan/9/20250819T150214242836")
print("locations: ", l)
print("number of node: ", n)
print("parcel weight: ", p)
print("Truck travel matrix: ", T)
print("Drone travel matrix: ", D)