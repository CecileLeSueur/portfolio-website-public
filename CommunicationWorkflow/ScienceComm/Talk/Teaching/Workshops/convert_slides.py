import subprocess
import os
from pathlib import Path

# Resolve paths relative to the script's location, not the working directory
SCRIPT_DIR = Path(__file__).parent
PDF_PATH = (SCRIPT_DIR / "../../../images/slides_workshop/FDR_modifApril2026.pdf").resolve()
OUTPUT_DIR = (SCRIPT_DIR / "../../../images/slides_workshop").resolve()
IMAGE_REL_PATH = "../../../images/slides_workshop"  # ← relative path as seen from index.qmd
DPI = 150  # ← was missing

print(f"Looking for PDF at: {PDF_PATH}")  # helpful for debugging
print(f"Output dir: {OUTPUT_DIR}")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# save each slide independently
subprocess.run([
    "pdftoppm", "-png", "-r", str(DPI),
    str(PDF_PATH), str(OUTPUT_DIR / "slide")
], check=True)

''' 
# Collect generated files in order
images = sorted(Path(OUTPUT_DIR).glob("slide-*.png"))

# Generate the carousel div block
lines = [':::: {.carousel .dark .framed autoplay="false" transition="none"}']
for img in images:
    rel_img = f"{IMAGE_REL_PATH}/{img.name}"  # ← e.g. ../../images/slides/slide-01.png
    lines.append(f':::: {{.carousel-item image="{rel_img}"}}')
    lines.append(":::")
lines.append(":::")

carousel_block = "\n".join(lines)

# Write it to a .qmd include file
with open("_carousel_include.qmd", "w") as f:
    f.write(carousel_block)

print(f"Generated carousel with {len(images)} slides.")
'''