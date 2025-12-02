# Smart Home IoT Lightweight Encryption Demo

import random
import time
from cryptography.fernet import Fernet

# Simulated Smart Home Devices
def get_temperature():
    """Simulate a temperature sensor (20-30°C)."""
    return random.randint(20, 30)

def get_door_status():
    """Simulate a smart door lock ('Locked' or 'Unlocked')."""
    return random.choice(["Locked", "Unlocked"])


# Encryption Setup
# Generate symmetric encryption key (Fernet)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encryption and Decryption Functions
def encrypt_data(data):
    """
    Encrypt data using Fernet.
    Returns: encrypted_data, encryption_time_ms
    """
    start = time.time()
    encrypted = cipher.encrypt(str(data).encode())
    end = time.time()
    return encrypted, (end - start) * 1000  # time in milliseconds

def decrypt_data(encrypted):
    """
    Decrypt data using Fernet.
    Returns: decrypted_data, decryption_time_ms
    """
    start = time.time()
    decrypted = cipher.decrypt(encrypted).decode()
    end = time.time()
    return decrypted, (end - start) * 1000  # time in milliseconds

# Device Simulation Dictionary
devices = {
    "Temperature Sensor": get_temperature,
    "Door Lock": get_door_status
}

# Simulation: Multiple Readings
print("=== Smart Home IoT Encryption Demo ===\n")

all_enc_times = []
all_dec_times = []

for iteration in range(5):  # simulate 5 cycles
    print(f"--- Cycle {iteration + 1} ---")
    for device_name, func in devices.items():
        # Generate device data
        value = func()

        # Encrypt
        encrypted, enc_time = encrypt_data(value)
        all_enc_times.append(enc_time)

        # Decrypt
        decrypted, dec_time = decrypt_data(encrypted)
        all_dec_times.append(dec_time)

        # Print results
        print(f"{device_name}:")
        print(f"  Original Data   : {value}")
        print(f"  Encrypted Data  : {encrypted}")
        print(f"  Decrypted Data  : {decrypted}")
        print(f"  Encryption Time : {enc_time:.3f} ms")
        print(f"  Decryption Time : {dec_time:.3f} ms\n")

    time.sleep(1)  # wait 1 second before next cycle

# Average Encryption/Decryption Time
avg_enc_time = sum(all_enc_times) / len(all_enc_times)
avg_dec_time = sum(all_dec_times) / len(all_dec_times)

print(f"Average Encryption Time per Reading: {avg_enc_time:.3f} ms")
print(f"Average Decryption Time per Reading: {avg_dec_time:.3f} ms")

print("=== Demo Complete ===")

