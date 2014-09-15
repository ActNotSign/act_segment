act_segment
===========
中文分词
------------
## 版本0.1
   有兴趣可以继续开发
   

### 
      from act import act
      act = act()
      '''
         act.segment(content, tagging, spacemake)
         content   string   内容
         tagging   bool     是否标注词性
         spackmake string   间隔符
         '''
      print act.segment("中华人民",False)

