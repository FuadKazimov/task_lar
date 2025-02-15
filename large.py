with open("large_file.txt", "w", encoding="utf-8") as file:
    for i in range(1, 211):
        file.write(f"Bu sətr {i}-dir.\n")
print("Hello world")
def split_file(input_file, output_prefix, line_size):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines() 

    total_lines = len(lines)  
    file_count = (total_lines // line_size) + (1 if total_lines % line_size else 0)  # Neçə fayl olacaq

    for i in range(file_count):
        start = i * line_size 
        end = start + line_size  
        chunk = lines[start:end] 

        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, "w", encoding="utf-8") as out_f:
            out_f.writelines(chunk) 

        print(f"{output_file} yaradıldı: {start}-{end if end < total_lines else total_lines} sətr")


split_file("large_file.txt", "prefix", 100)