# Music-of-Bitcoin


Music of Bitcoin is an adaptive MIDI music generator that uses blockchain data to generate music. It fetches the latest block height from the blockchain API, generates a MIDI file based on the data in the block, and plays the MIDI file.

Requirements
Python 3.6 or higher
mido library (pip install mido)
requests library (pip install requests)
Usage
To use Music of Bitcoin, simply run the main.py script in your terminal:

css
Copy code
python main.py
Music of Bitcoin will automatically check for a new block every minute and generate a new MIDI file if a new block is detected.

Improvements
Music of Bitcoin is a work in progress, and there are several areas that can be improved:

More complex algorithms for generating music based on blockchain data
Support for other blockchain APIs
Ability to customize the musical elements and MIDI file settings
Integration with other audio libraries for improved sound quality and flexibility
Feel free to contribute to this project by creating pull requests or opening issues for bugs or feature requests.
