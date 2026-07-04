from telegram import Animation, PhotoSize, Video, VideoNote


def format_file_info(
    title: str,
    file_id: str,
    unique_file_id: str,
    file_size: int | None,
    width: int | None = None,
    height: int | None = None,
    duration: int | None = None,
) -> str:
    lines = [
        f"{title}",
        "",
        "File ID:",
        f"`{file_id}`",
        "",
        "Unique File ID:",
        f"`{unique_file_id}`",
    ]

    if width:
        lines.append(f"Width: {width}px")

    if height:
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
        photo.width,
        photo.height,
    )


def format_video_info(video: Video):
    return format_file_info(
        "🎬 Video Information",
        video.file_id,
        video.file_unique_id,
        video.file_size,
        video.width,
        video.height,
        video.duration,
    )


def format_animation_info(animation: Animation):
    return format_file_info(
        "🎞 Animation Information",
        animation.file_id,
        animation.file_unique_id,
        animation.file_size,
        animation.width,
        animation.height,
        animation.duration,
    )


def format_video_note_info(video_note: VideoNote):
    return format_file_info(
        "📹 Video Note Information",
        video_note.file_id,
        video_note.file_unique_id,
        video_note.file_size,
        video_note.length,
        video_note.length,
        video_note.duration,
    )