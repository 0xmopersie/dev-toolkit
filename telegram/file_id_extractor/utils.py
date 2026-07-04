from telegram import PhotoSize


def format_photo_info(photo: PhotoSize) -> str:
    return (
        "📷 Photo Information\n\n"
        f"File ID:\n`{photo.file_id}`\n\n"
        f"Unique File ID:\n`{photo.file_unique_id}`\n\n"
        f"Width: {photo.width}px\n"
        f"Height: {photo.height}px\n"
        f"File Size: {photo.file_size or 'Unknown'} bytes"
    )