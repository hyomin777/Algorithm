def validate_pin(pin):
    if len(pin) != 4 or len(pin) != 6:
        return False
    for char in pin:
        if not char.isdigit():
            return False
    return True