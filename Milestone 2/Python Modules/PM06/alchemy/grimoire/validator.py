def validate_ingredients(ingredients: str) -> str:
    valid: bool = False
    ingredient_list: list[str] = ingredients.split()
    valid_list: list[str] = ["fire", "water", "earth", "air"]
    for ingredient in ingredient_list:
        for item in valid_list:
            if item == ingredient:
                valid = True
                break
            else:
                valid = False
        if valid is False:
            break
    if valid is True:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
