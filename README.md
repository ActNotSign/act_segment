act_segment
===========
中文分词
------------
###   文件结构
      dict  
            - core.dict    序列化之后的核心词库
            - custom.dict  自定义字典
            - symbol.dict  自定义字符扩张
            
      wordtree.py
            树构建类
            
      dictionary.py
            字典类
            
      act.py
            分词操作类
      
      words.txt
            文本词
            
            结构
               词 词性  词频
      
###   使用方法 
      from act import act
      act = act()
      '''
         act.segment(content, tagging, spacemake)
         content   string   内容
         tagging   bool     是否标注词性
         spackmake string   间隔符
         '''
      print act.segment("中华人民",False)


###   只为开源
      贡献自己的力量
