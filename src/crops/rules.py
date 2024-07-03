#rules for each plant... ie.. sugar cane needs to be adjacent to water, etc

from crops.crops import MinecraftCrop

#crop
def isConstraintSatisfied(crop, land, current_x, current_y):
    """
    return whether or not the constraint is satisfied
    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.

    Returns:
        bool: Description of the return value.
    """
    # Function implementation goes here
    if(crop == MinecraftCrop.WHEAT):
        return False
    elif(crop == MinecraftCrop.SUGAR_CANE):
        #check adjacent PAST squares (left to right, top to bottom) to see if placing this block will nullify current position
        # if
        # 
        #
        #if you're on the left most side...
        isLeftMost = False
        isRightMost = False
        isTop = False
        isBottom = False
        rows = len(land)
        cols = len(land[0])
        if(current_x - 1 >= 0):
           isTop = True
        if(current_x -  len(land) <= 0):
            isBottom = True
        if(current_y - 1 <= 0):
            isLeftMost = True
        if(current_y - len(land[0]) >= 0):
            isRightMost = True
            
        
            
            
        return True