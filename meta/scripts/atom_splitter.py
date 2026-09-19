import os
import re
import sys

def process_notes(input_path, output_dir=None):
    """
    Splits a master Markdown file using the '--atom--' delimiter
    and generates an automated Map of Content (MOC) index file.
    """
    if not os.path.exists(input_path):
        print(f"Error: File not found at '{input_path}'")
        return

    # Determine output directory (defaults to a folder named after the input file)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(input_path), base_name)
    os.makedirs(output_dir, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into atomic chunks
    raw_atoms = content.split("--atom--")
    
    created_notes = []

    for chunk in raw_atoms:
        chunk = chunk.strip()
        if not chunk:
            continue

        # Extract file_name metadata
        file_name_match = re.search(r"^file_name:\s*(.+)$", chunk, re.MULTILINE)
        if not file_name_match:
            continue

        raw_filename = file_name_match.group(1).strip()
        # Clean filename: allow alphanumeric characters, spaces, and hyphens
        sanitized_filename = re.sub(r"[^\w\s\-]", "", raw_filename).strip()
        if not sanitized_filename:
            sanitized_filename = "Untitled_Atom"

        # Extract title (optional, falls back to filename)
        title_match = re.search(r"^title:\s*(.+)$", chunk, re.MULTILINE)
        display_title = title_match.group(1).strip() if title_match else sanitized_filename

        # Extract type (concept, formula, problem, etc.)
        type_match = re.search(r"^type:\s*(.+)$", chunk, re.MULTILINE)
        note_type = type_match.group(1).strip() if type_match else "concept"

        # Remove the top-level atom metadata header lines so the note starts clean
        clean_chunk = re.sub(r"^(file_name|title|type|tags):[^\n]*\n?", "", chunk, flags=re.MULTILINE).strip()

        # Write the individual atomic markdown file
        note_filename = f"{sanitized_filename}.md"
        note_path = os.path.join(output_dir, note_filename)

        with open(note_path, "w", encoding="utf-8") as out_f:
            out_f.write(clean_chunk + "\n")

        created_notes.append({
            "filename": sanitized_filename,
            "title": display_title,
            "type": note_type
        })
        print(f"Created: {note_filename}")

    # Generate the MOC (Index file)
    moc_filename = f"00_MOC - {base_name}.md"
    moc_path = os.path.join(output_dir, moc_filename)

    with open(moc_path, "w", encoding="utf-8") as moc_f:
        moc_f.write(f"---\n")
        moc_f.write(f"type: moc\n")
        moc_f.write(f"topic: {base_name}\n")
        moc_f.write(f"---\n\n")
        moc_f.write(f"# {base_name} — Map of Content\n\n")
        
        # Group links by type if available, or list them cleanly
        grouped = {}
        for note in created_notes:
            grouped.setdefault(note["type"].capitalize(), []).append(note)

        for category, notes in grouped.items():
            moc_f.write(f"## 📌 {category}\n")
            for n in notes:
                moc_f.write(f"- [[{n['filename']}|{n['title']}]]\n")
            moc_f.write("\n")

    print(f"\nSuccessfully created {len(created_notes)} atomic notes.")
    print(f"MOC file created at: {moc_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python atom_splitter.py <path_to_master_note.md>")
    else:
        process_notes(sys.argv[1])