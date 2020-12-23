def count(s, k):
    words = s.split()
    res = []
    for i in range(len(words)):
       if (len(words[i]) < k):
           res.append(words[i])
    return res;