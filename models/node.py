class Node:
    def __init__(self, id, embodiedCarbon, lifetime, cpuLeft, ramLeft, storageLeft):
        self.id = id
        self.embodiedCarbon = embodiedCarbon
        self.lifetime = lifetime
        self.cpuLeft = cpuLeft
        self.ramLeft = ramLeft
        self.storageLeft = storageLeft
        self.pods = []

    def addPod(self, pod):
        self.pods.append(pod)
        self.cpuLeft -= pod.cpuRequest
        self.ramLeft -= pod.ramRequest
        self.storageLeft -= pod.storageRequest

    def removePod(self, pod):
        self.pods.remove(pod)
        self.cpuLeft += pod.cpuRequest
        self.ramLeft += pod.ramRequest
        self.storageLeft += pod.storageRequest

    def getPodsCount(self):
        return len(self.pods)