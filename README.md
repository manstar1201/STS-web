# STS-web
STS Task with finetuned model Web Prototype
# How to Use(Local)
- <code>pip install -r requiremnts.txt</code>
- <code>streamlit run main.py</code>
# How to Use(Cloud)
    [LINK CLICK](https://manstar1201-sts-web-main-xx97wt.streamlit.app/)
## 1. Task
    Semantic Text Similarity
## 2. Model
### Pre-trained model
    monologg/koelectra-base-v3-discriminator
### Fine-tuned model
    1) Pre-trained model with a regression layer
    2) Fine-tuned with 9325 train samples
    3) Output scales : 0-5 float to two decimal points
## 3. Web Prototype
    Streamlit Library
## 4. Reference
    https://github.com/monologg/KoELECTRA
