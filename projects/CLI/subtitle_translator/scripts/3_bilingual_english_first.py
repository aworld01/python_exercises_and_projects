import re

def parse_dataset(dataset_path):
    """
    Parses dataset.txt to build a mapping from block indices to Hindi translation lines.
    Using 'utf-8-sig' to strip any hidden BOM characters.
    """
    translations = {}
    with open(dataset_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Split dataset entries by double newlines
    blocks = re.split(r'\n\s*\n', content.strip())
    
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if len(lines) >= 3:
            index_str = lines[0]
            # The last line in the block is the Hindi translation
            hindi_translation = lines[-1] 
            
            # Ensure the index is purely numeric
            if index_str.isdigit():
                translations[int(index_str)] = hindi_translation
                
    return translations

def translate_srt(srt_path, output_path, translations):
    """
    Reads original SRT and creates an output with both English and Hindi text combined.
    The English line appears first, followed by the Hindi line.
    """
    with open(srt_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Normalize line endings and split by empty lines to isolate subtitle blocks
    content = content.replace('\r\n', '\n')
    blocks = content.strip().split('\n\n')
    translated_blocks = []

    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            index_str = lines[0].strip()
            timestamp = lines[1].strip()
            # Combine all remaining lines to capture the full original English subtitle text
            english_text = '\n'.join(lines[2:])
            
            if index_str.isdigit():
                srt_index = int(index_str)
                
                if srt_index in translations:
                    hindi_text = translations[srt_index]
                    # COMBINE BOTH LINES HERE: English on top, Hindi on bottom
                    combined_text = f"{english_text}\n{hindi_text}"
                else:
                    combined_text = english_text
                
                # Reconstruct the SRT block
                new_block = f"{index_str}\n{timestamp}\n{combined_text}"
                translated_blocks.append(new_block)
            else:
                translated_blocks.append(block)
        else:
            translated_blocks.append(block)

    # Write the new bilingual SRT file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(translated_blocks) + '\n')

if __name__ == "__main__":
    dataset_file = "dataset.txt"
    input_srt = "file1.srt"
    output_srt = "bilingual_english_first.srt"
    
    print("Parsing translation dataset...")
    translations_map = parse_dataset(dataset_file)
    print(f"Loaded {len(translations_map)} translations.")
    
    print("Generating bilingual SRT file (English first)...")
    translate_srt(input_srt, output_srt, translations_map)
    print(f"Success! Subtitle saved as '{output_srt}'.")