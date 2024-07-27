def set_threshold_values(min_value, max_value):
    if min_value > 0 or max_value < 0:
        raise ValueError("Threshold values must include zero.")
    
    # Continue with your logic
    print(f"Threshold values set from {min_value} to {max_value}")

try:
    set_threshold_values(-10, 10)  # Valid
    set_threshold_values(1, 5)     # Invalid, will raise an error
except ValueError as e:
    print(e)
