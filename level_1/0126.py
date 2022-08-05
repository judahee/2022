#손익분기점 (백준 1712번 문제)

A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else :
    print(A//(C-B)+1)
