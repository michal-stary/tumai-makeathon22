from transformers import AutoTokenizer, AutoModel, AutoConfig
from torch.utils import checkpoint
import torch



class HumanEstimator():
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "bert-base-uncased",
            do_lower_case=True
        )
        self.model = torch.load(model_path)

    def __cal__(self, text):
        encoded = self.tokenizer.encode_plus(
            text,
            None,
            add_special_tokens=False,
            max_length=512,
            padding="max_length",
            return_token_type_ids=True,
            truncation=True
        )
        ids = torch.LongTensor([encoded['input_ids']])
        mask = torch.LongTensor([encoded['attention_mask']])
        return float(self.model(ids, mask)[0].cpu().detach().numpy())


class CustomModel(torch.nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()
        self.distill_bert = AutoModel.from_pretrained(
            "bert-base-uncased"
        )

        self.top1 = torch.nn.Linear(768, 64)
        self.top2 = torch.nn.Linear(64, 1)  # classify the data into N laws described in the training dataset

        self.dropout1 = torch.nn.Dropout(p=0.3)
        self.sigm = torch.nn.Sigmoid()

    def forward(self, ids, mask):
        x = self.distill_bert(ids, mask)[0][:, 0, :]
        # select the first token only as it is trained for classifier
        x = torch.nn.functional.relu(self.top1(x))
        x = self.dropout1(x)
        x = self.top2(x)
        return self.sigm(x)