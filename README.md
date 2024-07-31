# Scheduling Algorithm Simulator

This project provides a way to test different scheduling algorithms that can be later developed into the model based Meta-Orchestrator of the FLUIDOS project.

The project is yet very simple and only provides a way to test different spatial, temporal, and spatiotemporal algorithms that aims to reduce the carbon footprint of each pod by scheduling them on specific time and location, where and when electricity grid is greener.

## Folder structure

- `algorithms/`: Contains the scheduling algorithms.
- `models/`: Contains the models used by the algorithms (nodes, pods, timeslots...).
- `views/`: Contains the views used to display the results of the algorithms.

## How to run

To run a specific algorithm, call the `__main__` function that generates fake data and calls the chosen algorithm. The pod characteristics can be modified directly in the `__main__` function. The output will be a plot:
- The cell circled in blue represents the result. It corresponds to the tuple `[node;timeslot]` which is the output of the algorithm.
- The value inside each cell represents the amount of CO2 emitted if the pod is scheduled here.
- The color of each cell is a simple way to view the best and worst cells. The coloration is linear.
- Some cells may be in white with "NaN" inside, meaning the timeslot is not valid for the given pod.