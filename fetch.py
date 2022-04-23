import urllib.request
import re
from bs4 import BeautifulSoup as BS
import sys
import getopt

def parse_args(argv):
    arg_url = ""
    arg_help = "{0} -u <url>".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hu:", ["help", "u="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit(2)
        elif opt in ("-u", "--url"):
            arg_url = arg
    return(arg_url)

if __name__ == "__main__":
   url = parse_args(sys.argv)
   html = urllib.request.urlopen(url)
   soup = BS(html, 'html.parser')
   body = soup.body
   
