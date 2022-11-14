def gender(ID):

    numbers_for_gender = int(ID[2:4])
    if numbers_for_gender > 50:
        return "žena"
    else:
        return "muž"
