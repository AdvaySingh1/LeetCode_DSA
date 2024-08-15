// O(n) apprach
#include <vector>
#include <unordered_set>
#include <string>
#include <queue>
using namespace std;

class Solution {
public:
    /**
     * @brief Solves the problem with O(n * m) time and space.
     * 
     * @param board 
     */
    void solve(vector<vector<char>>& board) {
        this->board = board;
        capture();

        for (int r = 1; r < board.size() - 1; r++){
            for (int c = 1; c < board[0].size() - 1; c++){
                if (board[r][c] == 'O'
                    && visited.count(to_string(r) + ',' + to_string(c)) == 0){
                        board[r][c] = 'X';
                }
            }
        }
    }

private:
    unordered_set<string> visited;
    vector<vector<char>> board;
        
        /**
         * @brief Using BFS, it marks every 'O' which is not sorrounded
         * By an 'X' in the in the Visited map.
         * 
         * @param i (int) for the row
         * @param j (int) for the col
         */
        void markVisited(int i, int j){
        // define a queue for bfs
        queue<pair<int, int>> q; q.push({i, j});
        vector<pair<int, int>> neighbors = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (q.size() > 0){
            int r = q.front().first, c = q.front().second; q.pop();
            visited.insert(to_string(r) + ',' + to_string(c));
            for (auto & p: neighbors){
                int dr = r + p.first, dc = c + p.second;
                if (dr >= 0 && dr < board.size()
                    && dc >= 0 && dc < board[0].size()
                    && visited.count(to_string(dr) + ',' + to_string(dc)) == 0
                    && board[dr][dc] == 'O'){
                        q.push({dr, dc});
                }
            }
        }
    }

    /**
     * @brief Using the markVisited function, it captures the board.
     * @link this->markVisited() @endlink
     */
    void capture(){
        for (int r = 0; r < board.size(); r++){
            if (board[r][0] == 'O') markVisited(r, 0);
            if (board[r][board[0].size() - 1] == 'O') markVisited(r, board[0].size() - 1);
        }
        for (int c = 0; c < board[0].size(); c++){
            if (board[0][c] == 'O') markVisited(0, c);
            if (board[board.size() - 1][c] == 'O') markVisited(board.size() - 1, c);
        }
    }
};



// O(m^2 * n^2) solution DFS
// class Solution {
// public:
//     void solve(vector<vector<char>>& board) {
//         for (int r = 1; r < board.size() - 1; r++){
//             for (int c = 1; c < board[0].size() - 1; c++){
//                 vector<pair<int, int>> toConvert;
//                 if (board[r][c] == 'O' && visited.count(to_string(r) + ',' + to_string(c)) == 0) {
//                     if (changeColors(r, c, board, toConvert)){
//                         for (auto & pair: toConvert){
//                             board[pair.first][pair.second] = 'X';
//                         }
//                     }
//                 }
//             }
//         }
//     }

//     bool changeColors(int r, int c, vector<vector<char>>& board, vector<pair<int, int>>& toConvert){
//         // dfs
//         bool isSorrounded = true;
//         visited.insert(to_string(r) + ',' + to_string(c));
//         vector<pair<int, int>> neighbors = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
//         for (auto & pair: neighbors){
//             int dr = r + pair.first, dc = c + pair.second;
//             if (dr >= 0 && dr < board.size() 
//             && dc >= 0 && dc < board[0].size()){
//                 if (visited.count(to_string(dr) + ',' + to_string(dc)) == 0
//                     && board[dr][dc] == 'O'){
//                         isSorrounded = changeColors(dr, dc, board, toConvert) && isSorrounded;
//                 }
//             } else {
//                 isSorrounded = false;
//             }
//         }
//         visited.erase(to_string(r) + ',' + to_string(c));
//         if (isSorrounded) {
//             toConvert.push_back({r, c});
//             return true;
//         }
//         return false;
//     }

// private:
//     unordered_set<string> visited;
// };
