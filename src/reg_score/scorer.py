from risk import RiskEstimator
class Scorer():
    def __init__(self):
       self.risker = RiskEstimator()


    def __call__(self, text, **kwargs):
        risk, law = self.risker(text)
        return {"risk": float(risk), "human":0,
                "law": law if risk else "No high-risk law identified"}