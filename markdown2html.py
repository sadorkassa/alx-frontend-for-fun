#!/usr/bin/python3
''' Converts markdown to HTML '''

import sys
import os.path

if __name__ == "__main__":
    ''' Check for correct usage '''
    if len(sys.argv) < 3:
        message = "Usage: ./markdown2html.py README.md README.html"
        print(message, file=sys.stderr)
        exit(1)
    ''' Check if file exists '''
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as md:
        with open(sys.argv[2], 'w') as html:
            ul_list_start = False
            is_ulist = False
            ol_list_start = False
            is_olist = False
            for line in md:

                heading_level = len(line) - len(line.lstrip('#'))

                if line[0] == '-':
                    is_ulist = True
                    if ul_list_start is False:
                        html.write("<ul>\n")
                        ul_list_start = True
                    html.write("<li>" + line.lstrip('-').strip() + "</li>\n")

                if line[0] == '*':
                    is_olist = True
                    if ol_list_start is False:
                        html.write("<ol>\n")
                        ol_list_start = True
                    html.write("<li>" + line.lstrip('*').strip() + "</li>\n")

                if is_ulist and line[0] != '-':
                    ul_list_start = False
                    is_ulist = False
                    html.write("</ul>\n")

                if is_olist and line[0] != '*':
                    ol_list_start = False
                    is_olist = False
                    html.write("</ol>\n")

                if heading_level >= 1 and heading_level <= 6:
                    htmlline = "<h{}>".format(heading_level)
                    htmlline += line.lstrip('#').strip()
                    htmlline += "</h{}>\n".format(heading_level)
                    html.write(htmlline)

            if ul_list_start is True:
                html.write("</ul>\n")

            if ol_list_start is True:
                html.write("</ol>\n")
    exit(0)
