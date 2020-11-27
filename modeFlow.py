from taskflow import engines
from taskflow.patterns import linear_flow
import TaskPool
from FlowPool import GraphicAlertFlow

class Mode5Flow():
    def __init__(self, shadowModel):
        self.shadowModel = shadowModel
        self.mode5Flow = linear_flow.Flow(self.__class__.__name__)
        self.graphicAlertFlow = GraphicAlertFlow(self.__class__.__name__,"Yolo").buildFlow()

    def buildFlow(self):
        self.mode5Flow.add(
            TaskPool.frameTask(self.__class__.__name__ + '_frameTask', provides = "frame"),
            TaskPool.yoloTask(self.__class__.__name__ + '_yoloTask', requires= "frame", provides="Yolo"),
            self.graphicAlertFlow 
        )
        result = engines.load(self.mode5Flow, store={'shadowModel':self.shadowModel}, engine = "parallel")
        result.run()

def runFlow(shadowModel):
	Mode5Flow(shadowModel).buildFlow()
