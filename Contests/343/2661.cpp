#include <vector>
#include <unordered_map>

using namespace std;

// My Solution
class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        unordered_map<int, int> row_map;
        unordered_map<int, int> col_map;
        int m = mat.size();
        int n = mat[0].size();
        // m, n = mat.size(), mat[0].size();

        // Map locations of each element first
        unordered_map<int, std::pair<int, int>> location;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++) {
                location[mat[i][j]] = make_pair(i, j);
            }
        }

        for(int i=0;i<arr.size();i++) {
            pair loc = location[arr[i]];
            // x, y = loc.first, loc.second;
            int x = loc.first;
            int y = loc.second;
            if(row_map.find(x) == row_map.end()){
                row_map[x] = 1;
            }else{
                row_map[x] += 1;
            }

            if(row_map[x]==n) {
                return i;
            }

            if(col_map.find(y)==col_map.end()) {
                col_map[y]=1;
            }else{
                col_map[y]+=1;
            }
            if(col_map[y]==m){
                return i;
            }
        }
        return 0;
    }
};

// Improved
class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<int> rows(m, 0);
        vector<int> cols(n, 0);

        unordered_map<int, std::pair<int, int>> location;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++) {
                location[mat[i][j]] = {i, j};
            }
        }

        for(int i=0;i<arr.size();i++) {
            pair loc = location[arr[i]];
            int r = loc.first, c = loc.second;
            if(++rows[r] == n) return i;
            if(++cols[c] == m) return i;
        }
        return 0;
    }
};