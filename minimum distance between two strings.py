def shortestDistance(s, word1, word2) :

	d1 = -1; d2 = -1
	ans = 100000000

	# Traverse the string
	for i in range(len(s)):
		if (s[i] == word1):
			d1 = i
		if (s[i] == word2):
			d2 = i
		if (d1 != -1 and d2 != -1):
			ans = min(ans, abs(d1 - d2))
	return ans


S = [ "the", "quick", "brown", "fox", "quick" ]
word1 = "the"; word2 = "fox"

print(shortestDistance(S, word1, word2))
