#include <vector>
#include <iostream>

class Solution {
public:
    int isWinner(vector<int>& player1, vector<int>& player2) {
        int first1, second1, first2, second2, total1, total2, val1, val2;
        first1 = second1 = first2 = second2 = -1;
        total1 = total2 = 0;

        for(int i=0; i<player1.size(); i++) {
            // player1
            if (first1 == 10 || second1 == 10) {
                val1 = 2 * player1[i];
            } else {
                val1 = player1[i];
            }
            
            // player2
            if (first2 == 10 || second2 == 10) {
                val2 = 2 * player2[i];
            } else {
                val2 = player2[i];
            }

            total1 += val1;
            second1 = first1;
            first1 = player1[i]; 

            total2 += val2;
            second2 = first2;
            first2 = player2[i];
        }

        if (total1 > total2) {
            return 1;
        } else if (total2 > total1) {
            return 2;
        } else {
            return 0;
        }
    }
};