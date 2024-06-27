/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x<0) {
            return false;
        }
        int num = 0;
        int temp = x;
        while (x != 0) {
            int a = x % 10;
            x = x / 10;
            num = num * 10 + a;
        }
        x = temp;
        return x == num;
    }
}
// @lc code=end

