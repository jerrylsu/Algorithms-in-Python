#include<iostream>
#include<vector>
#include<string>

using namespace std;

class Solution{
    public:
        vector<vector<string>> solveNQueens(int n){
            vector<vector<string>> res;
            vector<string> nQueens(n, string(n, '.'));
            dfs(nQueens, res, 0, n);
            return res;
        }

        void dfs(vector<string>& nQueens, vector<vector<string>>& res, int row, int& n){
            if(row == n){                             // N层树
                res.push_back(nQueens);
                return;
            }
            for(int col = 0; col < n; ++col){         // N叉树
                if(isValid(nQueens, row, col, n)){    // 剪枝
                    nQueens[row][col] = 'Q';
                    dfs(nQueens, res, row + 1, n);
                    nQueens[row][col] = '.';
                }
            }
        }

        bool isValid(vector<string>& nQueens, int row, int col, int& n){
            // 检查坐标(row, col)在column（上半部）上是否存在'Q'
            for(int i = 0; i < row; ++i){
                if(nQueens[i][col] == 'Q') return false;
            }
            // 检查坐标(row, col)在45°对角线（上半部）上是否存在'Q'
            for(int i = row, j = col; i >= 0 && j < n; --i, ++j){
                if(nQueens[i][j] == 'Q') return false;
            }
            // 检查坐标(row, col)在135°对角线（上半部）上是否存在'Q'
            for(int i = row, j = col; i >= 0 && j >= 0; --i, --j){
                if(nQueens[i][j] == 'Q') return false;
            }
            return true;
        }
};

