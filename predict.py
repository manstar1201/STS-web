import torch
import streamlit as st
from model import MyModel
import transformers

@st.cache()
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = MyModel().to(device)
    model.load_state_dict(torch.load("manstar_koelectra.pt"))

    return model


def get_predict(model, s1, s2):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = transformers.AutoTokenizer.from_pretrained('monologg/koelectra-base-v3-discriminator', max_length = 90)
    input_sentence = s1 + '[SEP]' + s2

    tokenized_sentence = tokenizer(input_sentence, return_tensors='pt').to(device)

    result = round(float(model(tokenized_sentence['input_ids'])),3)

    return result
