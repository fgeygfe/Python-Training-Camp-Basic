def skip_multiples_of_three(n):
    """
    返回从1到n的所有非3的倍数的整数列表
    
    参数:
    - n: 正整数上限
    
    返回:
    - 从1到n中所有不是3的倍数的整数列表
    """
    result = []  # 初始化结果列表
    for num in range(1, n + 1):  # 遍历1到n的数字
        if num % 3 == 0:  # 如果是3的倍数
            continue      # 跳过当前数字
        result.append(num)  # 否则添加到结果列表
    return result  # 返回最终结果
