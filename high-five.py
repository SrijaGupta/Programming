iclass Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        # dicti={}
        # d=items[0][0]
        # l=[]
        # output=[]
        # item=sorted(items)
        # for sid,score in item:
        #     if sid == d:   #dicti ={}
        #         l.append(score)
        #     else:
        #         dicti[d]=sum(sorted(l,reverse=True)[0:5])/5 if len(l) > 4 else sum(l)/len(l)
        #         l=[score]
        #         d=sid
        # dicti[d]=sum(sorted(l,reverse=True)[0:5])/5 if len(l) > 4 else sum(l)/len(l)
        # for k,v in dicti.items():
        #     output.append([k,v])
        # return output
        d = {}
        score_list = []
        out = []
        for sid, score in items:
            if d.get(sid) is None:
                d[sid] = [score]
            else:
                d[sid] += [score]
        for sid, scores in d.items():
            avg_score = sum(d[sid])/len(d[sid]) if len(d[sid]) < 5 else sum(sorted(d[sid], reverse=True)[:5])/5 
            out.append([sid, avg_score])
            
        return out
            
