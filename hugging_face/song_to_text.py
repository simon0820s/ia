from transformers import pipeline
import gradio as gr

def run():
    model=pipeline("automatic-speech-recognition",model="facebook/wav2vec2-large-xlsr-53-spanish")
    def transchibe(audio):
        text=model(audio)["text"]
        return text
    
    gr.Interface(
        fn=transchibe,
        inputs=[gr.Audio(source="microphone",type="filepath")],
        outputs=["textbox"],
    ).launch()

if __name__=='__main__':
    run()