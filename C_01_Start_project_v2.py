# Functions go here
def start_project(decoration, start: object, lines):
    """Create headings (3 lines), subheadings (2 lines) and emphasised
    text / mini-headings (1 line). Only use emoji for single line statements"""

    middle = f"{decoration * 3} {start} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main Routine goes here
start_project("Programming is Fun!", 'decoration "=", lines: 3')
print()
start_project("programming is Still Fun!" 'decoration "*", lines: 2')
print()
start_project("Emoji in Action",  'decoration "🐍", lines: 1')

