# Signal Averaging Filter for Medical Imaging Simulation

This repository accompanies the advanced undergraduate course "Fundamentals of Electronic Imaging" taught by Professor Ernest Sternglass. The project demonstrates a core challenge in both television and medical imaging: improving the signal-to-noise ratio (SNR) through digital signal averaging.

## Mathematical Background

A moving average (or boxcar) filter is one of the simplest noise‑reduction techniques. Given a discrete signal \(x[n]\) of length \(N\) and an odd window size \(W\), the filtered signal \(y[n]\) is computed as

\[
y[n] = \frac{1}{W} \sum_{k=-(W-1)/2}^{(W-1)/2} x[n+k],
\]

where the sum runs over the available samples near each position. At the boundaries, the window is truncated so that only the available samples are averaged (simple padding is also possible). Averaging over multiple independent realizations of the same signal reduces the noise variance by a factor equal to the number of realizations; here we simulate the effect by averaging adjacent samples of a single noisy trace.

## Repository Structure

- `signal_processor.py` – contains the simulation of a noisy sine‑wave signal (`generate_noisy_signal`) and a stub for the moving‑average filter (`apply_averaging_filter`) that students must complete.
- `.gitignore` – standard Python‑project ignore file.
- `README.md` – this file.

## How to Use

1. Clone the repository.
2. Install the required dependencies (NumPy).
3. Run the script to generate a noisy signal and test your implementation of `apply_averaging_filter`.
4. Observe the improvement in SNR by comparing the raw and filtered signals.

The exercise mirrors the problem of reducing quantum noise in low‑dose X‑ray images and suppressing static in early television camera tubes—two areas where Professor Sternglass made pioneering contributions.