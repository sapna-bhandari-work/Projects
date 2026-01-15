import urllib.request
from bs4 import BeautifulSoup
import threading
import queue
import sys
import time
import signal

# Set to keep track of visited links and avoid duplicates
linksVisited = set()

# Event used to gracefully stop all threads
stop_event = threading.Event()


class WorkerThread(threading.Thread):
    """
    Worker thread class responsible for crawling URLs
    """

    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue

    def run(self):
        # Keep running until stop signal is received
        while not stop_event.is_set():
            try:
                # Get URL from queue (with timeout to allow graceful exit)
                url = self.task_queue.get(timeout=1)
            except queue.Empty:
                continue

            try:
                # Open the URL
                with urllib.request.urlopen(url) as response:
                    site_content = response.read()

                # Parse HTML and extract all anchor tags
                soup = BeautifulSoup(site_content, 'html.parser')
                for link in soup.find_all('a'):
                    if link.has_attr('href'):
                        link_url = link['href']

                        # Convert relative links to absolute links
                        if not link_url.startswith('http'):
                            link_url = target + link_url

                        # Skip external domain links
                        if not link_url.startswith(target):
                            continue

                        # Add unvisited links to queue
                        if link_url not in linksVisited:
                            linksVisited.add(link_url)
                            self.task_queue.put(link_url)
                            print(link_url)

            except Exception:
                # Ignore all crawling errors and continue
                pass

            finally:
                # Mark the current task as done
                self.task_queue.task_done()


def shutdown_handler(sig, frame):
    """
    Handles graceful shutdown on Ctrl+C
    """
    print("\nStopping crawler...")
    stop_event.set()


# Register signal handler for graceful shutdown
signal.signal(signal.SIGINT, shutdown_handler)

# Initialize a thread-safe queue
task_queue = queue.Queue()

# Ensure target URL is provided
if len(sys.argv) < 2:
    print("Please pass a target URL in the format: http://www.example.com/")
    sys.exit(0)

# Target website to crawl
target = sys.argv[1]

# Mark root URL as visited
linksVisited.add(target)
linksVisited.add(target + '#')

# Create and start worker threads
threads = []
for _ in range(10):
    thread = WorkerThread(task_queue)
    thread.daemon = True
    thread.start()
    threads.append(thread)

# Start crawling from root URL
task_queue.put(target)

try:
    # Wait for all queued tasks to complete
    task_queue.join()
except KeyboardInterrupt:
    shutdown_handler(None, None)

# Signal all threads to stop
stop_event.set()

# Wait for threads to exit cleanly
for thread in threads:
    thread.join()

print("Crawling completed")
