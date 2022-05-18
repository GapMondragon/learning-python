def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)

# Printing Some Text
print(1)
print(2)
print(3)
print(4)
print(5)
print("Screen will now be cleared in 5 Seconds")
clear()
print(6)
print(7)
print(8)
print(9)
print(10)
# Waiting for 5 seconds to clear the screen

