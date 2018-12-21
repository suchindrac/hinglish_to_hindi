#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getch

hindi_map = {}
fd_out = None
tdata = [] 
totr = ""
tfin = ""

def parse():
        fd = open('map.txt', 'r')
        for line in fd.readlines():
            line_list = line.split()

            hindi_map[line_list[0].strip()] = line_list[1].strip()

def translate(ch):
    global tdata
    global totr
    global tfin

    totr += ch

    if ch == ' ':
        tfin += ' '
        return

    try:
        tdata.append(hindi_map[totr])

        #
        # If translated data list is just one character, then the final
        #  translated character is the only character in the list
        #
        if len(tdata) == 1:
            tfin += tdata[-1]

        #
        # If translated data list is more than 1 character in size, 
        #  then the final translated character is the last character in
        #  the list
        #
        if len(tdata) > 1:
            tfinl = [c for c in tfin]
            tfinl[-1] = tdata[-1]
            tfin = "".join(tfinl)

        sys.stdout.write("\r" + tfin)

        return
    except KeyError:

        #
        # If translation could not happen,
        #  then, if total number of characters attempted to translate now
        #  is greater than 2, then quit translating the sequence of 
        #  characters, and just translate the current character as a new one
        #
        if len(totr) > 2:
            totr = ''
            tdata = []
            translate(ch)
        else:
            return


translated = False
fd_out = open('translated_text.txt', 'w')

parse()

while True:
    try:
        ch = getch.getch()
        if ch == '\n':
            fd_out.write(tfin)
            break
        translate(ch)
    except:
        fd_out.write(tfin)
        break

fd_out.close()
