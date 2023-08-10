class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0 || x != 0 && x % 10 == 0)
            return false;
        int check = 0;
        while (x > check)
        {
            check = check * 10 + x % 10;
            x /= 10;
        }
        return (x == check || x == check / 10);
    }
};

//best time
class Solution
{
public:
    bool isPalindrome(int x)
    {
        long result = 0;
        int remainder;
        int z = x;
        while (x != 0)
        {
            if (x < 0)
            {
                return false;
            }
            remainder = x % 10;
            result = (result * 10) + remainder;
            x = x / 10;
        }
        if (result == z)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

//best space
class Solution
{
public:
    bool isPalindrome(int x)
    {
        int i = x;
        long int s = 0;
        while (x > 0)
        {
            s = (s * 10) + x % 10;
            x /= 10;
        }
        return (s == i);
    }
};