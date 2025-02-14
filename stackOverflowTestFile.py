import numpy as np

def convolve_1d(signal, kernel):
    kernel = kernel[::-1]
    return [
        np.dot(
            signal[max(0,i):min(i+len(kernel),len(signal))],
            kernel[max(-i,0):len(signal)-i*(len(signal)-len(kernel)<i)],
        )
        for i in range(1-len(kernel),len(signal))
    ]

print(convolve_1d([1, 1, 2, 2, 1], [1, 1, 1, 3]))

print(np.convolve([1, 1, 2, 2, 1], [1, 1, 1, 3],mode="full"))

def convolve_1d_mk2(signal, kernel):
    kernel = kernel[::-1]  # Reverse kernel for convolution
    output = []
    
    for i in range(1 - len(kernel), len(signal)):  # Slide kernel across signal
        start = max(0, i)
        # max(0, -3)
        end = min(i + len(kernel), len(signal))
        # min(-3 + 4, 5)
        kernel_start = max(-i, 0)
        # max(3, 0)
        kernel_end = kernel_start + (end - start)
        # 3 + (1 - 0) = 4

        conv_result = np.dot(signal[start:end], kernel[kernel_start:kernel_end])
        # signal[0:1], kernel[3:4]
        # signal[0:2], kernel[2:4]
        output.append(conv_result)
    
    return output

print(convolve_1d([1, 1, 2, 2, 1], [1, 1, 1, 3]))


def convolve_1d_same(signal, kernel):
    kernel = kernel[::-1]  # Reverse kernel for convolution
    
    pad_size = (len(kernel) - 1) // 2
    padded_signal = np.pad(signal, (pad_size, (len(kernel) - 1) - pad_size), mode='constant')

    output = [
        np.dot(padded_signal[i : i + len(kernel)], kernel)
        for i in range(len(signal))  # Ensure same output size as input signal
    ]
    
    return np.array(output)

print(convolve_1d_same([1, 1, 2, 2, 1], [1, 3,1,1]))
print(np.convolve([1, 1, 2, 2, 1], [1, 3,1,1 ],'same'))
print(np.convolve([1, 1, 2, 2, 1], [1, 3,1,1 ],'full'))