import logging
import os
import json

logger = logging.getLogger(__name__)

from TTS.api import TTS # For Coqui XTTS

# XTTS model lazy init
tts_model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
os.environ["COQUI_TTS_LICENSE_ACCEPTED"] = "true"

def get_xtts_model():
    try:
        from TTS.api import TTS
        return TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)
    except json.decoder.JSONDecodeError:
        logger.error("XTTS model config is corrupted. Try clearing the cache at ~/.local/share/tts.")
    except Exception as e:
        logger.error(f"XTTS load error: {e}", exc_info=True)
    return None

def synthesize_xtts_audio(full_text: str, speaker_wav_path: str, output_audio_path: str):
    """
    Generates voiceover using Coqui XTTS model with voice cloning.
    Removed desired_speed parameter.
    """
    coqui_tts_model = get_xtts_model()
    target_language = 'cn'
    if coqui_tts_model is None:
        raise RuntimeError("TTS model not available.")
    try:
        coqui_tts_model.tts_to_file(
            text=full_text,
            speaker_wav=speaker_wav_path,
            language=target_language,
            file_path=output_audio_path,
            split_sentences=True
        )
        logger.info(f"Coqui XTTS voiceover generated successfully for {output_audio_path}")
    except Exception as e:
        logger.error(f"❌ Coqui XTTS voice cloning failed: {e}. Attempting fallback to OpenAI.", exc_info=True)
        raise
