from telegram import MessageEntity


def extract_custom_emojis(entities: list[MessageEntity] | None) -> list[str]:
    if not entities:
        return []

    results = []

    for entity in entities:
        if entity.type == MessageEntity.CUSTOM_EMOJI:
            results.append(entity.custom_emoji_id)

    return results