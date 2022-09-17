## 15.BackTracking
框架
```
def backtrack(全局变量, 路径):
    if 满足结束条件：
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        if 判断是是否可以做当前选择:
            continue
        做选择
        backtrack(全局变量, 路径)
        撤销选择
```

[46.Permuations](https://github.com/jerrylsu/Algorithms-in-Python/blob/master/15.BackTracking/46.Permuations.py)
[51.N-Queens](https://github.com/jerrylsu/Algorithms-in-Python/blob/master/15.BackTracking/51.N-Queens.py)


## References

[leetcode](https://leetcode.com/problemset/all/)
[算法导论](https://www.bilibili.com/video/BV1rt411c7dV/)
[labuladong的算法](https://labuladong.gitee.io/algo/)