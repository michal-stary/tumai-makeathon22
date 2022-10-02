class Scorer():
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        
        return {"risk": 1, "human":0,
                "law": """Education and vocational training:
(a)        AI systems intended to be used for the purpose of determining access or assigning natural persons to educational and vocational training institutions;
(b)        AI systems intended to be used for the purpose of assessing students in educational and vocational training institutions and for assessing participants in tests commonly required for admission to educational institutions, for determining learning objectives, and for allocating personalised learning tasks to students.
(c)        AI systems intended to be used by children in ways that have a significant impact on their personal development, including through personalised education or their cognitive or emotional development""" }