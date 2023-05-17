n = int(input())
a = list(map(int, input().split(" ")))


def insertionSort(A: list, N: int):
    print(*A, sep=" ")

    for i in range(1, N):
        v = A[i]  # 選択
        j = i - 1
        while j >= 0 and A[j] > v:  # はみ出ていない，かつ，選択した数より大きい
            A[j + 1] = A[j]  # 値を一つ後ろにずらす
            j -= 1
        A[j + 1] = v

        print(*A, sep=" ")


insertionSort(a, n)
