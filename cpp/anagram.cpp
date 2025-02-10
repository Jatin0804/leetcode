class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        if (s == t)
            return true;
        else
            return false;
    }
};

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_map<char, int> count;

        for (auto x : s)
            count[x]++;
        for (auto x : t)
            count[x]--;

        for (auto x : count)
            if (x.second != 0)
                return false;
        return true;
    }
};

//best time
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        bool ans = 1;
        int hash1[26] = {0};
        int hash2[26] = {0};
        if (s.size() != t.size())
        {
            ans = 0;
        }
        else
        {
            for (int i = 0; i < s.size(); i++)
            {
                hash1[s[i] - 'a']++;
                hash2[t[i] - 'a']++;
            }
            for (int i = 0; i < 26; i++)
            {
                if (hash1[i] != hash2[i])
                {
                    ans = 0;
                    break;
                }
            }
        }
        return ans;
    }
};

//best space

const int ZERO = []()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

class Solution
{
public:
    bool isAnagram(const string &s, const string &t)
    {
        if (s.length() != t.length())
            return false;
        vector<int> freq(26, 0);
        for (int i = 0; i < s.length(); ++i)
        {
            freq[s[i] - 'a']++;
            freq[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; ++i)
            if (freq[i])
                return false;
        return true;
    }
};