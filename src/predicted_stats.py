import numpy as np



def calculate_statistics(predictions, true_values, insolubility_threshold=-6, solubility_threshold=-4):
    '''
    This function calculates percentage of the correctly and incorrectly predicted statistics based on predicted and true solubility arrays.

    Arguments:
    predictions -- Numpy array containing predicted solubility values.
    true_values -- Numpy array containing true solubility values.
    insolubility_threshold -- Threshold for insolubility which is -6.
    solubility_threshold -- Threshold for solubility which is -4.

    Returns:
    hit_percentage -- Percentage of correctly predicted solubilities within the solubility threshold range.
    Miss% -- Percentage of incorrectly predicted solubilities within the solubility threshold range.
    num_true -- Total number of true examples within the solubility threshold range.
    num_predicted -- Total number of predicted examples within the solubility threshold range.
    '''

    # Calculate true mask
    true_mask = (true_values > solubility_threshold)
    
    # Calculate Hit%
    num_true = np.sum(true_mask)
    possible_hits = predictions[true_mask]
    num_hits = np.sum((possible_hits > solubility_threshold))
    hit_percentage = num_hits / float(num_true) if num_true != 0 else 0
    
    # Calculate predicted mask
    predicted_mask = (predictions > solubility_threshold)
    
    # Calculate insolubility mask
    insolubility_mask = true_values <= insolubility_threshold
    
    # Calculate Miss%
    num_predicted = np.sum(predicted_mask)
    num_failures = np.sum(insolubility_mask & predicted_mask)
    miss_percentage = num_failures / float(num_predicted) if num_predicted != 0 else 0
    
    return hit_percentage, miss_percentage, num_true, num_predicted



