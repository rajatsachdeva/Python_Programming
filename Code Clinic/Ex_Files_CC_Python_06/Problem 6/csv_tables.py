#!/usr/bin/python3
# csv_tables.py by Barron Stone
# This is an exercise file from Python Code Clinic on lynda.com

import os
import csv

__version__ = '0.2.1'

HTML_PATH = '.\\programs\\graphic-design.htm'
CSV_FILES = ('.\\_assets\\first_semester.csv',
             '.\\_assets\\second_semester.csv')
SP_INC = 2 # number of spaces to increment by

def create_row(row_data, **kwargs):    
    sp = ' ' * kwargs.get('line_space', 0) # leading spaces     
    output = sp + '<tr>\n'
    sp += SP_INC * ' ' # increase lead spacing
     
    if kwargs.get('is_header', False):
        for item in row_data:
            output += sp + '<th>' + item + '</th>\n'
    else:      
        first_col = row_data[0].split(' ', 1) # first word of first column is <strong>
        output += sp + '<td><strong>' + first_col[0] + ' </strong>' + first_col[1] + '</td>\n'
        for item in row_data[1:]:
            output += sp + '<td>' + item + '</td>\n'
 
    sp = sp[:-SP_INC] # decrease lead spacing
    return output + sp + '</tr>\n'  
    
def create_table(table_data, **kwargs): # create table from list-of-lists
    border = str(kwargs.get('border', 0))
    cellspacing = str(kwargs.get('cellspacing', 0))
    cellpadding = str(kwargs.get('cellpadding', 0))
    sp = ' ' * kwargs.get('line_space', 0) # leading spaces   
    output = sp + '<table border="' + border + '" cellspacing="' + cellspacing + '" cellpadding="' + cellpadding + '">\n'              
    sp += SP_INC * ' ' # increase lead spacing
       
    output += create_row(table_data[0], line_space = len(sp), is_header = True) # first row is a header
    for row_data in table_data[1:]: # remaining rows are data
        output += create_row(row_data, line_space = len(sp))
    
    sp = sp[:-SP_INC] # decrease lead spacing
    return output + sp + '</table>\n' 
    
def insert_csv(html_path, csv_paths):   
    html_orig = open(html_path)
    html_halves = html_orig.read().split('</article>')
    sp = (len(html_halves[0]) - len(html_halves[0].rstrip(' '))) # number of spaces before </article> tag
    
    new_tables = ''
    for path in csv_paths:
        print('Building table from ' + path)
        file = open(path, 'r')
        csv_data = list(csv.reader(file, delimiter=','))        
        new_tables += create_table(csv_data, line_space = sp + 2)

    print('Inserting tables into copy of ' + html_path)
    output_html = html_halves[0].rstrip(' ') + new_tables + (sp * ' ') + '</article>' + html_halves[1]
    output_path = os.path.dirname(html_path) + '\\output.htm'
    print('Saving result to ' + output_path) 
    output_file = open(output_path, 'w')
    output_file.write(output_html)
    
if __name__ == "__main__": insert_csv(HTML_PATH, CSV_FILES)