---
title: "Lossy Checkpoint Compression in Full Waveform Inversion"
etype: 'unpublished'
collection: publications
permalink: /publication/2020-09-01-Lossy-Checkpoint-Compression-in-Full-Waveform-Inversion
excerpt: 'Submitted to GMD'
date: 2020-09-01
venue: 'Lossy Checkpoint Compression in Full Waveform Inversion'
paperurl: 'https://arxiv.org/pdf/2009.12623.pdf'
citation: ' Navjot Kukreja,  Jan Hueckelheim,  Mathias Louboutin,  John Washbourne,  Paul Kelly,  Gerard Gorman, &quot;Lossy Checkpoint Compression in Full Waveform Inversion.&quot; Lossy Checkpoint Compression in Full Waveform Inversion, 2020.'
---
Submitted to GMD

[Access paper here](https://arxiv.org/pdf/2009.12623.pdf){:target="_blank"}

This paper proposes a new method that combines check-pointing methods with error-controlled lossy compression for large-scale high-performance Full-Waveform Inversion (FWI), an inverse problem commonly used in geophysical exploration. This combination can significantly reduce data movement, allowing a reduction in run time as well as peak memory. In the Exascale computing era, frequent data transfer (e.g., memory bandwidth, PCIe bandwidth for GPUs, or network) is the performance bottleneck rather than the peak FLOPS of the processing unit. Like many other adjoint-based optimization problems, FWI is costly in terms of the number of floating-point operations, large memory footprint during backpropagation, and data transfer overheads. Past work for adjoint methods has developed checkpointing methods that reduce the peak memory requirements during backpropagation at the cost of additional floating-point computations. Combining this traditional checkpointing with error-controlled lossy compression, we explore the three-way tradeoff between memory, precision, and time to solution. We investigate how approximation errors introduced by lossy compression of the forward solution impact the objective function gradient and final inverted solution. Empirical results from these numerical experiments indicate that high lossy-compression rates (compression factors ranging up to 100) have a relatively minor impact on convergence rates and the quality of the final solution.
