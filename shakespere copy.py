sonnets = []

with open("Data/shakespere copy.txt", "r", encoding = "utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

current_sonnet = {}
roman_num = None
sonnet_lines = []

for line in lines:
    if line.isupper and all(ch in "IVXLCDM" for ch in line):
        if roman_num and sonnet_lines:
            current_sonnet = {roman_num: sonnet_lines}
            sonnets.append(current_sonnet)
        
        roman_num = line
        sonnet_lines = []

    else:
        sonnet_lines.append(line)

if roman_num and sonnet_lines:
    sonnets.append({roman_num: sonnet_lines})

# Optional: check
print(f"Loaded {len(sonnets)} sonnets.")
print(sonnets[0]) 
for sonnet in sonnets:
    for roman_num, lines in sonnet.items():
        print(f"{roman_num}: {lines[0]}")

