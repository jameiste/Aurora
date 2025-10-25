# Check whether the score is high enough
import pandas as pd

# Local imports
from functions.geo_func import get_data

# Function: Decide whether the score is high enough
def score_validation():
    
    # Get the data
    data, all_data = get_data()
    average_score = sum(data.score) / len(data.score)
    print(f"Currently, we have an averages score of: \n {average_score}")
    
    if average_score >= 3:
        return True, data
    else:
        return False, data
    