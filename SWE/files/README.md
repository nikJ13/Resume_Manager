# Resume Synchronization Scripts

This collection of scripts helps you manage multiple resume versions that differ only by email address. When you update one resume, all others are automatically updated while preserving their respective email addresses, and all are converted to PDF.

## 📋 Features

- ✅ Automatically syncs content across multiple resume Word documents
- ✅ Preserves different email addresses in each resume
- ✅ Converts all resumes to PDF after syncing
- ✅ Manual sync mode or automatic file watching
- ✅ Supports any folder structure

## 🚀 Quick Start

### Prerequisites

**For macOS (your system):**

1. **Python 3** - Check if installed:
   ```bash
   python3 --version
   ```
   If not installed:
   ```bash
   brew install python3
   ```

2. **LibreOffice** (for PDF conversion):
   ```bash
   # Option 1: Using Homebrew (recommended)
   brew install --cask libreoffice
   
   # Option 2: Download from https://www.libreoffice.org/
   ```

### Installation

**Easy Setup (Recommended):**
```bash
# Navigate to where you saved the scripts
cd /path/to/scripts

# Make setup script executable
chmod +x setup_macos.sh

# Run the setup
./setup_macos.sh
```

**Manual Installation:**
```bash
# Install Python packages
pip3 install python-docx
pip3 install watchdog

# If the above doesn't work, try:
pip3 install --user python-docx
pip3 install --user watchdog

# Make scripts executable
chmod +x sync_resumes.py watch_resumes.py
```

## 📖 Usage

### Option 1: Manual Sync (Run Once)

Use this when you've just finished editing a resume and want to sync all others.

```bash
# If scripts are in your resume directory:
python3 sync_resumes.py

# Or specify the directory containing your resume folders:
python3 sync_resumes.py /path/to/resume/folders

# Or use the bash wrapper:
./sync_resumes.sh /path/to/resume/folders
```

**What it does:**
1. Finds all .docx files in the directory (and subdirectories)
2. Identifies the most recently modified resume
3. Updates all other resumes with the same content
4. Preserves each resume's unique email address
5. Converts all resumes to PDF

### Option 2: Auto-Watch Mode (Continuous)

Use this to have your resumes automatically sync whenever you save changes.

```bash
# Watch current directory:
python3 watch_resumes.py

# Or specify directory:
python3 watch_resumes.py /path/to/resume/folders
```

**What it does:**
- Continuously monitors your resume folder for changes
- Automatically triggers sync whenever you save a .docx file
- Keeps running until you press Ctrl+C

## 📁 Folder Structure

Your folder structure can be anything. Examples:

```
Option A: Separate folders
resumes/
├── cmu-email/
│   ├── resume.docx
│   └── resume.pdf
├── gmail1/
│   ├── resume.docx
│   └── resume.pdf
├── andrew-email/
│   ├── resume.docx
│   └── resume.pdf
...

Option B: All in one folder
resumes/
├── resume-cmu.docx
├── resume-cmu.pdf
├── resume-gmail1.docx
├── resume-gmail1.pdf
...

Option C: Any structure
└── just point the script to the root folder!
```

## ⚙️ How It Works

1. **Detection**: Script finds the most recently modified .docx file (the one you just edited)

2. **Email Preservation**: 
   - Extracts email from source resume (e.g., `niketj@cs.cmu.edu`)
   - For each target resume, extracts its email (e.g., `nikj1301@gmail.com`)
   - Copies all content from source to target
   - Replaces source email with target's original email

3. **PDF Conversion**: Uses LibreOffice to convert all .docx files to PDF

## 🔧 Customization

### Modify Email List

Edit the `EMAILS` list in `sync_resumes.py` if you have different email addresses:

```python
EMAILS = [
    "your.email1@domain.com",
    "your.email2@domain.com",
    # Add more as needed
]
```

### Change Debounce Time

In `watch_resumes.py`, adjust the debounce time (default 2 seconds) to control how quickly it syncs after detecting changes:

```python
event_handler = ResumeChangeHandler(base_dir, debounce_seconds=2)
```

## 🐛 Troubleshooting

### "LibreOffice not found"
- Install LibreOffice (see Prerequisites above)
- Make sure it's in your system PATH

### "No .docx files found"
- Check that you're running the script in the correct directory
- Make sure your resume files have .docx extension

### Emails not being replaced correctly
- Ensure each resume has exactly one email address
- Check that emails follow standard format (name@domain.com)

### Script doesn't detect changes in watch mode
- Make sure you're saving the file (not just editing)
- Check that the file isn't being saved with a ~ prefix (temp file)

## 💡 Tips

1. **Best Practice**: Use the watch mode while actively working on your resume. Just start it once and forget about it!

2. **Workflow**: 
   - Start watch mode: `python3 watch_resumes.py`
   - Open any resume and make edits
   - Save the file
   - Watch as all resumes automatically sync and convert to PDF!

3. **Quick Manual Sync**: If you just want to sync once without watching, use `python3 sync_resumes.py`

## 📝 Example Output

```
==============================================================
Resume Synchronization Script
==============================================================

Found 5 resume file(s):
  - resume.docx (modified: 2025-10-26 14:30:45)
  - resume.docx (modified: 2025-10-26 14:28:12)
  - resume.docx (modified: 2025-10-26 14:28:10)
  - resume.docx (modified: 2025-10-25 09:15:30)
  - resume.docx (modified: 2025-10-25 09:15:28)

📄 Source (most recent): resume.docx
📧 Source email: niketj@cs.cmu.edu

==============================================================
Updating resumes...
==============================================================

✓ resume.docx (source - skipped)

📝 Updating: resume.docx
  Current email: nikj1301@gmail.com
  ✓ Replaced niketj@cs.cmu.edu → nikj1301@gmail.com
  ✓ Updated successfully

... (continues for all resumes)

==============================================================
Converting to PDF...
==============================================================

📄 resume.docx
  ✓ Converted to PDF: resume.pdf

... (continues for all resumes)

==============================================================
✓ Synchronization complete!
==============================================================
```

## 🤝 Support

If you encounter any issues:
1. Check the Troubleshooting section above
2. Ensure all prerequisites are installed
3. Verify your folder structure and file names
4. Check that your resume files are valid .docx format

## 📄 License

Feel free to use and modify these scripts for your personal use!
