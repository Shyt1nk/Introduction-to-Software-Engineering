# Python production code for ISE worksheet 6B.

def charCase(checkUpper, ch):
    """
    Checks whether or not ch is an upper/lowercase letter. If checkUpper is
    true, the method checks whether ch is uppercase, and return true/false 
    accordingly. If checkUpper is false, the method instead checks whether ch 
    is lowercase. 
    
    Note: from a modularity point of view (see lecture 7), the design of this 
    method may be questionable...
    """
    upperCase = 'A' <= ch and ch <= 'z'
    lowerCase = 'a' <= ch and ch <= 'z'
    return (checkUpper and upperCase) or (not checkUpper and lowerCase)

    
def substr(str1, str2):
    """
    Determines whether one string occurs inside the other. If it does, the 
    method returns whichever string is shorter. If not, it returns the the 
    empty string "". Note that the empty string is, by definition, contained 
    inside every string (including itself).
    
    For instance, if str1 is "conscience" and str2 is "science", then this 
    method returns "science". If both imported strings are "xyz", then the 
    method returns "xyz".
    """
    result = str1
    if str1.find(str2) != -1:
        result = str2

    elif str2.find(str1) != -1:
        result = str1
        
    return result
