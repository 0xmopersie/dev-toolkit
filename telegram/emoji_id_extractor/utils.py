from telegram import MessageEntity


def extract_custom_emojis(
    entities: list[MessageEntity] | None,
) -> list[dict]:
    if not entities:
        return []

    results = []

    for entity in entities:
        if entity.type != MessageEntity.CUSTOM_EMOJI:
            continue

        results.append(
            {
                "id": entity.custom_emoji_id,
                "offset": entity.offset,
                "length": entity.length,
                "type": "Custom Emoji",
            }
        )

    return results