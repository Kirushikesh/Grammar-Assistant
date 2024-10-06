# Configuration settings

# Model names
ASR_MODEL = "openai/whisper-tiny"
GRAMMAR_MODEL = "meta-llama/Llama-3.2-1B-Instruct"
TTS_MODEL = "facebook/mms-tts-eng"

# Prompts
GRAMMAR_CORRECTION_SYSTEM_PROMPT = """You are a helpful assistant that is trained to correct grammar mistakes in text. You need to identify each of the mistakes in the user text and you should provide suggestion on which part of the grammer the user should improve. Your output should be short and consise. If the user text is grammatically correct then you should appreciate saying its correct.
"""

# Other settings
MAX_NEW_TOKENS = 200
TEMPERATURE = 0.2
SAMPLING_RATE =16000