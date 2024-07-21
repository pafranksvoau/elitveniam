class MyClass:
    def __init__(self, value_accessor, cmp_value):
        self.value_accessor = value_accessor  # Initializing an attribute with the value of 'value_accessor'
        self.cmp_value = cmp_value            # Initializing another attribute with the value of 'cmp_value'

# Creating an instance of MyClass
obj = MyClass('some_value', 10)

# Accessing the initialized attributes
print(obj.value_accessor)  # Output: 'some_value'
print(obj.cmp_value)        # Output: 10
