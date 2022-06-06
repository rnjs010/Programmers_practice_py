# Greedy (탐욕법) - stack(LIFO)
def solution(number, k):
    answer = []
 
    for num in number:
        while k > 0 and answer and num > answer[-1]:
            answer.pop()
            k -= 1
        answer.append(num)

    answer = ''.join(answer[:len(answer) - k])
    return answer

print(solution("4177252841", 4))