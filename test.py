output_data = []

# Create a dictionary to hold the sum of values for each combination of gslb_name and gslb_service
sum_dict = {}

for item in input_data:
    gslb_name = item['gslb_name']
    gslb_service = item['gslb_service']
    value = item['value']
    
    # Check if the gslb_service contains "m3" or "m4"
    if "m3" in gslb_service or "m4" in gslb_service:
        # Create a key that combines the gslb_name and the "m3/m4" suffix
        new_key = f"{gslb_name}.*.m3/m4-443"
    elif "m5" in gslb_service:
        # Create a key that combines the gslb_name and the "m5" suffix
        new_key = f"{gslb_name}.*.m5-443"
    elif "m7" in gslb_service:
         # Create a key that combines the gslb_name and the "m5" suffix
        new_key = f"{gslb_name}.*.m7-443"
    else:
        new_key = "None"
    
    # Add the value to the sum_dict using the new_key
    if new_key in sum_dict:
        sum_dict[new_key] += value
    else:
        sum_dict[new_key] = value
        
# Convert the sum_dict to the desired output format
for key, value in sum_dict.items():
    gslb_name, gslb_service = key.split(".*.")
    output_data.append({'gslb_name': gslb_name, 'gslb_service': gslb_service, 'sum_value': value})
    
print(output_data)
