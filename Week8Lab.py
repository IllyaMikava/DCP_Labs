import string
from collections import defaultdict

# ============================================
# TASK 1: WORD FREQUENCY ANALYSIS
# ============================================

def clean_word(word):
    """
    Converts words to lowercase and removes punctuation
    Returns the cleaned word
    """
    # Remove punctuation
    word = word.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    word = word.lower()
    return word


def load_file(filename):
    """Load the file into a list of strings"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []


def count_word_frequencies(lines, exclude_stop_words=False):
    """Count word frequencies in the script"""
    word_counts = {}
    
    # Stop words for bonus task
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 
                  'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were',
                  'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
                  'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can',
                  'it', 'its', 'this', 'that', 'these', 'those', 'i', 'you', 'he',
                  'she', 'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why',
                  'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other',
                  'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                  'than', 'too', 'very', 'as', 'his', 'her', 'my', 'your'}
    
    for line in lines:
        words = line.split()
        for word in words:
            cleaned = clean_word(word)
            if cleaned:  # Skip empty strings
                if exclude_stop_words and cleaned in stop_words:
                    continue
                word_counts[cleaned] = word_counts.get(cleaned, 0) + 1
    
    return word_counts


def print_top_words(word_counts, n=10):
    """Find and print the top N most common words"""
    print(f"\n=== WORD FREQUENCY ANALYSIS ===")
    print(f"Total unique words: {len(word_counts)}")
    print(f"\nTop {n} most common words:")
    
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]
    
    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i}. {word}: {count} occurrences")


# ============================================
# TASK 2: CHARACTER ANALYSIS
# ============================================

def extract_characters(lines):
    """
    Extract character names from screenplay format
    Character names appear in ALL CAPS before dialogue
    """
    characters = set()
    
    # Common scene headings and words to exclude
    exclude_words = {
        'EXT', 'INT', 'CONTINUED', 'CONTD', 'DAY', 'NIGHT', 'MORNING', 
        'EVENING', 'LATER', 'FADE', 'CUT', 'DISSOLVE', 'TO', 'IN', 'OUT',
        'BLACK', 'BACK', 'THE', 'END', 'TITLE', 'CREDITS', 'SEQUENCE'
    }
    
    for line in lines:
        stripped = line.strip()
        
        # Check if line is all uppercase and not empty
        if stripped and stripped.isupper():
            # Remove parentheticals like (CONT'D) or (V.O.)
            stripped = stripped.split('(')[0].strip()
            
            # Check if it's not a scene heading
            words = stripped.split()
            if words and words[0] not in exclude_words:
                # It's likely a character name
                if len(stripped) < 50:  # Character names shouldn't be too long
                    characters.add(stripped)
    
    return sorted(list(characters))


def count_character_lines(lines):
    """Count how many times each character speaks"""
    character_lines = defaultdict(int)
    current_character = None
    
    exclude_words = {
        'EXT', 'INT', 'CONTINUED', 'CONTD', 'DAY', 'NIGHT', 'MORNING', 
        'EVENING', 'LATER', 'FADE', 'CUT', 'DISSOLVE', 'TO', 'IN', 'OUT',
        'BLACK', 'BACK', 'THE', 'END', 'TITLE', 'CREDITS', 'SEQUENCE'
    }
    
    for line in lines:
        stripped = line.strip()
        
        # Check if this is a character name
        if stripped and stripped.isupper():
            stripped = stripped.split('(')[0].strip()
            words = stripped.split()
            
            if words and words[0] not in exclude_words and len(stripped) < 50:
                current_character = stripped
                character_lines[current_character] += 1
    
    return dict(character_lines)


def print_character_report(character_lines):
    """Print formatted character report"""
    print(f"\n=== CHARACTER ANALYSIS ===")
    print(f"Total characters: {len(character_lines)}")
    print("\nCharacter speaking lines:")
    
    # Sort by number of lines (descending)
    sorted_characters = sorted(character_lines.items(), key=lambda x: x[1], reverse=True)
    
    for character, lines in sorted_characters:
        print(f"  {character}: {lines} lines")
    
    if sorted_characters:
        most_dialogue = sorted_characters[0]
        print(f"\nCharacter with most dialogue: {most_dialogue[0]} ({most_dialogue[1]} lines)")


# ============================================
# TASK 3: DIALOGUE ANALYSIS
# ============================================

def analyze_dialogue_length(lines):
    """Calculate total words and average words per line for each character"""
    character_dialogue = defaultdict(list)
    current_character = None
    
    exclude_words = {
        'EXT', 'INT', 'CONTINUED', 'CONTD', 'DAY', 'NIGHT', 'MORNING', 
        'EVENING', 'LATER', 'FADE', 'CUT', 'DISSOLVE', 'TO', 'IN', 'OUT',
        'BLACK', 'BACK', 'THE', 'END', 'TITLE', 'CREDITS', 'SEQUENCE'
    }
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if this is a character name
        if stripped and stripped.isupper():
            stripped = stripped.split('(')[0].strip()
            words = stripped.split()
            
            if words and words[0] not in exclude_words and len(stripped) < 50:
                current_character = stripped
        # If we have a current character and this is dialogue
        elif current_character and stripped and not stripped.isupper():
            # Count words in this line of dialogue
            word_count = len(stripped.split())
            character_dialogue[current_character].append(word_count)
    
    # Calculate statistics
    dialogue_stats = {}
    for character, word_counts in character_dialogue.items():
        total_words = sum(word_counts)
        num_lines = len(word_counts)
        avg_words = total_words / num_lines if num_lines > 0 else 0
        
        dialogue_stats[character] = {
            'total_words': total_words,
            'num_lines': num_lines,
            'avg_words_per_line': avg_words
        }
    
    return dialogue_stats


def analyze_character_words(lines):
    """Create nested dictionary of words used by each character"""
    character_words = defaultdict(lambda: defaultdict(int))
    current_character = None
    
    exclude_words = {
        'EXT', 'INT', 'CONTINUED', 'CONTD', 'DAY', 'NIGHT', 'MORNING', 
        'EVENING', 'LATER', 'FADE', 'CUT', 'DISSOLVE', 'TO', 'IN', 'OUT',
        'BLACK', 'BACK', 'THE', 'END', 'TITLE', 'CREDITS', 'SEQUENCE'
    }
    
    for line in lines:
        stripped = line.strip()
        
        # Check if this is a character name
        if stripped and stripped.isupper():
            stripped = stripped.split('(')[0].strip()
            words = stripped.split()
            
            if words and words[0] not in exclude_words and len(stripped) < 50:
                current_character = stripped
        # If we have a current character and this is dialogue
        elif current_character and stripped and not stripped.isupper():
            words = stripped.split()
            for word in words:
                cleaned = clean_word(word)
                if cleaned:
                    character_words[current_character][cleaned] += 1
    
    return dict(character_words)


def print_dialogue_analysis(dialogue_stats, character_words):
    """Print dialogue length analysis"""
    print(f"\n=== DIALOGUE LENGTH ANALYSIS ===")
    
    sorted_stats = sorted(dialogue_stats.items(), 
                         key=lambda x: x[1]['total_words'], 
                         reverse=True)
    
    for character, stats in sorted_stats:
        print(f"\n{character}:")
        print(f"  Total words spoken: {stats['total_words']}")
        print(f"  Number of lines: {stats['num_lines']}")
        print(f"  Average words per line: {stats['avg_words_per_line']:.2f}")
        
        # Show top 5 words for this character
        if character in character_words:
            top_words = sorted(character_words[character].items(), 
                             key=lambda x: x[1], 
                             reverse=True)[:5]
            print(f"  Top 5 words: {', '.join([f'{word}({count})' for word, count in top_words])}")


# ============================================
# BONUS TASKS
# ============================================

def calculate_dialogue_vs_action(lines):
    """Calculate percentage of dialogue vs action descriptions"""
    dialogue_lines = 0
    action_lines = 0
    current_is_character = False
    
    exclude_words = {
        'EXT', 'INT', 'CONTINUED', 'CONTD', 'DAY', 'NIGHT', 'MORNING', 
        'EVENING', 'LATER', 'FADE', 'CUT', 'DISSOLVE', 'TO', 'IN', 'OUT',
        'BLACK', 'BACK', 'THE', 'END', 'TITLE', 'CREDITS', 'SEQUENCE'
    }
    
    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            current_is_character = False
            continue
        
        # Character name
        if stripped and stripped.isupper():
            stripped_clean = stripped.split('(')[0].strip()
            words = stripped_clean.split()
            
            if words and words[0] not in exclude_words and len(stripped_clean) < 50:
                current_is_character = True
            else:
                current_is_character = False
                action_lines += 1
        # Dialogue or action
        elif not stripped.isupper():
            if current_is_character:
                dialogue_lines += 1
            else:
                action_lines += 1
    
    total_lines = dialogue_lines + action_lines
    if total_lines > 0:
        dialogue_pct = (dialogue_lines / total_lines) * 100
        action_pct = (action_lines / total_lines) * 100
    else:
        dialogue_pct = action_pct = 0
    
    return dialogue_lines, action_lines, dialogue_pct, action_pct


def analyze_scene_breakdown(lines):
    """Count total scenes, EXT and INT scenes"""
    total_scenes = 0
    ext_scenes = 0
    int_scenes = 0
    
    for line in lines:
        stripped = line.strip().upper()
        if stripped.startswith('EXT.') or stripped.startswith('EXT '):
            ext_scenes += 1
            total_scenes += 1
        elif stripped.startswith('INT.') or stripped.startswith('INT '):
            int_scenes += 1
            total_scenes += 1
    
    return total_scenes, ext_scenes, int_scenes


# ============================================
# MAIN EXECUTION
# ============================================

def main(save_to_file=True):
    """
    Main analysis function
    If save_to_file=True, saves output to analysis_report.txt
    """
    # Redirect output to file if requested
    if save_to_file:
        import sys
        original_stdout = sys.stdout
        report_file = open('analysis_report.txt', 'w', encoding='utf-8')
        sys.stdout = report_file
    
    # Print header FIRST before anything else
    print("=" * 60)
    print("ACE VENTURA: PET DETECTIVE - SCREENPLAY ANALYSIS")
    print("=" * 60)
    
    # Load the file
    filename = 'Data/aceventura.txt'
    print(f"\nAttempting to load {filename}...")
    lines = load_file(filename)
    
    if not lines:
        print("\nNo data to analyze. Please ensure aceventura.txt is in the same directory.")
        return
    
    print(f"Successfully loaded {len(lines)} lines from the file!\n")
    
    # Task 1: Word Frequency Analysis
    print("\n[Processing word frequencies...]")
    word_counts = count_word_frequencies(lines)
    print(f"[Found {len(word_counts)} unique words]")
    print_top_words(word_counts, 10)
    
    # Task 1 Bonus: Without stop words
    print("\n[Processing word frequencies without stop words...]")
    word_counts_no_stop = count_word_frequencies(lines, exclude_stop_words=True)
    print(f"\n--- Without Stop Words ---")
    print(f"Total unique words (excluding stop words): {len(word_counts_no_stop)}")
    top_words_no_stop = sorted(word_counts_no_stop.items(), 
                               key=lambda x: x[1], 
                               reverse=True)[:10]
    for i, (word, count) in enumerate(top_words_no_stop, 1):
        print(f"{i}. {word}: {count} occurrences")
    
    # Task 2: Character Analysis
    characters = extract_characters(lines)
    character_lines = count_character_lines(lines)
    print_character_report(character_lines)
    
    # Task 3: Dialogue Analysis
    dialogue_stats = analyze_dialogue_length(lines)
    character_words = analyze_character_words(lines)
    print_dialogue_analysis(dialogue_stats, character_words)
    
    # Bonus: Dialogue vs Action
    d_lines, a_lines, d_pct, a_pct = calculate_dialogue_vs_action(lines)
    print(f"\n=== DIALOGUE VS ACTION ===")
    print(f"Dialogue lines: {d_lines} ({d_pct:.1f}%)")
    print(f"Action lines: {a_lines} ({a_pct:.1f}%)")
    
    # Scene Breakdown
    total_scenes, ext_scenes, int_scenes = analyze_scene_breakdown(lines)
    print(f"\n=== SCENE BREAKDOWN ===")
    print(f"Total scenes: {total_scenes}")
    print(f"EXT scenes: {ext_scenes}")
    print(f"INT scenes: {int_scenes}")
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    
    # Restore stdout and close file if we redirected
    if save_to_file:
        sys.stdout = original_stdout
        report_file.close()
        print("\n✓ Analysis complete! Results saved to 'analysis_report.txt'")
        print("  Open analysis_report.txt to see the full report.")


if __name__ == "__main__":
    # Set to True to save to file, False to print to console
    main(save_to_file=True)