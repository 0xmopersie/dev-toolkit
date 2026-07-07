from telegram import (
    Animation,
    Audio,
    Document,
    PhotoSize,
    Video,
    VideoNote,
    Voice,
)


def format_file_info(
    title: str,
    file_id: str,
    unique_file_id: str,
    file_size: int | None,
    width: int | None = None,
    height: int | None = None,
    duration: int | None = None,
    file_name: str | None = None,
    mime_type: str | None = None,
) -> str:

    lines = [
        title,
        "",
        "File ID:",
        f"`{file_id}`",
        "",
        "Unique File ID:",
        f"`{unique_file_id}`",
    ]

    if file_name:
        lines.append(f"File Name: {file_name}")

    if mime_type:
        lines.append(f"MIME Type: {mime_type}")

    if width is not None:
        lines.append(f"Width: {width}px")

    if height is not None:
        lines.append(f"Height: {height}px")

    if duration is not None:
        lines.append(f"Duration: {duration}s")

    lines.append(f"File Size: {file_size or 'Unknown'} bytes")

    return "\n".join(lines)


def format_photo_info(photo: PhotoSize):
    return format_file_info(
        "📷 Photo Information",
        photo.file_id,
        photo.file_unique_id,
        photo.file_size,
        width=photo.width,
        height=photo.height,
    )


def format_video_info(video: Video):
    return format_file_info(
        "🎬 Video Information",
        video.file_id,
        video.file_unique_id,
        video.file_size,
        width=video.width,
        height=video.height,
        duration=video.duration,
        mime_type=video.mime_type,
    )


def format_animation_info(animation: Animation):
    return format_file_info(
        "🎞 Animation Information",
        animation.file_id,
        animation.file_unique_id,
        animation.file_size,
        width=animation.width,
        height=animation.height,
        duration=animation.duration,
        file_name=animation.file_name,
        mime_type=animation.mime_type,
    )


def format_video_note_info(video_note: VideoNote):
    return format_file_info(
        "📹 Video Note Information",
        video_note.file_id,
        video_note.file_unique_id,
        video_note.file_size,
        width=video_note.length,
        height=video_note.length,
        duration=video_note.duration,
    )


def format_document_info(document: Document):
    return format_file_info(
        "📄 Document Information",
        document.file_id,
        document.file_unique_id,
        document.file_size,
        file_name=document.file_name,
        mime_type=document.mime_type,
    )


def format_audio_info(audio: Audio):
    return format_file_info(
        "🎵 Audio Information",
        audio.file_id,
        audio.file_unique_id,
        audio.file_size,
        duration=audio.duration,
        file_name=audio.file_name,
        mime_type=audio.mime_type,
    )


def format_voice_info(voice: Voice):
    return format_file_info(
        "🎤 Voice Information",
        voice.file_id,
        voice.file_unique_id,
        voice.file_size,
        duration=voice.duration,
        mime_type=voice.mime_type,
    )