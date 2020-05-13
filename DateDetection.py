#! python3 
# dateDetection.py - validates date. 
 
import pyperclip, re 
 
# Set regex. 
dateRegex = re.compile(r'''( 
    (\d{2})                     # day 
    (/|-|.)?                    # separator 
    (\d{2})                     # month 
    (/|-|.)?                    # separator 
    (\d{4})                     # year 
    )''', re.VERBOSE)