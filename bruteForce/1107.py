# 리모콘
n = int(input())
m = int(input())

def get_min_buttons():
    # 최솟값을 비교해서 반환해주는 함수
    pass

# 고장난 번호가 있을 경우
if m != 0:
    nums = map(int, input().split())
    nums = list(nums) # str형 리스트

    min_buttons_2 = abs(n - 100)
    for i in range(0, 1000005): # 999999까지
        i = str(i) # i는 채널 번호
                    
        # i의 모든 자릿수 탐색
        for j in range(len(i)):
            if int(i[j]) in nums: 
                break # 2번째 for문 종료 후 i증가 (j)
            if j == len(i) - 1: # j가 i의 자릿수와 같으면 (=한 번도 break문을 안 만나면) 최솟값 갱신
                min_buttons_2 = min(min_buttons_2, int(len(str(i)) + abs(int(i) - int(n))))
    print(min(min_buttons_2, abs(n - 100)))

# 고장난 번호가 없을 경우
else:
    if n == 100:
        print(0)
    elif n == 101 or n == 99:
        print(1)
    elif n == 102 or n == 98:
        print(2)
    else:
        print(len(str(n)))