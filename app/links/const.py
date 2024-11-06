from enum import Enum
from typing import List


class LinkTypeEnum(Enum):
    WEBSITE = 'website'
    BOOK = 'book'
    ARTICLE = 'article'
    MUSIC = 'music'
    VIDEO = 'video'

    @classmethod
    def choices(cls) -> List[tuple]:
        return [(choice.value, choice.name.capitalize()) for choice in cls]
