# From Python 3-04.xml
import re
re.sub("1", "\\n", "123123123123") # replace digit one with newline
'\n23\n23\n23\n23'
re.sub("1", r"\n", "123123123123") # replace digit one with newline
def dashrepl(matchobj):
    if matchobj.group(0) == "-": return " "
    else: return "+"

re.sub('-{1,2}', dashrepl, 'pro----gram-files')

s = "(123) 456-7890 # Commented phone number"
nocomment = re.sub("#.*$", "", s)
nocomment
re.sub(r"\D", "", nocomment)
re.sub("@(=\+=)*@", "xxx", "@@")
re.sub("@(=\+=)*@", "xxx", "@=+=@")
re.sub("@(=\+=)*@", "xxx", "@=+==+=@")
re.sub("@(=\+=)*@", "xxx", "@=+=+=@")
re.sub("[aeiouAEIOU]", "-", "The Quick Brown Fox Jumps Over the Lazy Dog")
