from fastapi import APIRouter
from fastapi import status
from fastapi.responses import StreamingResponse
from src.content.audio_generators import audio_generator
from src.resources.types import Speech, Text


audio_router = APIRouter()


@audio_router.post('/generate_audio', status_code=status.HTTP_201_CREATED)
def generate_audio_from_text(options: Text):
    audio_buffer = audio_generator(options.text, options.language)
    return StreamingResponse(audio_buffer, media_type="audio/wav")