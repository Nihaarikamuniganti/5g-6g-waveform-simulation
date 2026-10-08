import numpy as np
import matplotlib.pyplot as plt

def generate_qam_symbols(num_symbols, m_ary=16):
    """Generates random high-order QAM symbols."""
    k = int(np.log2(m_ary))
    # Random bits
    bits = np.random.randint(0, 2, num_symbols * k)
    # Simple normalization for QAM constellation
    if m_ary == 16:
        # 16-QAM mapping approximation
        real = np.random.choice([-3, -1, 1, 3], size=num_symbols)
        imag = np.random.choice([-3, -1, 1, 3], size=num_symbols)
        symbols = (real + 1j * imag) / np.sqrt(10)
    else:
        # Fallback to QPSK
        symbols = (2 * np.random.randint(0, 2, num_symbols) - 1 + 
                   1j * (2 * np.random.randint(0, 2, num_symbols) - 1)) / np.sqrt(2)
    return symbols

def calculate_papr(signal):
    """Calculates the Peak-to-Average Power Ratio (PAPR) in dB."""
    peak_power = np.max(np.abs(signal)**2)
    avg_power = np.mean(np.abs(signal)**2)
    papr = 10 * np.log10(peak_power / avg_power)
    return papr

# Simulation Parameters
num_subcarriers = 64
num_symbols = 1000

# 1. Generate QAM symbols & apply IFFT (Multicarrier simulation like OFDM)
data_symbols = generate_qam_symbols(num_subcarriers * num_symbols, m_ary=16)
data_matrix = data_symbols.reshape((num_symbols, num_subcarriers))
time_domain_signal = np.fft.ifft(data_matrix, axis=1).flatten()

# 2. Calculate PAPR
papr_value = calculate_papr(time_domain_signal)
print(f"Calculated Signal PAPR: {papr_value:.2f} dB")

# 3. Simulate a simple Rayleigh fading channel effect
h = (np.random.randn(len(time_domain_signal)) + 1j * np.random.randn(len(time_domain_signal))) / np.sqrt(2)
faded_signal = time_domain_signal * h

print("Simulation completed successfully!")
