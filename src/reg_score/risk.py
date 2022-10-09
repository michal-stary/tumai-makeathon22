import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import re
from numpy import dot
from numpy.linalg import norm
import openai

class RiskEstimatorDeberta():
    def __init__(self, model_path, 
                       model_name="MoritzLaurer/DeBERTa-v3-xsmall-mnli-fever-anli-ling-binary"):
        
        self.tokenizer = AutoTokenizer.from_pretrained(
                model_name)
        self.model = torch.load(model_path)


    def __call__(self, text, **kwargs):
        self.encodings = self.tokenizer([text], return_tensors="pt", padding=True)
        item = {key: torch.tensor(val[0]) for key, val in self.encodings.items()
                
        output = self.model(**item)
        return (output.logits > 0).float(), ""
                
openai.api_key = "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"
class RiskEstimatorGPT3():
    def __init__(self):
        pass
    def __call__(self, text, **kwargs):
        response = openai.Answer.create(
            model="text-davinci-002",
            file="file-Bil7GJIkeNbj8rJurv0V210c",
            question=f"""How is the startup which is {text}. Concerns this text? Yes or no""",
            examples_context="In 2017, U.S. life expectancy was 78.6 years.",
            examples=[["What is human life expectancy in the United States?", "78 years."]],
            max_tokens=256,
        )
        print(response['answers'][0])
        return response['answers'][0], response["selected_documents"][-1]['text']

    
    
    
class RiskEstimatorCosine():
    def __init__(self):
        with open("src/annex_data.txt") as f:
            annex_file = f.read()
        self.df_annex = self.parse_numbered(annex_file)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        sentences_annex = self.df_annex[0].to_list()
        self.embeddings_annex = self.model.encode(sentences_annex)

    def __call__(self, text, **kwargs):

        a = self.embeddings_annex
        b = self.model([text])
        cos_sim = (a @ b.T) / (norm(a) * norm(b))
        print(cos_sim.argmax(0) > 0.025, self.df_annex.iloc[cos_sim.argmax(0)])
        return cos_sim.argmax(0)[0] > 0.025, self.df_annex.iloc[cos_sim.argmax(0)[0]]


    def parse_numbered(self, text):
        mapp = dict()
        activate = False
        num = None
        for txt in re.split("\\n([0-9])\.", text):
            if txt.isdigit():
                activate = True
                num = int(txt)
            elif activate:
                mapp[num] = txt
                activate = False
        end = text.split("8a")[1]
        mapp[9], mapp[10] = re.split("\([a-b]\)", end)[1:]
        mapp[8] = mapp[8].split("8a")[0]
        mapp[10] = mapp[10].split("Version")[0]
        return pd.DataFrame(pd.Series(mapp.values()))

