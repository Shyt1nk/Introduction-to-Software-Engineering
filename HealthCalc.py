# Python production code for ISE worksheet 6B.

def uvRating(index):
    """
    Determines a rating for ultraviolet radiation risk, based on a real-valued 
    UV index. Ratings below zero are invalid, in which case the submodule 
    returns "-". Otherwise, if the index is below 3, the rating is "low", then 
    up to 6 for "moderate", up to 8 for "high", and up to 11 for "very high". 
    Any rating over 11 is "extreme".
    """
    if index < 0.0:
        rating = "-"

    elif index <= 3.0:
        rating = "low"

    elif index <= 6.0:
        rating = "medium"

    elif index <= 8.0:
        rating = "high"

    elif index <= 11.0:
        rating = "very high"

    else:
        rating = "extreme"

    return rating
