import glob
import os
import random
import shutil

def rotate():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Search for all arcade contribution SVGs in base directory or ready to go
    svg_files = glob.glob(os.path.join(base_dir, "acrade-contributions *.svg"))
    if not svg_files:
        svg_files = glob.glob(os.path.join(base_dir, "ready to go", "acrade-contributions *.svg"))
        
    if not svg_files:
        print("No arcade contribution SVG files found.")
        return

    # Sort files to ensure deterministic ordering for sequential rotation
    svg_files.sort()
    
    state_file = os.path.join(base_dir, ".github", "arcade_index.txt")
    next_idx = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r", encoding="utf-8") as f:
                last_idx = int(f.read().strip())
                next_idx = (last_idx + 1) % len(svg_files)
        except Exception:
            next_idx = random.randint(0, len(svg_files) - 1)
    else:
        next_idx = random.randint(0, len(svg_files) - 1)

    selected_svg = svg_files[next_idx]
    game_name = os.path.basename(selected_svg).replace("acrade-contributions ", "").replace(".svg", "").title()
    print(f"Selected Arcade Game Mode: {game_name} ({os.path.basename(selected_svg)})")

    # Save state
    os.makedirs(os.path.dirname(state_file), exist_ok=True)
    with open(state_file, "w", encoding="utf-8") as f:
        f.write(str(next_idx))

    # Targets to update
    targets = [
        os.path.join(base_dir, "arcade-contribution.svg"),
        os.path.join(base_dir, "ready to go", "arcade-contribution.svg")
    ]

    for target in targets:
        shutil.copyfile(selected_svg, target)
        print(f"Updated: {target}")

if __name__ == "__main__":
    rotate()
