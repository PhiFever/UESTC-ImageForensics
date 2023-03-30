import numpy as np


def get_feature(matrix: list):
    """
    :param matrix:由8*8的DCT变换后的小矩阵组成的二维数组
    :return:
    """
    vec_arr = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            vec_arr.append({"vec": get_zigzag(matrix[i][j]), "x": i, "y": j})
    vec_arr.sort(key=cmp)

    res={}
    for i in range(len(vec_arr))[1:]:
        dis_vec=cal_dis_vec(vec_arr[i-1],vec_arr[i])
        if not res.__contains__(dis_vec):
            res[dis_vec]=set([(vec_arr[i],vec_arr[i-1])])
        else:
            res[dis_vec].add((vec_arr[i],vec_arr[i-1]))

    return res

def get_zigzag(matrix: np.ndarray) -> list:
    """
    :param matrix:8*8的DCT变换后的小矩阵
    :return: z字形排列后得到的列表
    """
    res = []
    f = 0
    loc = {"x": 0, "y": 0}
    n, m = matrix.shape
    n -= 1
    m -= 1
    while loc["x"] <= n and loc["y"] <= m:
        if f == 0:
            while loc["x"] < n and loc["y"] > 0:
                res.append(matrix[loc["x"]][loc["y"]])
                loc["x"] += 1
                loc["y"] -= 1
            res.append(matrix[loc["x"]][loc["y"]])
            if loc["x"] < n:
                loc["x"] += 1
            else:
                loc["y"] += 1
            f ^= 1
        else:
            while loc["x"] > 0 and loc["y"] < m:
                res.append(matrix[loc["x"]][loc["y"]])
                loc["x"] -= 1
                loc["y"] += 1
            res.append(matrix[loc["x"]][loc["y"]])
            if loc["y"] < m:
                loc["y"] += 1
            else:
                loc["x"] += 1
            f ^= 1
    return res


def cmp(a: dict) -> list:
    return a["vec"]


# 计算位移向量
def cal_dis_vec(a: dict, b: dict) -> tuple:
    x = a["x"] - b["x"]
    y = a["y"] - b["y"]
    if x < 0:
        x = -x
        y = -y
    elif x == 0 and y < 0:
        y = -y
    return (x, y)
