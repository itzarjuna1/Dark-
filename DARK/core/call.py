import os
from datetime import datetime, timedelta
from typing import Union
import asyncio

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls
from pytgcalls.types import StreamType
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    TelegramServerError,
)
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo

import config
from DARK import LOGGER, YouTube, app
from DARK.misc import db
from DARK.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_lang,
    get_loop,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
    set_loop,
)
from DARK.utils.exceptions import AssistantErr
from DARK.utils.formatters import check_duration, seconds_to_min, speed_converter
from DARK.utils.inline.play import stream_markup, telegram_markup
from DARK.utils.stream.autoclear import auto_clean
from DARK.utils.thumbnails import get_thumb
from strings import get_string


# Initialization

class Call(PyTgCalls):
    def __init__(self):
        self.clients = []
        self.calls = []
        for i in range(1, 6):
            userbot = Client(
                name=f"KUZEAss{i}",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(getattr(config, f"STRING{i}"))
            )
            call = PyTgCalls(userbot, cache_duration=100)
            setattr(self, f"userbot{i}", userbot)
            setattr(self, f"call{i}", call)
            self.clients.append(userbot)
            self.calls.append(call)

    async def pause_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.pause_stream(chat_id)

    async def resume_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.resume_stream(chat_id)

    async def stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            await remove_active_video_chat(chat_id)
            await remove_active_chat(chat_id)
            db.pop(chat_id, None)
            await assistant.leave_group_call(chat_id)
        except:
            pass

    async def stop_stream_force(self, chat_id: int):
        for call in self.calls:
            try:
                await call.leave_group_call(chat_id)
            except:
                pass
        db.pop(chat_id, None)
        await remove_active_video_chat(chat_id)
        await remove_active_chat(chat_id)

    async def speedup_stream(self, chat_id: int, file_path, speed, playing):
        assistant = await group_assistant(self, chat_id)
        if str(speed) != "1.0":
            base = os.path.basename(file_path)
            chatdir = os.path.join(os.getcwd(), "playback", str(speed))
            os.makedirs(chatdir, exist_ok=True)
            out = os.path.join(chatdir, base)
            if not os.path.isfile(out):
                vs = {"0.5": 2.0, "0.75": 1.35, "1.5": 0.68, "2.0": 0.5}[str(speed)]
                cmd = f"ffmpeg -i {file_path} -filter:v setpts={vs}*PTS -filter:a atempo={speed} {out}"
                proc = await asyncio.create_subprocess_shell(cmd, stdin=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                await proc.communicate()
        else:
            out = file_path

        dur = int(await asyncio.get_event_loop().run_in_executor(None, check_duration, out))
        played, con_seconds = speed_converter(playing[0]["played"], speed)
        duration = seconds_to_min(dur)

        stream_cls = AudioVideoPiped if playing[0]["streamtype"] == "video" else AudioPiped
        stream = stream_cls(
            out,
            audio_parameters=HighQualityAudio(),
            video_parameters=MediumQualityVideo() if stream_cls == AudioVideoPiped else None,
            additional_ffmpeg_parameters=f"-ss {played} -to {duration}"
        )

        if str(db[chat_id][0]["file"]) == str(file_path):
            await assistant.change_stream(chat_id, stream)
            db[chat_id][0].update({
                "played": con_seconds,
                "dur": duration,
                "seconds": dur,
                "speed_path": out,
                "speed": speed,
                "old_dur": db[chat_id][0].get("dur"),
                "old_second": db[chat_id][0].get("seconds")
            })
        else:
            raise AssistantErr("Speed stream mismatch.")

    # Additional functions like force_stop_stream, skip_stream, seek_stream, join_call, change_stream would go here
    # Modular and shorter with reusable subroutines and error handling


call_handler = Call()