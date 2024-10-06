![image](https://github.com/user-attachments/assets/d07c3132-d798-4264-89fe-5598b7aa8cae)

# Grammar Assistant

Grammar Assistant is a friendly bot that helps users improve their grammar and provides feedback. It utilizes Auto Speech Recognition (ASR), Natural Language Processing (NLP), and Text to Speech (TTS) technologies through the Hugging Face Inference API.

## Features

- Transcribe speech from microphone input or uploaded audio files
- Correct grammar in the transcribed text
- Provide audio feedback with corrected grammar
- Utilizes Hugging Face Inference API, eliminating the need to download models locally
- Easy-to-use web interface powered by Gradio

## Use Cases

1. **Language Learning**: Ideal for non-native English speakers to practice and improve their grammar in real-time.
2. **Professional Communication**: Helps professionals refine their spoken English for presentations, meetings, or interviews.
3. **Academic Writing**: Assists students in improving the grammatical accuracy of their spoken ideas before writing them down.
4. **Accessibility**: Supports individuals with hearing impairments by providing text transcriptions and corrections.

## Technologies Used

- ASR: OpenAI Whisper (tiny model) for speech recognition
- NLP: Meta Llama 3.2 1B Instruct model for grammar correction
- TTS: Facebook MMS TTS (English) for converting corrected text to speech
- Frontend: Gradio for the user interface
- API: Hugging Face Inference API for model inference

## Installation

1. Clone the repository: `https://github.com/Kirushikesh/Grammar-Assistant.git`
2. Navigate to the project directory:
```cd Grammar-Assistant```
3. Install dependencies using Poetry:
```poetry install```

## Usage

1. Run the application:
```poetry run python main.py```
2. Open the provided URL in your web browser.
3. Enter your Hugging Face API token when prompted.
4. Choose between "Transcribe Microphone" or "Transcribe Audio File" tabs.
5. Record or upload your audio for grammar correction.
6. View the original transcription and listen to the corrected speech.

## Configuration

You can modify the models and settings in the `config.py` file:

- `ASR_MODEL`: Model for Automatic Speech Recognition
- `GRAMMAR_MODEL`: Model for grammar correction
- `TTS_MODEL`: Model for Text-to-Speech conversion
- `GRAMMAR_CORRECTION_SYSTEM_PROMPT`: System prompt for grammar correction
- `MAX_NEW_TOKENS`: Maximum number of new tokens for grammar correction
- `TEMPERATURE`: Temperature setting for the language model
- `SAMPLING_RATE`: Audio sampling rate

## Advantages of Using Hugging Face Inference API

- No need to download large model files locally
- Reduced computational requirements on the user's machine
- Easy access to state-of-the-art AI models
- Simplified deployment and maintenance

## Contributing

Contributions to improve the project are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License.
