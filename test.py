import gradio as gr
from transformers import pipeline

model = pipeline("text-generation")

def predict(prompt):
    completion = model(prompt)[0]["generated_text"]
    return completion

gr.Interface(fn=predict, inputs="text", outputs="text").launch()
