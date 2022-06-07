# 완전탐색
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    li = []
    for i in range(1, total):
        if total % i == 0:
            li.append(i)

    for i in range(len(li) // 2 + 1):
        width = total // li[i]
        if li[i] - 2 + width == (brown // 2):
            answer.append(width)
            answer.append(li[i])
            
    return answer


# 더 간단한 방법
def solution(brown, yellow):

    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if (i + yellow//i) * 2 == brown-4:
                return [yellow//i+2, i+2]