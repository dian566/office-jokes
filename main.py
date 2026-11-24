"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = "My out-of-office reply said 'gone fishing for a better job' — HR called it 'too honest'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
