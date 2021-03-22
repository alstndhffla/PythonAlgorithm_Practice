# 고정 길이 스택 구현하기

from typing import Any


class FixedStack:
    """
    고정 길이 스택 클래스
    """

    class Empty(Exception):
        """비어 있는 FixedStack 에 pop 또는 peek 함수를 호출할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack 에 push 를 호출할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """초기화"""
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity      # 스택의 크기
        self.ptr = 0                  # 스택 포인터(스택 비어있는지 여부를 판단)

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수를 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어 있는가?"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택은 가득 찼는가?"""
        return self.ptr >= self.capacity

    # raise 문을 사용해 파이썬은 예외처리를 의도적으로 할 수 있다.
    def push(self, value: Any) -> None:
        """스택에 value 를 푸시"""
        if self.is_full():              # 스택이 가득 참
            raise FixedStack.Full       # 가득 찼을 경우 class 내의 class 인 예외처리 발생
        self.stk[self.ptr] = value      # 그게 아니면 들어온 값을 스택에 현재 포인터에 저장
        self.ptr += 1                   # 기존 포인터는 찼으니 +1 로 변경.

    def pop(self) -> Any:
        """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
        if self.is_empty():             # 스택이 비어 있음
             raise FixedStack.Empty     # 가득 찼을 경우 class 내의 class 인 예외처리 발생
        self.ptr -= 1                   # 포인터의 디폴트는 +1 인 상태이니 -1 을 해주고
        return self.stk[self.ptr]       # -1한 포인터에 있는 value 를 리턴한다.

    def peek(self) -> Any:
        """스택에서 데이터를 피크(꼭대기 데이터를 들여다 봄)"""
        if self.is_empty():             # 스택이 비어 있음
            raise FixedStack.Empty      # 가득 찼을 경우 class 내의 class 인 예외처리 발생
        return self.stk[self.ptr - 1]   # 데이터의 입출력이 없으므로 스택포인터는 변화하지 않는다.

    def clear(self) -> None:
        """
        스택을 비움(모든 데이터를 삭제)
        스택에서 푸시나 팝 등 모든 작업은 스택 포인터 ptr 을 바탕으로 이루진다.
        따라서 스택의 배열 원솟값 자체를 변경할 필요가 없다.
        """
        self.ptr = 0                    # 포인터에 0 을 참조시킨다.

    def find(self, value: Any) -> Any:
        """
        스택에서 value 를 찾아 첨자(없으면 -1)를 반환
        최근에 들어온 포인터-1 을 기준으로 검색을 시작한다.
        -1 씩 줄여가면서.
        """
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기 쪽부터 선형 검색
            if self.stk[i] == value:
                return i  # 검색 성공
        return -1         # 검색 실패시 -1 반환

    def count(self, value: Any) -> bool:
        """
        스택에 포함되어있는 value 의 개수를 반환
        """
        c = 0
        for i in range(self.ptr):  # 바닥 쪽부터 선형 검색(인덱스 0부터 ptr-1까지)
            if self.stk[i] == value:
                c += 1             # 들어 있는 경우 c(카운트) 값을 +1 -> 범위끝까지 반복
        return c    # 최종 카운트 값 반환

    def __contains__(self, value: Any) -> bool:
        """스택에 value 가 있는가?"""
        return self.count(value)

    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
