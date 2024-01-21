from io import BytesIO
import scipy
import torch
from TTS.api import TTS
import numpy as np

from src.resources.types import Text


# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS
tts_api = TTS()
model_name = tts_api.list_models().list_models()[0]
tts = TTS(model_name)

def audio_generator(text_prompt: str, language: str):
    amplitudes = tts.tts(text=text_prompt, speaker="Ana Florence", language=language)
    amplitudes_norm = np.array(amplitudes) * (32767 / max(0.01, np.max(np.abs(np.array(amplitudes)))))
    amplitudes_norm = np.array(amplitudes_norm).astype(np.int16)
    buffer = BytesIO()
    scipy.io.wavfile.write(buffer, 22050, amplitudes_norm)
    buffer.seek(0)
    return buffer
