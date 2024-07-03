from crops.crops import MinecraftCrop

# return the enum of the user's input. clean up input too
def convertUserInput(user_input): 
    
    user_input = user_input.lower().replace(" ", "")

    for crop in MinecraftCrop:
        enum_value = crop.value.lower().replace(" ", "")
        if user_input == enum_value:
            return crop

    # Return NONE if no match found
    return MinecraftCrop.NONE


