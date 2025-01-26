"""
This module provides functions for loading and processing emoji mappings and
translating text files based on the mappings.
"""
def load_emoji_mapping(emoji_file_name: str) -> dict:
    """
    Loads an emoji mapping from a specified file.

    Args:
        emoji_file_name (str): The filename of the emoji mapping file.

    Returns:
        dict: A dictionary with English words as keys and dictionaries of
              emoji representations as values.
    """
    emoji_dict = {}
    try:
        with open(emoji_file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            metadata = lines[0].split()
            english_col = metadata.index("ENGLISH")
            western_col = metadata.index("WESTERN")
            kaomoji_col = metadata.index("KAOMOJI")

            for line in lines[1:]:
                parts = line.split()
                english_word = parts[english_col - 1]
                western_emoji = parts[western_col - 1]
                kaomoji_emoji = parts[kaomoji_col - 1]
                emoji_dict[english_word.lower()] = {
                    "western": western_emoji,
                    "kaomoji": kaomoji_emoji
                }
    except FileNotFoundError:
        print(f"Error: Expression mapping file does not exist")
    print(emoji_dict)
    return emoji_dict

def process_translation(input_file: str, output_file: str, emoji_dict: dict, 
                        from_lang: str, to_lang: str):
    """
    Processes a text file and translates words based on the emoji dictionary.

    Args:
        input_file (str): The name of the input file to process.
        output_file (str): The name of the output file to save processed text.
        emoji_dict (dict): Dictionary with emoji mappings.
        from_lang (str): Source language (e.g., 'english').
        to_lang (str): Target language (e.g., 'kaomoji', 'western').
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # Process each line of text
                words = line.strip().split(' ')
                # Loop through each word in the line
                for i in range(len(words)):
                    word = words[i]
                    # Convert from English to Western or Kaomoji emoji
                    if from_lang == "english" and to_lang == "western":
                        if word.lower() in emoji_dict:
                            words[i] = emoji_dict[word.lower()]["western"]
                    elif from_lang == "english" and to_lang == "kaomoji":
                        if word.lower() in emoji_dict:
                            words[i] = emoji_dict[word.lower()]["kaomoji"]
                    # Convert from Kaomoji or Western emoji to English
                    elif from_lang == "kaomoji" and to_lang == "english":
                        for k, v in emoji_dict.items():
                            if v["kaomoji"] == word:
                                words[i] = k
                    elif from_lang == "western" and to_lang == "english":
                        for k, v in emoji_dict.items():
                            if v["western"] == word:
                                words[i] = k   
                
                processed_line = ' '.join(words)
                outfile.write(processed_line + '\n')
            print(f"{input_file} processed and {output_file} generated")
    except FileNotFoundError:
        print(f"Error: File {input_file} does not exist")

def batch_translate(emoji_file_name: str, directives_file_name: str):
    """
    Reads a directive file and processes multiple translation commands.

    Args:
        emoji_file_name (str): The filename of the emoji mapping file.
        directives_file_name (str): The filename of the directives file.
    """
    emoji_dict = load_emoji_mapping(emoji_file_name)

    try:
        with open(directives_file_name, 'r') as f:
            for line in f:
                directive = line.strip().split()
                from_lang, to_lang, input_file, output_file = directive
                from_lang = from_lang.lower()
                to_lang = to_lang.lower()

                try:
                    process_translation(input_file, output_file, emoji_dict, 
                                        from_lang, to_lang)
                except FileNotFoundError:
                    print(f"Error: File does not exist. Skipping command.")
                    continue
    except FileNotFoundError:
        print(f"Error: Directive file does not exist")
