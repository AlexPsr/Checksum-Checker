#!/usr/bin/env python3
"""
checksum_checker.py
A tiny Tk-based utility that lets you pick a checksum type (MD5, SHA-256, SHA-512),
browse for a file, paste a reference checksum, and see whether they match.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import os
import sys

# ──────────── core logic ────────────
def calculate_checksum(file_path: str, algorithm: str) -> str | None:
    """
    Calculate the checksum of *file_path* using the chosen *algorithm*.
    Valid values: 'md5', 'sha256', 'sha512'.  Returns a hex digest string.
    """
    alg_map = {
        "md5": hashlib.md5,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
    }
    hasher_ctor = alg_map.get(algorithm.lower())
    if hasher_ctor is None:
        return None

    hasher = hasher_ctor()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (OSError, IOError) as e:
        messagebox.showerror("File Error", f"Could not read file:\n{e}")
        return None


# ──────────── GUI callbacks ────────────
def browse_file():
    """
    Ask the user to choose a file and display its path.
    """
    path = filedialog.askopenfilename(title="Select a file to checksum")
    if path:
        file_path_var.set(path)
        result_var.set("")# clear previous result


def do_compare():
    """
    Calculate the selected checksum for the chosen file and compare it to
    the reference string entered by the user.
    """
    filepath = file_path_var.get().strip()
    reference = reference_var.get().strip()

    if not filepath:
        messagebox.showinfo("No file", "Please select a file first.")
        return
    if not reference:
        messagebox.showinfo("No reference", "Please enter a reference checksum.")
        return

    algo = algo_var.get()
    calc = calculate_checksum(filepath, algo)

    if calc is None:
        return  # error already shown

    if calc.lower() == reference.lower():
        result_var.set("✅ Checksums match!")
    else:
        result_var.set(
            "❌ Checksums do NOT match.\n"
            f"Calculated ({algo.upper()}):\n{calc}"
        )


# ──────────── build the UI ────────────
root = tk.Tk()
root.title("Checksum Checker")
root.resizable(False, False)

# Fonts (optional aesthetics—works fine if unavailable)
try:
    import tkinter.font as tkfont
    bold_font = tkfont.nametofont("TkDefaultFont").copy()
    bold_font.configure(weight="bold")
except Exception:
    bold_font = None


# Algorithm selector
algo_frame = tk.Frame(root, pady=6, padx=10)
algo_frame.pack(anchor="w")

tk.Label(algo_frame, text="Checksum algorithm:").pack(side=tk.LEFT)

algo_var = tk.StringVar(value="md5")
for alg in ("md5", "sha256", "sha512"):
    tk.Radiobutton(
        algo_frame,
        text=alg.upper(),
        variable=algo_var,
        value=alg,
        padx=6
    ).pack(side=tk.LEFT)

# File chooser
file_frame = tk.Frame(root, pady=4, padx=10)
file_frame.pack(fill="x")

tk.Button(file_frame, text="Browse file…", command=browse_file).pack(side=tk.LEFT)

file_path_var = tk.StringVar()
file_label = tk.Label(
    file_frame,
    textvariable=file_path_var,
    anchor="w",
    wraplength=400
)
file_label.pack(side=tk.LEFT, padx=8, fill="x", expand=True)

# Reference checksum entry
ref_frame = tk.Frame(root, pady=4, padx=10)
ref_frame.pack(fill="x")

tk.Label(ref_frame, text="Reference checksum:").pack(side=tk.LEFT)

reference_var = tk.StringVar()
tk.Entry(ref_frame, textvariable=reference_var, width=64).pack(
    side=tk.LEFT,
    padx=6,
    fill="x",
    expand=True
)

# Compare button
tk.Button(
    root,
    text="Compare",
    command=do_compare,
    width=15,
    pady=4
).pack(pady=6)

label_font = bold_font if bold_font else "TkDefaultFont"

# Result field
result_var = tk.StringVar()
tk.Label(
    root,
    textvariable=result_var,
    fg="blue",
    wraplength=400,
    justify="left",
    font=label_font
).pack(pady=(0, 10), padx=10)

# ──────────── start the loop ────────────
if __name__ == "__main__":
    # Helpful tip if Tkinter is missing
    try:
        root.mainloop()
    except tk.TclError as e:
        sys.stderr.write(
            "Error starting Tkinter: {}\n"
            "On Debian/Ubuntu, you may need:\n"
            "    sudo apt-get install python3-tk\n".format(e)
        )
