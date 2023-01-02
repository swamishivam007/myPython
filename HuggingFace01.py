import gradio as gr

gr.Interface.load("models/facebook/bart-large-cnn").launch(share=True)