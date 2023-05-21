#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int minimumCost(vector<int> start, vector<int> target, vector<vector<int> > specialRoads) {
        vector<vector<int>> visited;
        vector<bool> empty;
        for(int i=0;i<=target[0];i++) {
            empty.push_back(false);
        }
        return f(start, target, start[0],start[1], specialRoads, dp);
    }

    int f(vector<int> start, vector<int> target, int x, int y, vector<vector<int> > spr, vector<vector<int> >& dp) {
        return 0;
    }
};

int main(){
    vector<int> v = {1,1};
    vector<int> v2 = {4,6};
    vector<vector<int> > sp = {{3,4,2,4,1},{2,5,4,2,5},{3,2,1,6,3}};
    cout<<Solution().minimumCost(v, v2, sp);
    return 0;
}