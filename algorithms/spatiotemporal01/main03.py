import numpy as np

from algorithms.spatiotemporal01 import spatiotemporalalgorithm
from models.node import Node
from views.plot import showPlot
from models.pod import Pod
from models.timeslot import Timeslot

if __name__ == '__main__':
    dummyPod1 = Pod(0, 10, 2, 10, 50, 50, 50)
    dummyPod2 = Pod(1, 10, 2, 10, 50, 50, 50)
    dummyPod3 = Pod(2, 10, 2, 10, 50, 50, 50)
    dummyPod4 = Pod(3, 10, 2, 10, 50, 50, 50)
    dummyPod5 = Pod(4, 10, 2, 10, 50, 50, 50)

    node0 = Node(0, 100, 10, 3000, 3000, 3000)
    node1 = Node(1, 200, 10, 3000, 3000, 3000)
    node2 = Node(2, 300, 10, 3000, 3000, 3000)

    timeslot1 = Timeslot(0, 2024, 6, 20, 15, 5)
    timeslot2 = Timeslot(1, 2024, 6, 20, 13, 5)
    timeslot3 = Timeslot(2, 2024, 6, 20, 14, 5)
    timeslot4 = Timeslot(3, 2024, 6, 20, 15, 5)
    timeslot5 = Timeslot(4, 2024, 6, 20, 16, 1)

    nodes = [node0, node1, node2]
    timeslots = [timeslot1, timeslot2, timeslot3, timeslot4, timeslot5]

    avgCarbonIntensities = np.zeros((len(nodes), len(timeslots)))

    avgCarbonIntensities[0, 0] = 900
    avgCarbonIntensities[0, 1] = 900
    avgCarbonIntensities[0, 2] = 900
    avgCarbonIntensities[0, 3] = 900
    avgCarbonIntensities[0, 4] = 900

    avgCarbonIntensities[1, 0] = 100
    avgCarbonIntensities[1, 1] = 100
    avgCarbonIntensities[1, 2] = 100
    avgCarbonIntensities[1, 3] = 100
    avgCarbonIntensities[1, 4] = 100

    avgCarbonIntensities[2, 0] = 100
    avgCarbonIntensities[2, 1] = 100
    avgCarbonIntensities[2, 2] = 100
    avgCarbonIntensities[2, 3] = 100
    avgCarbonIntensities[2, 4] = 100

    podToSchedule = Pod(5, 10, 1, 10, 50, 50, 50)

    bestNode, bestTimeslot, totalEmissionsPerNode = spatiotemporalalgorithm.execute(podToSchedule, nodes, timeslots,
                                                                                    avgCarbonIntensities)
    print(f"Best node: {bestNode.id}")
    print(f"Best timeslot: {bestTimeslot.id}")

    showPlot(nodes, timeslots, totalEmissionsPerNode, bestNode.id, bestTimeslot.id)
