# with open('file.txt', 'w') as f:
#     f.write("123")  



# f = open("file.txt" , "w")
# f.write("222")


# my_list = []
# for i in range(100000):
#     f = open("file.txt", "w")
#     my_list.append(f)
#     f.close()



# class Context:
#     def __enter__(self):
#         print("...start")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("...exit")

# with Context():
#     print("Какой-то обёрнутый код")

# print("А это уже после менеджера")


# import time 

# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
#     def __enter__(self):
#         print("...start")
#         self.start = time.time()
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"Время выполнения кода {time.time() - self.start} сек")
#         print("...exit")
        
#         if exc_type is TypeError:
#             return True

# with RunningCodeJudge():
#     my_list = [x for x in range(1,100000)]
#     my_list -= "s"



# my_list = [1, 2, 3, 4, 5]
# list_iterator = iter(my_list)
# print(next(list_iterator))

# for i in my_list:
#     print(i) 



# import random

# class RandomIter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.__reload = limit
#     def __iter__(self):
#         self.limit = self.__reload

#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         self.limit-= 1
#         return random.randint(0, 100)
# rand_iter = RandomIter(5)
# print(next(rand_iter))
# print(next(rand_iter))
# print(next(rand_iter))
# print(next(rand_iter))
# print(next(rand_iter))

# for rand_int in rand_iter:
#     print(rand_int) 



# class MyFile: 
#     def __init__(self, filename, mode, encoding='utf-8'): 
#         self.filename = filename 
#         self.mode = mode 
#         self.encoding = encoding 
 
#     def __enter__(self): 
#         self.file = open(self.filename, self.mode, encoding=self.encoding) 
#         return self.file 
 
#     def __exit__(self, exc_type, exc_val, exc_tb): 
#         self.file.close()



# class InfiniteIterator: 
#     def __init__(self, start): 
#         self.start = start 
 
#     def __iter__(self): 
#         return self 
 
#     def __next__(self): 
#         self.start += 1 
#         return self.start - 1