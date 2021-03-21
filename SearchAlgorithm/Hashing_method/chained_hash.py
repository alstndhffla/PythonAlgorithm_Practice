# 체인법으로 해시함수

from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    """
    해시를 구성하는 노드
    """

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    """
    체인법을 해시 클래스 구현현
    """