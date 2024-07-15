import logging
from datetime import datetime

import numpy as np
import time


def execute(pod, nodes, timeslots, carbonForecast):
    start_time = time.time()
    minEmissions = np.inf
    bestNode = None
    bestTimeslot = None
    totalEmissionsPerNode = np.zeros((len(nodes), len(timeslots)))
    for timeslot in timeslots:
        if isTimeslotValid(timeslot, pod):
            for node in nodes:
                if checkNodeResource(node, pod):
                    # todo check Duration
                    operationalEmissions = (carbonForecast[node.id][
                        timeslot.id]) * pod.duration * pod.powerConsumption  # grams, hours, kW
                    embodiedEmissions = ((node.embodiedCarbon / (365 * node.lifetime * 24)) / (
                                node.getPodsCount() + 1)) * pod.duration

                    totalEmissions = operationalEmissions + embodiedEmissions
                    totalEmissionsPerNode[node.id][timeslot.id] = totalEmissions
                    # print(f"Total Emissions of Node {node.id}: {totalEmissions}")
                    if totalEmissions < minEmissions:
                        minEmissions = totalEmissions
                        bestNode = node
                        bestTimeslot = timeslot
                else:
                    totalEmissionsPerNode[node.id][timeslot.id] = np.nan
        else:
            totalEmissionsPerNode[:, timeslot.id] = np.nan
    if bestTimeslot is None:
        print("No available timeslot found")
    if bestNode is None:
        print("No available node found")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
    totalEmissionsPerNode = np.where(np.isnan(totalEmissionsPerNode), totalEmissionsPerNode,
                                     np.round(totalEmissionsPerNode, 3))

    return bestNode, bestTimeslot, totalEmissionsPerNode


def isTimeslotValid(timeslot, pod):
    if pod.deadline > timeslot.getStart():
        if datetime.now() <= timeslot.getEnd():
            return True
        else:
            print(f"Timeslot {timeslot.id} is not valid as it is in the past.")
    else:
        print(f"Timeslot {timeslot.id} is not valid as it is after the deadline.")

    return False


def checkNodeResource(node, pod):
    if node.cpuLeft >= pod.cpuRequest and node.ramLeft >= pod.ramRequest and node.storageLeft >= pod.storageRequest:
        return True
    else:
        print(f"Node {node.id} does not have enough resources to accommodate the pod.")
        return False