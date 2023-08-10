s = input()
h = len(s) // 2
print(s[:h] == s[:len(s)-h-1:-1]) 