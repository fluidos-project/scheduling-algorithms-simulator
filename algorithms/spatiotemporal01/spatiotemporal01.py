import logging
import random
from datetime import datetime

import numpy as np
import time

def execute(pod, nodes, timeslots, carbonForecast):
    minEmissions = np.inf
    bestNode = None
    bestTimeslot = None
    totalEmissionsPerNode = np.zeros((len(nodes), len(timeslots)))
    for timeslot in timeslots:
        if isTimeslotValid(timeslot, pod):
            for node in nodes:
                if checkNodeResource(node, pod):
                    operationalEmissions = (carbonForecast[node.id][
                        timeslot.id]) * pod.duration * pod.powerConsumption  # grams, hours, kW
                    embodiedEmissions = ((node.embodiedCarbon / (365 * node.lifetime * 24)) / (
                                node.getPodsCount() + 1)) * pod.duration

                    totalEmissions = operationalEmissions + embodiedEmissions
                    totalEmissionsPerNode[node.id][timeslot.id] = totalEmissions
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
    node.cpuLeft = random.randint(0, 1000)  # Example range for CPU left
    node.ramLeft = random.randint(0, 1000)  # Example range for RAM left
    node.storageLeft = random.randint(0, 1000)  # Example range for storage left
    if node.cpuLeft >= pod.cpuRequest and node.ramLeft >= pod.ramRequest and node.storageLeft >= pod.storageRequest:
        return True
    else:
        print(f"Node {node.id} does not have enough resources to accommodate the pod.")
        return False
