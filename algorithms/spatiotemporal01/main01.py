from datetime import timedelta, datetime

import numpy as np

from algorithms.spatiotemporal01 import spatiotemporal01
from models.node import Node
from views.plot import showPlot
from models.pod import Pod
from models.timeslot import Timeslot

def generate_timeslots(num_timeslots):
    timeslots = []
    now = datetime.now()
    start_time = now.replace(minute=0, second=0, microsecond=0)
    for i in range(num_timeslots):
        slot_time = start_time + timedelta(hours=i)
        timeslot = Timeslot(i, slot_time.year, slot_time.month, slot_time.day, slot_time.hour, 2)
        timeslots.append(timeslot)
    return timeslots

if __name__ == '__main__':
    dummyPod1 = Pod(0, 10, 2, 10, 50, 50, 50)
    dummyPod2 = Pod(1, 10, 2, 10, 50, 50, 50)
    dummyPod3 = Pod(2, 10, 2, 10, 50, 50, 50)
    dummyPod4 = Pod(3, 10, 2, 10, 50, 50, 50)
    dummyPod5 = Pod(4, 10, 2, 10, 50, 50, 50)

    node0 = Node(0, 10, 10, 3000, 3000, 3000)
    node1 = Node(1, 10, 10, 3000, 3000, 3000)
    node2 = Node(2, 10, 10, 3000, 3000, 3000)





    nodes = [node0, node1, node2]
    timeslots = generate_timeslots(5)

    avgCarbonIntensities = np.zeros((len(nodes), len(timeslots)))

    avgCarbonIntensities[0, 0] = 300
    avgCarbonIntensities[0, 1] = 100
    avgCarbonIntensities[0, 2] = 130
    avgCarbonIntensities[0, 3] = 160
    avgCarbonIntensities[0, 4] = 190

    avgCarbonIntensities[1, 0] = 220
    avgCarbonIntensities[1, 1] = 250
    avgCarbonIntensities[1, 2] = 600
    avgCarbonIntensities[1, 3] = 900
    avgCarbonIntensities[1, 4] = 1

    avgCarbonIntensities[2, 0] = 420
    avgCarbonIntensities[2, 1] = 121
    avgCarbonIntensities[2, 2] = 842
    avgCarbonIntensities[2, 3] = 453
    avgCarbonIntensities[2, 4] = 318

    podToSchedule = Pod(5, 10, 1, 10, 50, 50, 50)

    bestNode, bestTimeslot, totalEmissionsPerNode = spatiotemporal01.execute(podToSchedule, nodes, timeslots, avgCarbonIntensities)
    print(f"Best node: {bestNode.id}")
    print(f"Best timeslot: {bestTimeslot.id}")

    showPlot(nodes, timeslots, totalEmissionsPerNode, bestNode.id, bestTimeslot.id)
