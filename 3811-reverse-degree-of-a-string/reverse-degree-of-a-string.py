class Solution(object):
    def reverseDegree(self, s):
        g = {'a':26,'b':25,'c':24,'d':23,'e':22,'f':21,'g':20,'h':19,'i':18,'j':17,'k':16,'l':15,'m':14,'n':13,'o':12,'p':11,'q':10,'r':9,'s':8,'t':7,'u':6,'v':5,'w':4,'x':3,'y':2,'z':1}   
        l = list(s)
        count = 0
        rec = []
        for i in l:
            count += 1
            nums = g[i]*count
            rec.append(nums)
        return sum(rec)