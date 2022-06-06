# 정렬
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_c = array[commands[i][0]-1:commands[i][1]]
        array_c.sort()
        answer.append(array_c[commands[i][2]-1])
    return answer


# 다른 풀이1
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# 다른 풀이2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer