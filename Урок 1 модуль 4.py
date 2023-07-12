

# s = "aab"
# for sym in set(s):
#     count = 0
#     for sub_sym in s:
#         if sub_sym == sym:
#             count+=1
#     print(sym, count)


s = "aab"
syms_counter = {}
for sym in s:
    syms_counter[sym] = syms_counter.get(sym)+1
print(syms_counter)


