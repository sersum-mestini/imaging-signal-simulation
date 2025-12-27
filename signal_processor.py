"""
Signal Processing Simulation for Electronic Imaging
Course: Fundamentals of Electronic Imaging
Professor: Ernest Sternglass

This module simulates a noisy signal (akin to television static or X‑ray quantum noise)
and provides a moving‑average filter to improve the signal‑to‑noise ratio (SNR).
"""

import numpy as np

def generate_noisy_signal(length=1000, frequency=0.05, noise_level=0.5):
    """
    Generate a clean sine wave signal and add Gaussian noise.
    
    Parameters
    ----------
    length : int, default=1000
        Number of samples.
    frequency : float, default=0.05
        Frequency of the sine wave (normalized).
    noise_level : float, default=0.5
        Standard deviation of the Gaussian noise.
    
    Returns
    -------
    noisy_signal : numpy.ndarray
        The generated signal with additive Gaussian noise.
    """
    t = np.arange(length)
    clean_signal = np.sin(2 * np.pi * frequency * t)
    noise = np.random.normal(0, noise_level, length)
    noisy_signal = clean_signal + noise
    return noisy_signal

def apply_averaging_filter(signal, window_size):
    """
    Apply a moving average filter to smooth the signal.
    
    The filter uses a symmetric window of `window_size` samples (odd recommended).
    At the boundaries, only the available samples inside the signal are averaged.
    
    Parameters
    ----------
    signal : numpy.ndarray
        Input noisy signal (1‑D array).
    window_size : int
        Size of the moving window (must be a positive integer).
    
    Returns
    -------
    filtered_signal : numpy.ndarray
        The smoothed signal, same length as the input.
    
    TODO
    ----
    Replace the `pass` statement with a proper moving‑average implementation.
    """
    pass

if __name__ == "__main__":
    # Quick demonstration: generate a noisy signal and print its shape
    signal = generate_noisy_signal(length=200, frequency=0.1, noise_level=0.3)
    print(f"Generated signal length: {len(signal)}")
    print(f"First 10 samples: {signal[:10]}")
    print("\nThe averaging filter is not yet implemented.")
    print("Run the tests after completing `apply_averaging_filter`.")