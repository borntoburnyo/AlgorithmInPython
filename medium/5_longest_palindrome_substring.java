class Solution {
	public String longestPalindrome(String s) {
		if (s == null || s.length() < 1) return "";
		int lo = 0, hi = 0;
		for (int i = 0; i < s.length(); i++) {
			int len1 = maxPalindrome(s, i, i);
			int len2 = maxPalindrome(s, i, i+1);
			int len = Math.max(len1, len2);
			if (len > hi - lo) {
				lo = i - (len - 1) / 2;
				hi = i + len / 2;
			}
		}
		return s.substring(lo, hi + 1);
	}
	
	private int maxPalindrome(String s, int left, int right) {
		int L = left, R = right;
		while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
			L--;
			R++;
		}	
		return R - L - 1;
	}
}
