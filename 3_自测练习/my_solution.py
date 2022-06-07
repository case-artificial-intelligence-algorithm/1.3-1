#!/usr/bin/env python3

# 待测试程序
def solution(G):
    in_degrees = dict((u, 0) for u in G)    # 对图G中的每个节点匹配一个入度的属性
    
    for u in G: # 计算每个节点的入度
        for v in G[u]:
            in_degrees[v] += 1

    Q = [u for u in G if in_degrees[u] == 0]    # 定义用于存储图G中入度为0的节点队列Q

    S = []  # S是存储拓扑序列顶点的列

    while Q:
        u = Q.pop() # 弹出入度为0的节点
        S.append(u) # 将该节点添加到拓扑序列中

        raise NotImplementedError('编写相邻节点入度更新的代码')


    if len(S) == len(G):    # 如果拓扑序列中的节点数与图G中的节点数相等，则说明图G是有向无环图
        return S
    else:
        return False


if __name__ == '__main__':
    pass
