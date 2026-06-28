import re

def parse_dataset(dataset_path):
    """
    Parses dataset.txt to build a mapping from block indices to Hindi translation lines.
    Using 'utf-8-sig' to strip any hidden BOM characters.
    """
    translations = {}
    with open(dataset_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Split dataset entries by double newlines or looking for the index pattern
    blocks = re.split(r'\n\s*\n', content.strip())
    
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if len(lines) >= 3:
            index_str = lines[0]
            # The last line in the block is typically the Hindi translation
            hindi_translation = lines[-1] 
            
            # Ensure the index is purely numeric
            if index_str.isdigit():
                translations[int(index_str)] = hindi_translation
                
    return translations

def translate_srt(srt_path, output_path, translations):
    """
    Reads the original SRT file and replaces English text with Hindi text from translations dictionary.
    Using 'utf-8-sig' to read properly from the exact file start.
    """
    with open(srt_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # SRT blocks are usually separated by blank lines
    blocks = content.strip().split('\n\n')
    translated_blocks = []

    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            index_str = lines[0].strip()
            timestamp = lines[1].strip()
            
            if index_str.isdigit():
                srt_index = int(index_str)
                # Find translation if it exists, otherwise fall back to original text joining remaining lines
                if srt_index in translations:
                    translated_text = translations[srt_index]
                else:
                    translated_text = '\n'.join(lines[2:])
                
                # Reconstruct the SRT block
                new_block = f"{index_str}\n{timestamp}\n{translated_text}"
                translated_blocks.append(new_block)
            else:
                translated_blocks.append(block)
        else:
            translated_blocks.append(block)

    # Write the new SRT file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(translated_blocks) + '\n')

if __name__ == "__main__":
    dataset_file = "dataset.txt"
    input_srt = "file1.srt"
    output_srt = "translated_file1.srt"
    
    print("Parsing translation dataset...")
    translations_map = parse_dataset(dataset_file)
    print(f"Loaded {len(translations_map)} translations.")
    
    print("Translating SRT file...")
    translate_srt(input_srt, output_srt, translations_map)
    print(f"Success! Translated subtitle saved as '{output_srt}'.")