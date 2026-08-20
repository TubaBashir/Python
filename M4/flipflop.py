import time

def text_flip_flop():
    # Start with a baseline state
    state = True
    
    print("Starting Flip-Flop simulation. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            if state:
                print("🟢 FLIP")
            else:
                print("🔴 FLOP")
            
            # This line flips the boolean value to its opposite
            state = not state
            
            # Wait for 1 second before alternating
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    text_flip_flop()
