import numpy as np
import random
from datetime import timedelta, datetime
from algorithms.spatiotemporal01 import spatiotemporal01
from models.node import Node
from views.plot import showPlot
from models.pod import Pod
from models.timeslot import Timeslot


def generate_pods(num_pods):
    pods = []
    for i in range(num_pods):
        deadline_hours = random.randint(5, 20)  # Example range for deadline hours
        duration = random.randint(1, 5)  # Example range for duration
        powerConsumption = random.randint(10, 100)  # Example range for power consumption
        cpuRequest = random.randint(10, 100)  # Example range for CPU request
        ramRequest = random.randint(10, 100)  # Example range for RAM request
        storageRequest = random.randint(10, 100)  # Example range for storage request
        pod = Pod(i, deadline_hours, duration, powerConsumption, cpuRequest, ramRequest, storageRequest)
        pods.append(pod)
    return pods


def generate_nodes(num_nodes):
    nodes = []
    for i in range(num_nodes):
        embodiedCarbon = random.randint(455000, 2502000)  # Example range for embodied carbon
        lifetime = 4  # Example range for lifetime
        cpuLeft = random.randint(1000, 10000)  # Example range for CPU left
        ramLeft = random.randint(1000, 10000)  # Example range for RAM left
        storageLeft = random.randint(1000, 10000)  # Example range for storage left
        node = Node(i, embodiedCarbon, lifetime, cpuLeft, ramLeft, storageLeft)
        nodes.append(node)
    return nodes


def assign_pods_to_nodes(nodes, pods):
    for i, pod in enumerate(pods):
        nodes[i % len(nodes)].addPod(pod)


def generate_timeslots(num_timeslots):
    timeslots = []
    now = datetime.now()
    start_time = now.replace(minute=0, second=0, microsecond=0)
    for i in range(num_timeslots):
        slot_time = start_time + timedelta(hours=i)
        timeslot = Timeslot(i, slot_time.year, slot_time.month, slot_time.day, slot_time.hour, 2)
        timeslots.append(timeslot)
    return timeslots


def generate_avg_carbon_intensities(nodes, timeslots):
    avgCarbonIntensities = np.zeros((len(nodes), len(timeslots)))
    for i in range(len(nodes)):
        for j in range(len(timeslots)):
            avgCarbonIntensities[i, j] = random.randint(10, 1000)  # Random values between 10 and 1000
            print(f"Node {i} - Timeslot {j}: {avgCarbonIntensities[i, j]}")
    return avgCarbonIntensities


if __name__ == '__main__':
    pods = generate_pods(0)
    nodes = generate_nodes(10)
    assign_pods_to_nodes(nodes, pods)

    timeslots = generate_timeslots(10)
    avgCarbonIntensities = generate_avg_carbon_intensities(nodes, timeslots)

    podToSchedule = Pod(5, 4, 2, 1, 50, 50, 50) # powerConsumption in kW

    bestNode, bestTimeslot, totalEmissionsPerNode = spatiotemporal01.execute(podToSchedule, nodes, timeslots, avgCarbonIntensities)
    print(f"Best node: {bestNode.id}")
    print(f"Best timeslot: {bestTimeslot.id}")

    showPlot(nodes, timeslots, totalEmissionsPerNode, bestNode.id, bestTimeslot.id)
