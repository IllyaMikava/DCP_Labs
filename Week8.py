# Clean word function
def clean_word(word):
    word = word.lower()
    
    # Remove punctuation using string replacement
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in punctuation:
        word = word.replace(char, '')
    
    return word

# Load file
with open('Data/aceventura.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

# Word frequency analysis
word_counts = {}
for line in lines:
    words = line.split()
    for word in words:
        cleaned = clean_word(word)
        if cleaned:
            word_counts[cleaned] = word_counts.get(cleaned, 0) + 1

# Top 10 words
top_10 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Extract characters
def extract_characters(lines):
    characters = []
    scene_indicators = ['EXT', 'INT', 'CONT', 'DAY', 'NIGHT', 'SCENE', 'CUT']
    
    for line in lines:
        if line.isupper() and len(line) > 1:
            if not any(indicator in line for indicator in scene_indicators):
                characters.append(line)
    
    return list(set(characters))

characters = extract_characters(lines)

# Count lines per character
character_lines = {}
for line in lines:
    if line in characters:
        character_lines[line] = character_lines.get(line, 0) + 1

# Dialogue length analysis
dialogue_analysis = {}
current_speaker = None

for line in lines:
    if line in characters:
        current_speaker = line
        if current_speaker not in dialogue_analysis:
            dialogue_analysis[current_speaker] = {'total_words': 0, 'line_count': 0}
    elif current_speaker and line not in characters:
        words = len(line.split())
        dialogue_analysis[current_speaker]['total_words'] += words
        dialogue_analysis[current_speaker]['line_count'] += 1

# Print reports
print("=== WORD FREQUENCY ANALYSIS ===")
print(f"Total unique words: {len(word_counts)}")
print("Top 10 most common words:")
for i, (word, count) in enumerate(top_10, 1):
    print(f"{i}. {word}: {count} occurrences")

print("\n=== CHARACTER ANALYSIS ===")
print(f"Total characters: {len(characters)}")
for char in sorted(character_lines.items(), key=lambda x: x[1], reverse=True):
    print(f"{char[0]}: {char[1]} lines")

most_talkative = max(character_lines.items(), key=lambda x: x[1]) if character_lines else ("None", 0)
print(f"\nMost talkative character: {most_talkative[0]} with {most_talkative[1]} lines")

print("\n=== DIALOGUE LENGTH ANALYSIS ===")
for char, stats in dialogue_analysis.items():
    if stats['line_count'] > 0:
        avg_words = stats['total_words'] / stats['line_count']
        print(f"{char}: {stats['total_words']} total words, {avg_words:.1f} avg per line")