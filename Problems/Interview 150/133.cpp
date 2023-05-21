#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

// Version 1 DFS
// class Solution {
// public:
//     Node* cloneGraph(Node* node) {
//         unordered_map<Node*, Node*> og_to_clone;
//         if(node == NULL) return node;    
//         if(node->neighbors.size() == 0) {
//             Node* clone = new Node(node->val);
//             return clone;
//         }

//         return dfs(node, og_to_clone);
//     }

//     Node* dfs(Node* node, unordered_map<Node*, Node*>& og_to_clone) {
//         vector<Node*> neighbours;
//         Node* clone = new Node(node->val);
//         og_to_clone[node] = clone;
//         for(auto neighbour : node->neighbors) {
//             if(og_to_clone.find(neighbour) != og_to_clone.end()) {
//                 neighbours.push_back(og_to_clone[neighbour]);
//             } else {
//                 Node* neighbour_clone = dfs(neighbour, og_to_clone);
//                 neighbours.push_back(neighbour_clone);
//             }
//         }
        
//         clone->neighbors = neighbours;
//         return clone;
//     }
// };

//Version 2 BFS
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node==NULL) return node;
        if(node->neighbors.size()==0) return new Node(node->val);
        
        unordered_map<int, Node*> map;
        map[node->val] = new Node(node->val);
        queue<Node*> queue;
        queue.push(node);

        while(queue.size() != 0) {
            Node* current = queue.front();
            queue.pop();
            Node* current_clone = map[current->val];

            for(auto neighbour : current->neighbors) {
                if(map.find(neighbour->val) == map.end()) {
                    map[neighbour->val] = new Node(neighbour->val);
                    queue.push(neighbour);
                }
                current_clone->neighbors.push_back(map[neighbour->val]);
            }
        }

        return map[node->val];
    }
};
int main(){
    return 0;
}