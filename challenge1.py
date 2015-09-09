__author__ = 'dlohani'
# Challenge 1 : as image shows
# K -> M    O -> Q  E -> G
# we know its related to text translation
# http://www.pythonchallenge.com/pc/def/map.html

from string import maketrans

##
# translates the given string by making the translation
# @param str string to translate
def translateString(str):
    # function maketrans() is used to define the required translation
    trantab = maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
    return str.translate(trantab)

print(
    translateString("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))

# output :  i hope you didnt translate it by hand.
# thats what computers are for. doing it in by hand is inefficient and that's why
# this text is so long. using string.maketrans() is recommended. now apply on the url.

# applying translation in the url
print(translateString("map"))

# output: ocr, so the next challenge link is http://www.pythonchallenge.com/pc/def/ocr.html