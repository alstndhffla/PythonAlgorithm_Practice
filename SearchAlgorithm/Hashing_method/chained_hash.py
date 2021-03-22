# 체인법으로 해시함수

from __future__ import annotations
from typing import Any, Type
import hashlib  # 해시법 모듈


class Node:
    """
    해시를 구성하는 노드
    노드 클래스는 개별 버킷(해시테이블의 원소)을 나타낸다.
    해당하는 키, 값, 뒤쪽 노드를 참조(next)를 초기화
    """

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    """
    체인법으로 해시 클래스 구현
    """

    def __init__(self, capacity: int) -> None:
        """
        초기화
        매개변수 capacity 에 전달받는 것은 해시 테이블의 크기.
        원소수가 capacity 인 list 형의 배열 table 을 생성하고 모든 원소를 None 으로 한다.
        """
        self.capacity = capacity                # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """
        인수 key 에 대응하는 해시값 구하기
        (내가 원하는 기준으로 해시값을 설정할 수 있다)
        모든 원소를 int 로 한다.
        """
        # int 형일 경우
        if isinstance(key, int):
            return key % self.capacity

        # int 형이 아닐 경우
        # sha256 - 주어진 바이트 문자열의 해시값을 구하는 해시 알고리즘의 생성자(constructor)
        # encode - hashlib.sha256 에는 바이트 문자열의 인수롤 전달해야 한다. 그래서 key를 str 형
        #           문자열로 변환한 뒤 그 문자열을 encode() 함수에 전달하여 바이트 문자열을 생성한다.
        # hexdigest() - sha256 알고리즘에서 해시값을 16진수 문자열로 꺼낸다.
        # int() - hexdigest() 함수로 꺼낸 문자열을 16진수 문자열로 하는 int 형으로 변환한다.
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        """
        키가 key 인 원소를 검색하여 값을 반환
        """
        hash = self.hash_value(key)     # 검색하는 키의 해시값 - 해시 함수를 사용하여 키를 해시값으로 변환하는 과정에 필요
        p = self.table[hash]        # 노드를 노드 - 해시값을 인덱스로 하는 버킷에 주목할 과정에 필요

        while p is not None:
            if p.key == key:
                return p.value  # 키와 같은 값이 발견되면 검색 성공

            p = p.next      # 그게 아니면 뒤쪽 노드에 주목

        return None     # 검색 자체 실패

    def add(self, key: Any, value: Any) -> bool:
        """
        키가 key 이고 값이 value 인 원소를 삽입
        1. 해시 함수를 사용하여 키를 해시값으로 변환
        2. 해시값을 인덱스로 하는 버킷에 주목
        3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 선형 검색 실시
            키와 같은 값이 발견되면 키가 이미 등록된 경우이므로 추가에 실패한다.
            원소의 맨 끝까지 발견되지 않으면 해시값인 리스트의 맨 앞에 노드를 추가한다.
        """
        hash = self.hash_value(key)     # 삽입하는 키의 해시값
        p = self.table[hash]        # 주목하는 노드

        while p is not None:
            if p.key == key:
                return False        # 삽입 실패
            p = p.next      # 뒤쪽 노드에 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp     # 노드를 삽입
        return True     # 삽입 성공

    def remove(self, key: Any) -> bool:
        """
        키가 key 인 원소를 삭제
        1. 해시 함수를 사용하여 키를 해시값으로 변환
        2. 해시값을 인덱스로 하는 버킷에 주목
        3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 선형 검색한다. 키와 같은 값이 발견되면
            그 노드를 리스트에서 삭제한다. 그렇지 않으면 삭제에 실패
        """
        hash = self.hash_value(key)     # 삭제할 키의 해시값
        p = self.table[hash]        # 주목하고 있는 노드
        pp = None       # 삭제 될 키의 바로 앞 주목 노드

        while p is not None:
            if p.key == key:        # key 를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True     # key 삭제 성공
            pp = p
            p = p.next      # 뒤쪽 노드에 주목
        return False        # 삭제 실패(key 가 존재하지 않음)

    def dump(self) -> None:
        """
        해시 테이블을 덤프
        즉, 해시테이블의 내용을 한꺼번에 통째로 출력한다.
        전체 배열의 뒤쪽 노드까지 찾아가면서 각 노드의 키와 값을 출력하는 작업.
        """
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')   # 해시 테이블에 있는 키와 값을 출력
                p = p.next
            print()
