import requests
import time
import mido
from mido import Message, MidiFile, MidiTrack

# Set up the blockchain API URL
API_URL = "https://blockchain.info/"

# Define the musical elements
ELEMENTS = {
    "rhythm": {"factor": 1000},
    "polyphony": {"factor": 1000000000, "control": 0},
    "dynamics": {"factor": 1000},
    "harmony": {"factor": 1000, "chords": [[60, 64, 67], [63, 67, 70]]},
    "microtonality": {"factor": 1, "pitchwheel": 4096},
    "mempool": {"factor": 1000, "silence": 0.2},
    "volume": {"factor": 1, "control": 7},
    "tempo": {"factor": 1, "bpm": 120},
}

# Define the MIDI file settings
MIDI_SETTINGS = {
    "program": 0,
    "time_signature": (4, 4),
    "tempo": 500000,
}

# Define the MIDI message types and their attributes
MESSAGE_TYPES = {
    "note_on": {"velocity": 127},
    "note_off": {"velocity": 0},
    "control_change": {},
    "pitchwheel": {},
}

# Define the MIDI file tracks
TRACKS = {
    "notes": {"messages": [], "channel": 0},
    "control": {"messages": [], "channel": 0},
}

# Helper functions
def get_latest_block_height():
    """
    Get the latest block height from the blockchain API.
    """
    response = requests.get(API_URL + "latestblock")
    if response.status_code == 200:
        return response.json()["height"]
    else:
        return -1

def get_block_transactions_count(block_height):
    """
    Get the number of transactions in the given block height from the blockchain API.
    """
    response = requests.get(API_URL + f"block-height/{block_height}?format=json")
    if response.status_code == 200:
        return response.json()["blocks"][0]["n_tx"]
    else:
        return -1

def get_hash_rate():
    """
    Get the hash rate from the blockchain API.
    """
    response = requests.get(API_URL + "q/hashrate")
    if response.status_code == 200:
        return int(response.text)
    else:
        return -1

def get_market_price():
    """
    Get the market price from the blockchain API.
    """
    response = requests.get(API_URL + "ticker")
    if response.status_code == 200:
        return float(response.json()["USD"]["last"])
    else:
        return -1

def create_adaptive_midi(block_height, transactions_count, hash_rate, market_price):
    """
    Create an adaptive MIDI file based on the given blockchain data.
    """
    # Calculate the musical factors
    factors = {}
    for element, data in ELEMENTS.items():
        factor = data["factor"]
        if element == "harmony":
            if market_price < factor / 2:
                chords = data["chords"][0]
            else:
                chords = data["chords"][1]
            factors[element] = {"chords": chords}
        else:
            factors[element] = {"factor": locals()[element + "_factor"] / factor}

    # Create the MIDI file
    midi_file = MidiFile()
    midi_file.ticks_per_beat = 480

    # Define the MIDI file tracks
    TRACKS = {
        "notes": {"messages": [], "channel": 0},
        "control": {"messages": [], "channel": 0},
    }

    # Helper functions
    def get_latest_block_height():
        # Make a request to the blockchain API to get the latest block height
        response = requests.get(API_URL + "latestblock")
        if response.status_code == 200:
            return response.json()["height"]
        else:
            return -1

    def get_block_transactions_count(block_height):
        # Make a request to the blockchain API to get the number of transactions in the block
        response = requests.get(API_URL + f"block-height/{block_height}?format=json")
        if response.status_code == 200:
            return response.json()["blocks"][0]["n_tx"]
        else:
            return -1

    def get_hash_rate():
        # Make a request to the blockchain API to get the hash rate
        response = requests.get(API_URL + "q/hashrate")
        if response.status_code == 200:
            return int(response.text)
        else:
            return -1

    def get_market_price():
        # Make a request to the blockchain API to get the market price
        response = requests.get(API_URL + "ticker")
        if response.status_code == 200:
            return float(response.json()["USD"]["last"])
        else:
            return -1

    def create_adaptive_midi(block_height, transactions_count, hash_rate, market_price):
        # Calculate the musical factors
        factors = {}
        for element, data in ELEMENTS.items():
            factor = data["factor"]
            if element == "harmony":
                if market_price < factor / 2:
                    chords = data["chords"][0]
                else:
                    chords = data["chords"][1]
                factors[element] = {"chords": chords}
            else:
                factors[element] = {"factor": locals()[element + "_factor"] / factor}

        # Create the MIDI file
        midi_file = MidiFile()
        midi_file.ticks_per_beat = 480

        # Add the tracks
        for track_name, track_data in TRACKS.items():
            track = MidiTrack()
            midi_file.tracks.append(track)

            # Add the messages to the track
            messages = track_data["messages"]
            channel = track_data["channel"]
            time_counter = 0
            for message_type, message_data in MESSAGE_TYPES.items():
                message_factor = factors[message_type]["factor"]
                for i in range(transactions_count):
                    message = Message(message_type, channel=channel, time=int(time_counter))
                    message.update(message_data)
                    if message_type == "note_on":
                        message.note = chords[i % len(chords)]
                        message.velocity = int(127 * dynamics_factor)
                    elif message_type == "control_change":
                        if message_data.get("control") == 0:
                            message.value = int(16 * polyphony_factor)
                        elif message_data.get("control") == 32:
                            message.value = 0
                    elif message_type == "pitchwheel":
                        message.pitch = int(4096 * (microtonality_factor - 0.5))
                    messages.append(message)
                    time_counter += int(message_factor * rhythm_factor * 1000)

        # Save the MIDI file
        output_file = f"block_{block_height}.mid"
        midi_file.save(output_file)

        # Play the MIDI file
        play_midi_file(output_file)

    def play_midi_file(output_file):
        # Open the MIDI file
        with mido.open_output() as port:
            # Play the MIDI file
            mid = MidiFile(output_file)
            for msg in mid.play():
                port.send(msg)


# Main loop
while True:
    # Get the latest block height
    block_height = get_latest_block_height()


    def main():
        # Define the initial value of the current block height
        current_block_height = get_latest_block_height()

        while True:
            block_height = get_latest_block_height()
            if block_height != current_block_height:
                current_block_height = block_height
                print(f'New block detected: {current_block_height}')

                # Get the number of transactions in the block
                transactions_count = get_block_transactions_count(current_block_height)
                # Get the hash rate and market price
                hash_rate = get_hash_rate()
                market_price = get_market_price()

                # Create an adaptive MIDI file based on the blockchain data
                create_adaptive_midi(current_block_height, transactions_count, hash_rate, market_price)

            time.sleep(60)  # Check for a new block every minute


    if __name__ == '__main__':
        main()

    # Check if a new block has been detected
    if block_height != current_block_height:
        current_block_height = block_height
        print(f'New block detected: {current_block_height}')

        # Get the number of transactions in the block
        transactions_count = get_block_transactions_count(current_block_height)

        # Get the hash rate and market price
        hash_rate = get_hash_rate()
        market_price = get_market_price()

        # Create an adaptive MIDI file based on the blockchain data
        create_adaptive_midi(current_block_height, transactions_count, hash_rate, market_price)

        # Play the generated MIDI file
        play_midi_file(output_file)

    # Wait for 1 minute before checking for a new block again
    time.sleep(60)
