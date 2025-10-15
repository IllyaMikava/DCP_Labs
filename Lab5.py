import pandas as pd

# Part 2: Read file
def load_abc_file(file):
    """Load ABC file into list of lines"""
    try:
        
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file, 'r', encoding='latin-1') as f:
            lines = f.readlines()
    return lines

# Part 3: Parse tunes
def parse_tune(tune_lines):
    """Parse a single tune from lines"""
    tune = {
        'X': None,
        'title': None,
        'alt_title': None,
        'tune_type': None,
        'key': None,
        'notation': '\n'.join(tune_lines)
    }
    
    title_count = 0
    
    for line in tune_lines:
        line = line.strip()
        
        # Parse X: (tune ID)
        if line.startswith('X:'):
            tune['X'] = line[2:].strip()
        
        # Parse T: (title)
        elif line.startswith('T:'):
            title_count += 1
            if title_count == 1:
                tune['title'] = line[2:].strip()
            elif title_count == 2:
                tune['alt_title'] = line[2:].strip()
        
        # Parse R: (tune type)
        elif line.startswith('R:'):
            tune['tune_type'] = line[2:].strip()
        
        # Parse K: (key)
        elif line.startswith('K:'):
            tune['key'] = line[2:].strip()
    
    return tune

def parse_all_tunes(lines):
    """Parse all tunes from lines"""
    tunes = []
    current_tune_lines = []
    in_tune = False
    
    for i, line in enumerate(lines):
        # Check if this starts a new tune
        if line.strip().startswith('X:'):
            # If we were already collecting a tune, save it first
            if current_tune_lines:
                tunes.append(parse_tune(current_tune_lines))
            
            # Start collecting new tune
            current_tune_lines = [line]
            in_tune = True
        
        elif in_tune:
            # Check if this is a blank line (end of tune)
            if line.strip() == '' or line.strip() == '%%%':
                # Found end of tune
                tunes.append(parse_tune(current_tune_lines))
                current_tune_lines = []
                in_tune = False
            else:
                # Still in tune, add line
                current_tune_lines.append(line)
    
   
    if current_tune_lines:
        tunes.append(parse_tune(current_tune_lines))
    
    return tunes

# Main 
if __name__ == "__main__":
    # Part 2: Load file
    print("=== PART 2: LOADING FILE ===")
    lines = load_abc_file('oneills.abc')
    print(f"Loaded {len(lines)} lines")
    print("\nFirst 20 lines:")
    for i, line in enumerate(lines[:20]):
        print(f"{i:3}: {line.rstrip()}")
    
    print("\nLast 10 lines:")
    for i, line in enumerate(lines[-10:], len(lines)-10):
        print(f"{i:3}: {line.rstrip()}")
    
    # Part 3: Parse tunes
    print("\n\n=== PART 3: PARSING TUNES ===")
    tunes = parse_all_tunes(lines)
    print(f"Parsed {len(tunes)} tunes")
    
    print("\nFirst tune:")
    for key, value in tunes[0].items():
        if key != 'notation':
            print(f"  {key}: {value}")
    
    print("\nLast tune:")
    for key, value in tunes[-1].items():
        if key != 'notation':
            print(f"  {key}: {value}")
    
    # Part 4: Create DataFrame
    print("\n\n=== PART 4: CREATE DATAFRAME ===")
    df = pd.DataFrame(tunes)
    
    print(f"DataFrame shape: {df.shape}")
    print("\nDataFrame info:")
    print(df.info())
    
    print("\nFirst 5 rows:")
    print(df[['X', 'title', 'tune_type', 'key']].head())
    
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Part 5: Data Analysis
    print("\n\n=== PART 5: DATA ANALYSIS ===")
    
    # Task 5.1: Group by Tune Type
    print("\n--- Tune Type Counts ---")
    tune_type_counts = df['tune_type'].value_counts()
    print(tune_type_counts)
    print(f"\nTotal unique tune types: {df['tune_type'].nunique()}")
    print(f"Most common tune type: {tune_type_counts.index[0]} ({tune_type_counts.iloc[0]} tunes)")
    print(f"Least common tune type: {tune_type_counts.index[-1]} ({tune_type_counts.iloc[-1]} tunes)")
    
    # Task 5.2: Group by Key
    print("\n--- Key Counts ---")
    key_counts = df['key'].value_counts()
    print(key_counts)
    
    # Count major vs minor keys
    major_keys = df[df['key'].str.contains(r'^[A-G](?!m)', regex=True, na=False)]['key'].count()
    minor_keys = df[df['key'].str.contains(r'm(?:aj|in)?', regex=True, na=False)]['key'].count()
    print(f"\nMajor keys: {major_keys}")
    print(f"Minor keys: {minor_keys}")
    print(f"Most popular key: {key_counts.index[0]} ({key_counts.iloc[0]} tunes)")
    
    # Task 5.3: Find Alcoholic Drinks in Titles
    print("\n--- Alcoholic Drinks in Titles ---")
    
    # Create search pattern for drinks
    drinks = ['whiskey', 'whisky', 'beer', 'ale', 'wine', 'brandy', 'punch', 'porter', 'rum', 'gin']
    drinks_pattern = '|'.join(drinks)
    
    # Find tunes with drinks in title
    drinks_mask = df['title'].str.contains(drinks_pattern, case=False, na=False)
    drinks_tunes = df[drinks_mask]
    
    print(f"Found {len(drinks_tunes)} tunes mentioning alcoholic drinks")
    
    # Count which drinks appear most often
    drink_counts = {}
    for drink in drinks:
        count = df['title'].str.contains(drink, case=False, na=False).sum()
        if count > 0:
            drink_counts[drink] = count
    
    if drink_counts:
        sorted_drinks = sorted(drink_counts.items(), key=lambda x: x[1], reverse=True)
        print("\nDrink mentions:")
        for drink, count in sorted_drinks:
            print(f"  {drink}: {count}")
        print(f"\nMost mentioned drink: {sorted_drinks[0][0]} ({sorted_drinks[0][1]} times)")
    
    print("\nTune titles mentioning drinks:")
    for idx, row in drinks_tunes.iterrows():
        print(f"  - {row['title']} ({row['tune_type']}, Key: {row['key']})")
    
    # Part 6: Export Results
    print("\n\n=== PART 6: EXPORT RESULTS ===")
    df.to_csv('parsed_tunes.csv', index=False)
    print("Saved DataFrame to 'parsed_tunes.csv'")
    
    # Bonus: Create a summary report
    print("\n\n=== SUMMARY REPORT ===")
    print(f"Total tunes parsed: {len(df)}")
    print(f"Tunes with alternate titles: {df['alt_title'].notna().sum()}")
    print(f"Most common tune type: {tune_type_counts.index[0]}")
    print(f"Most common key: {key_counts.index[0]}")
    print(f"Percentage of tunes mentioning alcohol: {len(drinks_tunes)/len(df)*100:.1f}%")