# Instead of: value = my_dict[key]
value = my_dict.get(key, default_value)

# Or check first:
if key in my_dict:
    value = my_dict[key]