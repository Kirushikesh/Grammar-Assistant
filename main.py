from utils import process_audio
import gradio as gr

# Set up Gradio interface
iface = gr.Blocks()

def transcribe_speech(token,filepath):
    if not token:
        return "Please enter a Hugging Face token.", "", None
    
    if filepath is None:
        gr.Warning("No audio found, please retry.")
        return ""
    transcription, output_audio = process_audio(token,filepath)
    return transcription, output_audio

mic_transcribe = gr.Interface(
    fn=transcribe_speech,
    inputs=[ 
        gr.Textbox(label="Enter your Hugging Face token", type="password"),
        gr.Audio(sources="microphone",type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Original Transcription"),
        gr.Audio(label="Corrected Speech",)
    ],
    allow_flagging="never")


file_transcribe = gr.Interface(
    fn=transcribe_speech,
    inputs=[
        gr.Textbox(label="Enter your Hugging Face token", type="password"),
        gr.Audio(sources="upload",type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Original Transcription"),
        gr.Audio(label="Corrected Speech")
    ],
    allow_flagging="never",
)

with iface:
    gr.TabbedInterface(
        [
            mic_transcribe, 
            file_transcribe
        ],
        ["Transcribe Microphone",
         "Transcribe Audio File"],
        title="Speech Grammar Correction",
    )

# Launch the interface
if __name__ == "__main__":
    iface.launch()