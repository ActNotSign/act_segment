#!/usr/bin/env python
import os,sys,json,time
reload(sys)
sys.setdefaultencoding('utf8')

class tools (object):

    """
        format data
        """
    @staticmethod
    def formatdata():
        words_info = {}
        output = open("wordslibrary1.wd", "a+")
        for line in open ("words.txt"):
            line = line.strip('\n').decode('utf-8')
            __wordsArray = line.split("	")
            __tmp_code_str = ""
            for str_word in __wordsArray[0] :
                __tmp_code_str += str(ord(str_word))
            output.write(__tmp_code_str+' '+__wordsArray[1]+' ')
        output.close()

        pass

    """
        clean data
        """
    @staticmethod
    def cleandata():
        output = open('words.txt' ,'a')
        for line in open ("test.txt"):
            __wordsArray = line.split("	")
            if __wordsArray[1] != 'nw' and __wordsArray[1] != 'comb' :
                output.write(line)
        output.close()
        pass

    """
        add name word to words list
        """
    @staticmethod
    def addname():
        output = open('words.txt' ,'w+')
        for line in open ("name.txt"):
            output.write(line.strip("\n")+"	"+"nr"+"	"+"0\n")
        output.close()
        pass

    """
        load data test
        """
    @staticmethod
    def loadtest():
        wordslibrary = {}
        print time.strftime("%Y-%m-%d %H:%M:%S")
        for line in open ("wordslibrary1.wd"):
            wordlist = line.split(" ")
            len_list = len(wordlist)
            for i in range(0,len_list,2):
                if i+1 < len_list:
                    wordslibrary[long(wordlist[i])] = wordlist[i+1]

        print time.strftime("%Y-%m-%d %H:%M:%S")
        print wordslibrary.get(334573582136713)
        print time.strftime("%Y-%m-%d %H:%M:%S")
        pass

    @staticmethod
    def formatsymbol():
        output = open("symbol.dict", "a+")
        for line in open ("fuhao.txt"):
            line = line.strip('\n').decode('utf-8')
            for symbol in range(0,len(line)):
                output.write(str(ord(line[symbol]))+" wp ")
        output.close()

def switch(param):
    operator = {"-fd":tools.formatdata,
                "-cd":tools.cleandata,
                "-an":tools.addname,
                "-lt":tools.loadtest,
                "-fs":tools.formatsymbol
    }
    if operator.has_key(param):
        operator.get(param)()
    else :
        print "command list \n fd format data \n cd clean data \n an add name word to words list \n lt load data test"
    pass

switch(sys.argv[1])

