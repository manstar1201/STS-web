import torch
import torch.nn as nn
import transformers

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.plm = transformers.AutoModelForSequenceClassification.from_pretrained(
            pretrained_model_name_or_path='monologg/koelectra-base-v3-discriminator', num_labels=1)
    
    def forward(self, x):
        x = self.plm(x)['logits']
        return x
