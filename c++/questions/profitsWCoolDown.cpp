#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
/**
 * @brief Given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
        You may buy and sell one NeetCoin multiple times with the following restrictions:
        After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
        You may only own at most one NeetCoin at a time.
        You may complete as many transactions as you like.
 * 
 * @param prices : vector<int>& is the prices of the market on the respective days.
 * @return int : the maximum profit you can achieve.
 */
    int maxProfit(vector<int>& prices) {
        this->prices = prices;
        return dfs(0, "yes");
        
    }
private:
    unordered_map<string, int> cache;
    vector<int> prices;
    int dfs(int i, string buying){
        if (i >= prices.size()) return 0;

        if (cache.count(to_string(i) + buying) > 0) return cache[(to_string(i) + buying)];

        if (buying == "yes") {
            cache[(to_string(i) + buying)] = max(dfs(i + 1, "no") - prices[i], dfs(i + 1, "yes"));
        } /* buy */ else {
            cache[(to_string(i) + buying)] = max(dfs(i + 1, "no"), dfs(i + 2, "yes") + prices[i]);
        } /* sell */
        return cache[(to_string(i) + buying)];
    }
};
