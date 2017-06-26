import numpy as np
# 输入矩阵
A = np.array([[3, 1, 2],
              [5, 6, 7],
              [4, 2, 6]])
# 卷积核矩阵
f = np.array([[1, -1],
              [-1, 1]])

# 卷积运算转换矩阵运算
def transform(A, f):
    m_A = A.shape[0]
    m_f = f.shape[0]
    n_A = A.shape[1]
    n_f = f.shape[1]
    m = m_A + m_f - 1
    n = n_A + n_f - 1
    # print(m, n)
    # 对输入矩阵进行延拓补零
    A = np.vstack((A, np.zeros([m - m_A, n_A])))
    A = np.hstack((A, np.zeros([m, n - n_A])))
    # print(A)
    # 对卷积核矩阵进行延拓补零
    f = np.vstack((f, np.zeros([m - m_f, n_f])))
    f = np.hstack((f, np.zeros([m, n - n_f])))
    # print(f)
    # 对输入矩阵进行转换
    A = A.flatten()
    # print(A)
    # 对卷积核矩阵进行转换
    f2 = np.zeros([f.shape[0], f.shape[1]])
    f2[0, :] = f[0, :]
    for i in range(1, m):
        f2[i, :] = f[m - i, :]
    # print(f2)
    f4 = np.zeros([n, n])  # 存放每一行生成的子矩阵
    f1 = np.zeros([m * n, m * n])  # 存放最终转换生成的矩阵
    for i in range(m):
        # print(f2[i])
        for j in range(n):  # 对卷积核矩阵的每一行生成子矩阵
            for k in range(1, n + 1):
                t = (j + k) % n
                if t == 0: t = n
                f4[k - 1, t - 1] = f2[i, j]
        # print(f4)
        for k in range(m):  # 对子矩阵放置到正确位置
            t = (i + 1 + k) % m
            if t == 0: t = m
            f1[(t - 1) * n:t * n, k * n:(k + 1) * n] = f4
    temp = np.dot(f1, A).reshape([m, n])
    temp = np.vstack((temp[-1,], temp[:-1, ]))
    result = np.zeros([m, n])
    for i in range(m):
        for j in range(n):
            k = j + 1
            if k == n: k = 0
            result[i, k] = temp[i, j]
    print(result)

# 主程序调用转换函数
if __name__=="__main__":
    transform(A, f)
