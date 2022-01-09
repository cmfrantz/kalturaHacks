#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Carie Frantz'
__email__ = 'cariefrantz@weber.edu'
"""DataProcessing
Created on Sun Jan 9 14:48:09 2022
@author: cariefrantz
@project: Teaching

Strips Kaltura captions from *.srt files for editing and transcripts

Arguments:  None

Example in command line:
    python kalturaCaptionStripper.py

Dependencies Install:
    sudo apt-get install python3-pip python3-dev
    pip install os
    pip install sys
    pip install pandas
    pip install tkinter

Copyright (C) 2022  Carie M. Frantz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>

####################
# TO DO
####################
For now, the script only strips text from the srt files.
The code is built so that in the future, a script could re-import edited
text files and save them as *.srt files for re-uploading edited captions.

"""

####################
# IMPORTS
####################
import os
import pandas as pd
from tkinter import *
from tkinter import filedialog



####################
# VARIABLES
####################
'''
Format of transcript file:
    Line 1 = identifying number for the snippet
    Line 2 = times for the snippet
    Line 3-n = text
    Line n+1 = blank
'''
demark = '\n'


####################
# SCRIPTS
####################

def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in the list
    listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

#%%
####################
# MAIN FUNCTION
####################
if __name__ == '__main__': 
    # Select files (UI)
    root = Tk()
    fileList = filedialog.askopenfilenames(initialdir=os.getcwd(), filetypes=[('SRT','*.srt')], title = 'Select transcripts')
    root.destroy()
    dirPath=os.path.dirname(fileList[0])
    
    # Parse files into text transcripts
    for file in fileList:
        # Read in the text
        with open(file) as f:
            lines=f.readlines()
        indices = [0] + [1+r for r in get_index_positions(lines, demark)]
        indices = indices[0:-1]
        
        # Create the table
        table = pd.DataFrame(index=range(len(indices)), columns=['n','time','text'])
        for n, r in enumerate(indices):
            table.loc[n,'n']=lines[r]
            table.loc[n,'time']=lines[r+1]
            if n<len(indices)-1:
                table.loc[n,'text']=lines[r+2:indices[n+1]-1]
            else:
                table.loc[n,'text']=lines[r+2:-1]
                
        # Save the text file where each line is a caption entry
        text = ''
        text = [text+' '.join(table.loc[r,'text']).replace('\n', '')
                for r in table.index]
        textfile = open(file[:-4]+'_text.txt','w')
        for line in text:
            textfile.write(line+'\n')
        textfile.close()
        


        
            

    