#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
/**
 * @brief N queens O(n!) solution. O(n^2) space solution. As the tree gets larger (n), the number of options began to decrease hence O(n!)
 * 
 * @param n size of the board
 * @return vector<vector<string>> the possible solutions
 */
    vector<vector<string>> solveNQueens(int n) {
        this->n = n;
        board = vector<vector<char>>(n, vector<char>(n, '.'));
        unordered_set<int> col, leftDiag, rightDiag;
        backTrack(0, col, leftDiag, rightDiag);
        return res;

    }
private:
    int n = 0;
    vector<vector<char>> board;
    vector<vector<string>> res;


    /**
     * @brief Add valid solutions to res
     * 
     * @param r current row
     * @param vert invalid verticals
     * @param leftDiag invalid left diagonals
     * @param rightDiag invalid right diagonals
     */
    void backTrack(int r, unordered_set<int>& vert, 
    unordered_set<int>& leftDiag, 
    unordered_set<int>& rightDiag){

        if (r == n){
            vector<string> copy;
            for (auto & col: board){
                string row(col.begin(), col.end()); // requires col to be vector<char> rather than string
                copy.push_back(row);
            }
            res.push_back(copy);
            return;
        }

        for (int c = 0; c < n; c++){
            if (vert.count(c) == 0 && leftDiag.count(r + c) == 0 && rightDiag.count(r - c) == 0){
                board[r][c] = 'Q';
                vert.insert(c); leftDiag.insert(r + c); rightDiag.insert(r - c);
                
                backTrack(r + 1, vert, leftDiag, rightDiag);

                board[r][c] = '.';
                vert.erase(c); leftDiag.erase(r + c); rightDiag.erase(r - c);
            }
        }
    }   
};
