# max heart rate: 220-age
# target heart rate: 50-85% of max heart rate

age = int(input( "how old are you?:"))
max_heart_rate = 220 - age

target_heart_rate_upper = (85 * max_heart_rate)/100
target_heart_rate_lower = (50 * max_heart_rate)/100

print(f"max_heart_rate = {max_heart_rate}")
print(f"target_heart_rate_lower = {max_heart_rate}")
