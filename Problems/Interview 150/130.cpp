#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    void DFS(int i, int j, int rows, int cols, vector<vector<char>>& board) {
        if(i<0 || j<0 || i>=rows || j>=cols || board[i][j] != 'O') return;

        board[i][j] = 'B';
        DFS(i-1, j, rows, cols, board);
        DFS(i+1, j, rows, cols, board);
        DFS(i, j+1, rows, cols, board);
        DFS(i, j-1, rows, cols, board);
    }

    void solve(vector<vector<char>>& board) {
        int rows = board.size(), cols = board[0].size();
        for(int i=0; i<rows; i++) {
            if(board[i][0] == 'O') {
                DFS(i, 0, rows, cols, board);
            }

            if(board[i][cols-1] == 'O') {
                DFS(i, cols-1, rows, cols, board);
            }
        }

        for(int i=0; i<cols; i++) {
            if(board[0][i] == 'O') {
                DFS(0, i, rows, cols, board);
            }
            if(board[rows-1][i] == 'O') {
                DFS(rows-1, i, rows, cols, board);
            }
        }

        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if(board[i][j]=='O') {
                    board[i][j] = 'X';
                } else if(board[i][j] == 'B') {
                    board[i][j] = 'O';
                }
            }
        }
    }
};
