__author__ = "ResearchInMotion"

arr = [1,3,2,3]

def monotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

print(monotonic(arr))