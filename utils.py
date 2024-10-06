import config
from huggingface_hub import InferenceClient

def get_client(token):
    return InferenceClient(token=token)

def correct_grammar(client,text):
    response = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content": config.GRAMMAR_CORRECTION_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ],
        max_tokens=config.MAX_NEW_TOKENS,
        model=config.GRAMMAR_MODEL,
        temperature=config.TEMPERATURE,
        stream=False
    )

    return response.choices[0].message.content

def read_audio_file(audio_file):
    with open(audio_file, "rb") as f:
        speech = f.read()
    return speech

def transcribe_audio(client,audio_file):
    audio = read_audio_file(audio_file)

    response = client.automatic_speech_recognition(
        model = config.ASR_MODEL,
        audio = audio
    )
    
    return response.text

def text_to_speech(client,text):
    speech_out = client.text_to_speech(
        text=text, 
        model=config.TTS_MODEL
    )
    return speech_out

def process_audio(token,audio):
    client = get_client(token)
    transcription = transcribe_audio(client,audio)
    corrected_text = correct_grammar(client,transcription)
    output_audio = text_to_speech(client,corrected_text)
    return transcription, output_audio