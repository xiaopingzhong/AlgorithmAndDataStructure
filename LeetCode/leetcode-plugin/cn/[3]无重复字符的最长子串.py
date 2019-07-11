# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#


# *********+++++++++++*********========*********+++++++++++*********========
#   问题关键点:
#   找出最长不重复子串:关键点: 找出不重复,找出最长
#   不重复:滑动窗口--常用寻找子序列--滑动窗口的思想
#   找出最长:每次添加的时候,记录子串的长度
# *********+++++++++++*********========*********+++++++++++*********========


# *********+++++++++++*********========*********+++++++++++*********========
# 代码注意点:
#   (1)代码变量的赋值情况要考虑完整:max([])会报错,因此需要特别考虑,所需要计算的列表的长度--尽量考虑全:
#     例子:        if s[i] in slide_window_str:
#                     slide_window_str = slide_window_str.split(s[i])[1]
#                 slide_window_str += s[i]
#                 record_lenght_l.append(len(slide_window_str))
#   (2) 注意积累优秀的代码格式
# *********++++++++++®+*********========*********+++++++++++*********========


# *********+++++++++++*********========*********+++++++++++*********========
#   提交结果:https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190710141412.png
# *********+++++++++++*********========*********+++++++++++*********========

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        ABCDBEAB:
        ABCD-->CDB(删除A)-->CDBE-->CDBEA-->EAB
        :type s: str
        :rtype: int
        """
        slide_window_str = ""
        record_lenght_l = []
        length = 0
        if s == "":
            return length
        else:
            for i in range(len(s)):
                if s[i] in slide_window_str:
                    # Delete all characters that contains duplicate character and before
                    slide_window_str = slide_window_str.split(s[i])[1]
                slide_window_str += s[i]
                # 长度的插入位置需要特别注意,若插在if里面,如果只有一个字符,
                # 外面的record_lenght_l,则会出现[],导致max([])字符串报错的场景
                record_lenght_l.append(len(slide_window_str))
            # judge the length of slide window
            # empty list need caculate independently(Notice),
            # otherwise it will be occur exception named bNull when you submit the code
            if len(record_lenght_l) == 0:
                length = 0
            else:
                length = max(record_lenght_l)
            return length


if __name__ == '__main__':
    solution = Solution()
    max_sub_string = solution.lengthOfLongestSubstring(" ")
    print(max_sub_string)

