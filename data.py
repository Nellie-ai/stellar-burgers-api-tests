USER_NAME = "Test User"

REQUIRED_USER_FIELDS = ("email", "password", "name")

VALID_INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6f",
]
INVALID_INGREDIENT_HASH = "000000000000000000000001"

USER_ALREADY_EXISTS_RESPONSE = {
    "success": False,
    "message": "User already exists",
}
REQUIRED_FIELDS_RESPONSE = {
    "success": False,
    "message": "Email, password and name are required fields",
}
INVALID_CREDENTIALS_RESPONSE = {
    "success": False,
    "message": "email or password are incorrect",
}
INGREDIENTS_REQUIRED_RESPONSE = {
    "success": False,
    "message": "Ingredient ids must be provided",
}
