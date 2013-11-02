#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This module provides a class that detect a particular word in the text.
# This module has been tested on python ver.2.6.6.
# ver1.31102
# (C) 2013 Matsuda Hiroaki 


import re
import os

class Text():

    def check_text(self, text_path, *check_path):
        '''
        Check Text File.
        check_text(text path, check list path 1, ..., check list path N)
        '''
        
        lines = self._read_textfile(text_path)

        words = []
        for path in check_path:
            print path
            words += self._read_checklist(path)
            
        for count, line in enumerate(lines):
            line = self._encode(line) 
            
            for word in words:
                word = self._encode(word)

                if re.search(re.escape(word), line) != None:
                    print('Line: %d Word: %s') %(count + 1, word)

    def _read_textfile(self, file_path):
        file_exists = os.path.exists(file_path)

        if file_exists == True:
            print('Tex file: %s') % file_path

        else:
            raise('File path error: Please check your TEX path.')

        text = open(file_path)
        lines = text.readlines()
        text.close()

        return lines
    
    def _read_checklist(self, file_path):
        file_exists = os.path.exists(file_path)

        if file_exists == True:
            print('Check List file: %s') % file_path

        else:
            raise('File path error: Please check your Check List path.')
        
        text = open(file_path)
        lines = text.readlines()
        text.close()

        words = [line.replace('\r\n', '').replace('\r', '').replace('\n', '') for line in lines]

        if len(words) > 0:
            return words

        else:
            raise('File error: Please chech your check list.')

    def _encode(self, text):

        try:
            return text.decode('utf-8')
        except:
            pass

        try:
            return text.decode('shift-jis')
        except:
            pass

        try:
            return text.decode('enu-jp')
        except:
            pass

        try:
            return text.decode('iso2022-jp')
        except:
            pass


if __name__=="__main__":
    t = Text()
    t.check_text('test.tex', 'basic.txt', 'sice.txt') 
