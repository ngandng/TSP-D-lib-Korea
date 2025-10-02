# TSP-D-lib-Korea
This repository provides benchmark instances for **vehicle routing problem (VRP) variants**, including: CVRP, TSP, TSP-D, FSTSP, VRPD, and related extensions.  

The dataset is built from real-world road networks in South Korea.  

## Cities and Regions

Currently, two cities are available:  

- **Ulsan**  
  - Longitude: 129.306000 – 129.354000  
  - Latitude: 35.521000 – 35.545000  

- **Seoul**  
  - Longitude: 126.903000 – 126.957000  
  - Latitude: 37.494000 – 37.514000  


## Folder Structure

Each city folder follows this structure (followed followed the structure of [mFSTSP](https://github.com/optimatorlab/mFSTSP)):

|-- CityName/
|   |-- num_nodes/
|   |   |-- instance_name/
|   |   |   |-- map.html
|   |   |   |-- tbl_locations.csv
|   |   |   |-- tbl_truck_travel_data-PG.csv

### File Descriptions

- **`map.html`**  
  Interactive HTML map showing the sampled node locations.  

- **`tbl_locations.csv`**  
  Contains node information:  
  - `nodeid`: unique node identifier  
  - `lat`: latitude  
  - `long`: longitude  
  - `nodetype`: `0` = depot, `1` = customer  
  - `parcel_weight`: demand/weight at customer  

- **`tbl_truck_travel_data-PG.csv`**  
  Pairwise travel distances between nodes, computed using [osmnx](https://osmnx.readthedocs.io/) and [NetworkX](https://networkx.org/) based on real road networks (used for truck).  

### Usage
The file `read_instance.py` provide the code to read our data with input of truck speed, drone speed and instance_name.

## Dependencies  

To generate or process the instances, the following Python libraries are used:  
- `osmnx`  
- `networkx`  
- `pandas`  


## Author 
👩🏻‍💻 Thi Thuy Ngan Duong at RML, UNIST