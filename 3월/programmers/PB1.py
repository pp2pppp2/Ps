def v(moves, N, board):
    ans = 0
    q = [-1]
    lb = [0] * (N+1)
    for move in moves:
        move -= 1
        while lb[move] < N and board[lb[move]][move] == 0:
            lb[move] += 1
        if lb[move] == N:
            continue
        if q[-1] == board[lb[move]][move]:
            ans += 2
            q.pop()
        else:
            q.append(board[lb[move]][move])
        lb[move] += 1
    print(q)
    return ans
def solution(board, moves):
    return v(moves, len(board[0]), board)


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
