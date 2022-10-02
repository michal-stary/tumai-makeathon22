from risk import RiskEstimatorGPT3
from human import HumanEstimator
class Scorer():
    def __init__(self, models_folder = "models"):
        self.risker = RiskEstimatorGPT3()

        self.humaner = HumanEstimator(f"{models_folder}/model_human")
        # self.humaner = lambda x: 0

    def __call__(self, text, **kwargs):
        risk, law = self.risker(text)
        return {"risk": risk, "human":self.humaner(text),
                "law": law if risk else "No high-risk law identified"}