# run_query_gradio.py
import os
import gradio as gr
from embedchain import App
from dotenv import load_dotenv
load_dotenv() 
app = App.from_config(config_path="config.yaml")

# Query function
def answer_question(question):
    response = app.query(question)
    if hasattr(response, "__iter__") and not isinstance(response, str):
        return "".join(chunk for chunk in response)
    return str(response)

# Gradio UI
demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(label="Ask your question", placeholder="ask a question about your Instagram data..."),
    outputs=gr.Textbox(label="Answer"),
    title="Instagram RAG Chatbot",
    description="Chat with your Instagram data using a Retrieval-Augmented Generation (RAG) model. Ask questions about your indexed data.",
)

if __name__ == "__main__":
    demo.launch(debug=True)  # Set share=True to allow public access

