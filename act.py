#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
from dictionary import dictionary

reload(sys)
sys.setdefaultencoding('utf8')

class act (object):

    def __init__(self):
        print 'loading dict'
        dictionary.loaddictionary()
        print 'over'
        self.string = ''
        pass

    def check(self, __tmp_word):
        return dictionary.check(__tmp_word)

    def isEnglish(self, __char):
        asciicode = ord(__char)
        if 97 <= asciicode <= 122 or 65 <= asciicode <= 90 or 48 <= asciicode <= 57 or \
            32 < asciicode <= 47 or 49 <= asciicode <= 64 or 91 <= asciicode <= 96 or \
            123 <= asciicode <= 126:
            return True
        else :
            return False

    def isnumber(self, a):
        try:
            float(a)
            return True
        except:
            return False

    def segment(self, in_content, in_tagging = True,  space_mark = "    "):
        print '---------segment-----------'
        self.string = ""
        self.fullmapping(in_content.decode("utf-8"),in_tagging, space_mark)
        return self.string

    def fullmapping(self, in_content,in_tagging = True, space_mark = "    "):
        __str_len = len(in_content)
        __tagging = 'comb'
        """
            last word
            """
        if 1 >= __str_len:
            if in_content != '':
                __status = dictionary.check(in_content)
                if __status.get('s') != None:
                    __tagging = __status.get('s')
                self.string += in_content+"/"+__tagging+"    "
            return

        """
            depath
            """
        __forward_char = __segment_word = __tmp_word = in_content[0]
        for index in range(1, __str_len):
            __char = in_content[index]
            if self.isEnglish(__forward_char) and self.isEnglish(in_content[index]):
                __segment_word += __char
                pass
            elif dictionary.check(__tmp_word).get('status'):
                __segment_word = __tmp_word
                __tmp_word += __char
                if __str_len == len(__tmp_word) and dictionary.check(__tmp_word).get('status'):
                    __segment_word = __tmp_word
                __tmp_s = dictionary.check(__segment_word).get('s')
                if __tmp_s != None:
                    __tagging = __tmp_s
                pass
            else:
                break
            __forward_char = in_content[index-1]

        if self.isnumber(__segment_word):
            __tagging = 'm'

        if in_tagging:
            self.string += __segment_word+"/"+__tagging+space_mark
        else:
            self.string += __segment_word+space_mark

        self.fullmapping(in_content[len(__segment_word):__str_len], in_tagging, space_mark)
        pass
