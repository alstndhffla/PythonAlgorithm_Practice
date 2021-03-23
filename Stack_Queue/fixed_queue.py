# 고정 길이의 큐 구현하기

from typing import Any


class FixedQueue:

    class Empty(Exception):
        """
        비어있는 FixedQueue 에 대해 deque 또는 peek 를 호출할 때 내보내는 예외처리
        """

    class Full(Exception):
        """
        가득 찬 FixedQueue 에 enque(인큐) 를 호출할 때 내보내는 예외처리
        """

    def __init__(self, capacity: int) -> None:
        """
        초기화
        가득 차 있거나 아니거나 프론트와 리어의 인덱스 값이 같을 수 있다.
        """
        self.no = 0  # 현재 데이터 개수
        self.front = 0  # 맨앞 원소 커서(인덱스)
        self.rear = 0  # 맨끝 원소  커서(인덱스)
        self.capacity = capacity  # 큐의 크기
        self.que = [None] * capacity  # 큐의 본체

    def __len__(self) -> int:
        """
        큐에 있는 모든 데이터 개수를 반환
        :return:
        """
        return self.no

    def is_empty(self) -> bool:
        """
        큐가 비어있는지 판다
        :return:
        """
        return self.no <= 0     # 판단 후 조건에 맞으면 True, 아니면 False

    def is_full(self) -> bool:
        """
        큐가 가득 찼는지 판단
        :return:
        """
        return self.no >= self.capacity     # 판단 후 조건에 맞으면 True, 아니면 False

    def enque(self, x: Any) -> None:
        """
        데이터 x를 인큐
        :param x:
        :return:
        """
        if self.is_full():
            raise FixedQueue.Full   # 큐가 가득 찬 경우, 예외처리 발생
        self.que[self.rear] = x     # 들어온 x 값을 rear 의 추가가
        self.rear += 1  # 리어 인덱스 증가
        self.no += 1    # 원소 개수 증가
        if self.rear == self.capacity:  # 리어 인덱스와 큐 배열의 크기가 같아지면 0으로 이렇게 하면 다음에 인큐하는
                                        # 데이터가 que[0] 에 위치해 제대로 저장된다.
            self.rear = 0

    def deque(self) -> Any:
        """데이터를 디큐합니다"""
        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있는 경우 예외처리를 발생
        x = self.que[self.front]    # 맨 앞에 있는 원소를 뺀다.선입선출
        self.front += 1             # 프론트의 인덱스를 증가(기존 인덱스의 원소 값을 뺐으니) # 프론트를 가리키는 인덱스의 기준을 바꾼거임...
        self.no -= 1                # 원소 갯수 감소
        if self.front == self.capacity:     # 바뀐 프론트 인덱스의 값이 큐 배열의 크기와 같으면 한계에 다다랐다는 것이므로 인덱스를 0으로 옮긴다.
                                            # 다음 디큐 수행시 que[0] 에서 꺼내진다.
            self.front = 0
        return x

    def peek(self) -> Any:
        """데이터를 피크합니다(맨 앞 데이터를 들여다 봄)
        다음 디큐에서 꺼낼 데이터를 들여다 보다는 것이다. front, rear, no 의 값은 변하지 않는다.
        맨 앞 front 데이터만 반환하기 때문.
        """
        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있으면 예외처리를 발생
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        """
        큐에서 value 를 찾아 인덱스를 반환하고 없으면 -1을 반환합니다

        """
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 검색 성공
                return idx
        return -1  # 검색 실패

    def count(self, value: Any) -> bool:
        """큐에 포함되어 있는 value의 개수를 반환합니다"""
        c = 0
        for i in range(self.no):  # 큐 데이터를 선형 검색
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 검색 성공
                c += 1  # 들어있음
        return c    # 갯수를 구해서 반환

    def __contains__(self, value: Any) -> bool:
        """
        큐에 value가 포함되어 있는지 판단합니다
        값이 있으면 True
        """
        return self.count(value)

    def clear(self) -> None:
        """
        큐의 모든 데이터를 비웁니다
        인큐와 디큐는 no, front, rear 의 값을 바탕으로 수행.
        그러므로 값을 0으로만 하면 된다.
        """
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        """
        모든 데이터를 맨 앞에서 맨 끝 순서대로 출력합니다

        """
        if self.is_empty():  # 큐가 비어 있으면 예외처리를 발생
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
