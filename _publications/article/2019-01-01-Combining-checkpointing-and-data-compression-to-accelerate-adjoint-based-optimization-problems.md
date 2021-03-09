---
title: "Combining checkpointing and data compression to accelerate adjoint-based optimization problems"
etype: 'article'
collection: publications
permalink: /publication/2019-01-01-Combining-checkpointing-and-data-compression-to-accelerate-adjoint-based-optimization-problems
excerpt: '(Euro-Par 2019: Parallel Processing)'
date: 2019-01-01
venue: 'Combining checkpointing and data compression to accelerate adjoint-based optimization problems'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/PASC/2019/kukreja2019PASCccd/kukreja2019PASCccd.pdf'
citation: ' Navjot Kukreja,  Jan H{\&quot;u}ckelheim,  Mathias Louboutin,  Paul Hovland,  Gerard Gorman, &quot;Combining checkpointing and data compression to accelerate adjoint-based optimization problems.&quot; Combining checkpointing and data compression to accelerate adjoint-based optimization problems, 2019.'
---
(Euro-Par 2019: Parallel Processing)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/PASC/2019/kukreja2019PASCccd/kukreja2019PASCccd.pdf){:target="_blank"}

Seismic inversion and imaging are adjoint-based optimization problems that processes up to terabytes of data, regularly exceeding the memory capacity of available computers. Data compression is an effective strategy to reduce this memory requirement by a certain factor, particularly if some loss in accuracy is acceptable. A popular alternative is checkpointing, where data is stored at selected points in time, and values at other times are recomputed as needed from the last stored state. This allows arbitrarily large adjoint computations with limited memory, at the cost of additional recomputations. In this paper we combine compression and checkpointing for the first time to compute a realistic seismic inversion. The combination of checkpointing and compression allows larger adjoint computations compared to using only compression, and reduces the recomputation overhead significantly compared to using only checkpointing.
