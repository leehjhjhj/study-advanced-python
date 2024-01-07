"""
Futures 동시성
비동기 작업 실행
지연시간(Block) CPU 및 리소스 낭비를 방지 -> (file)Network I/O 관련 작업 -> 동시성 작업 권장
비동기 작업과 적합한 프로그램일 경우 압도적으로 성능이 향상된다.

futures: 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
concurrent.Futures
1. 멀티 스레딩 / 멀티 프로세싱 API 통일 -> 매우 사용하기 쉬움
2. 실행 중인 작업 취소, 완료 여부 체크, 타임 아웃 옵션, 콜백 함수 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

GIL(Global Interpreter Lock): 두 개 이상의 쓰레드가 동시에 실행 될 때, 하나의 자원을 엑세스 하는 경우 문제점을 방지하기 위해서
                            GIL이 실행된다. 즉 리소스 전체에 락이 걸린다. -> Context switch(문맥 교환)
GIL 우회: 멀티프로세싱, CPython 을 이용
"""
# 2가지 패턴 실습
# concurrent.futures의 사용법1

import os
import time
from concurrent import futures
WORK_LIST = [10000, 1000000, 10000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker count
    worker = min(10, len(WORK_LIST))
    start_time = time.time()

    # 결과 건수
    # ProcessPoolExcutor
    with futures.ThreadPoolExecutor() as excutor:
        # map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)

    end_time = time.time() - start_time
    msg = '\n Result -> {} Time : {:.2f}s'
    print(msg.format(list(result), end_time))

if __name__ == '__main__':
    main()


