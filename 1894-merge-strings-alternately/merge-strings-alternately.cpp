class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        result.reserve(word1.size() + word2.size());

        int i = 0, j = 0;

        while (i < word1.size() || j < word2.size()) {
            if (i < word1.size()) {
                result.push_back(word1[i++]);
            }
            if (j < word2.size()) {
                result.push_back(word2[j++]);
            }
        }

        return result;
    }
};