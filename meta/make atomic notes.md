Split the note `<PATH_TO_NOTE.md>` into atomic notes and update the subject MOC at `<PATH_TO_SUBJECT_MOC.md>`.

Rules:
1. Zero Data Loss: Do NOT omit, modify, rephrase, or skip any point, detail, formula, code block, diagram, invariant, or edge case from the original file.
2. Short & Appropriate File Names: Save each atomic note in the same folder using a concise, descriptive filename (e.g., `producer-consumer-problem.md`).
3. No Useless `#` Headers: Do NOT add a redundant `# Title` top-level header inside the atomic notes. Start directly with content or `## Subheadings`.
4. Master Note Naming & Structure (`<PATH_TO_NOTE.md>`):
   - Keep/rename the master file using the natural title of the topic itself (e.g., `Classic Problems.md`, `Paging.md`).
   - STRICTLY BAN words like `moc`, `hub`, `index`, or `overview` in the master note filename.
   - Replace the master note's content with a clean index containing ONLY wikilinks (`[[atomic-note-name]]`) to the new atomic notes. Do NOT include full text, summaries, or transclusion embeds (`![[...]`).
5. Subject MOC Update (`<PATH_TO_SUBJECT_MOC.md>`): Link ONLY the master topic note (`[[<TOPIC_NAME>]]`) under the appropriate section in the subject MOC. Do not list the individual subatomic notes in the MOC.