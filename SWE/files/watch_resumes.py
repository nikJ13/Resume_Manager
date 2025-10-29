#!/usr/bin/env python3
"""
Resume Auto-Sync Watcher
Monitors resume files for changes and automatically syncs them.
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("Error: watchdog library is not installed.")
    print("Please install it by running:")
    print("  pip3 install watchdog")
    print("\nOr if that doesn't work, try:")
    print("  pip3 install --user watchdog")
    sys.exit(1)

# Import the sync function from the main script
import sync_resumes


class ResumeChangeHandler(FileSystemEventHandler):
    """Handles file system events for resume files."""
    
    def __init__(self, base_dir, debounce_seconds=2):
        self.base_dir = base_dir
        self.debounce_seconds = debounce_seconds
        self.last_sync_time = 0
        
    def on_modified(self, event):
        """Called when a file is modified."""
        if event.is_directory:
            return
        
        # Only process .docx files (not temporary Word files)
        if event.src_path.endswith('.docx') and not os.path.basename(event.src_path).startswith('~$'):
            self.trigger_sync(event.src_path)
    
    def on_created(self, event):
        """Called when a file is created."""
        if event.is_directory:
            return
        
        if event.src_path.endswith('.docx') and not os.path.basename(event.src_path).startswith('~$'):
            self.trigger_sync(event.src_path)
    
    def trigger_sync(self, changed_file):
        """Trigger a sync with debouncing to avoid multiple syncs."""
        current_time = time.time()
        
        # Debounce: only sync if enough time has passed since last sync
        if current_time - self.last_sync_time < self.debounce_seconds:
            return
        
        self.last_sync_time = current_time
        
        print(f"\n{'=' * 60}")
        print(f"Change detected: {os.path.basename(changed_file)}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'=' * 60}")
        
        # Run the sync
        sync_resumes.sync_resumes(self.base_dir)
        
        print(f"\n👀 Watching for changes... (Press Ctrl+C to stop)")


def watch_resumes(base_dir):
    """Start watching the directory for changes."""
    base_path = Path(base_dir).resolve()
    
    print("=" * 60)
    print("Resume Auto-Sync Watcher")
    print("=" * 60)
    print(f"\n📁 Watching directory: {base_path}")
    print(f"👀 Monitoring for changes to .docx files...")
    print(f"⚙️  When a resume is modified, all others will be automatically synced")
    print(f"\nPress Ctrl+C to stop watching\n")
    
    event_handler = ResumeChangeHandler(base_dir)
    observer = Observer()
    observer.schedule(event_handler, str(base_path), recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping watcher...")
        observer.stop()
    
    observer.join()
    print("✓ Watcher stopped")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_directory = sys.argv[1]
    else:
        base_directory = "."
    
    if not os.path.exists(base_directory):
        print(f"Error: Directory '{base_directory}' does not exist")
        sys.exit(1)
    
    watch_resumes(base_directory)
