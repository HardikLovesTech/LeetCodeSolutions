class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int count[2] = {0 , 0};
        for(int s : students){
            count[s]++;
        }
        for(int k : sandwiches){
            if(count[k] > 0){
                count[k]--;
            }
            else{
                break;
            }
        }
        return count[0]+ count[1];
    }
};