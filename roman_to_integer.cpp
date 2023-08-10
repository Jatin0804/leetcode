class Solution
{
public:
    int romanToInt(string s)
    {
        unordered_map<char, int> mp{
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };
        int ans = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (mp[s[i]] < mp[s[i + 1]])
                ans -= mp[s[i]];
            else
                ans += mp[s[i]];
        }
        return ans;
    }
};

//best time

class Solution
{
public:
    int romanToInt(string s)
    {
        int sum = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char curr = s.at(i);
            if (curr == 'M')
            {
                sum += 1000;
            }
            else if (curr == 'D')
            {
                sum += 500;
            }
            else if (curr == 'L')
            {
                sum += 50;
            }
            else if (curr == 'V')
            {
                sum += 5;
            }
            else if (i < s.length() - 1)
            {
                // subtractions
                char next = s.at(i + 1);
                if (curr == 'C')
                {
                    if (next == 'D')
                    {
                        sum += 400;
                        i++;
                    }
                    else if (next == 'M')
                    {
                        sum += 900;
                        i++;
                    }
                    else
                    {
                        sum += 100;
                    }
                }
                else if (curr == 'X')
                {
                    if (next == 'L')
                    {
                        sum += 40;
                        i++;
                    }
                    else if (next == 'C')
                    {
                        sum += 90;
                        i++;
                    }
                    else
                    {
                        sum += 10;
                    }
                }
                else if (curr == 'I')
                {
                    if (next == 'V')
                    {
                        sum += 4;
                        i++;
                    }
                    else if (next == 'X')
                    {
                        sum += 9;
                        i++;
                    }
                    else
                    {
                        sum += 1;
                    }
                }
            }
            else if (curr == 'C')
            {
                sum += 100;
            }
            else if (curr == 'X')
            {
                sum += 10;
            }
            else if (curr == 'I')
            {
                sum += 1;
            }
            else
            {
                return -1;
            }
        }
        return sum;
    }
};