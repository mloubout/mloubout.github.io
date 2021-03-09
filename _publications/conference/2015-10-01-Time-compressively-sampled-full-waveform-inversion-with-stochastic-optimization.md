---
title: "Time compressively sampled full-waveform inversion with stochastic optimization"
etype: 'conference'
collection: publications
permalink: /publication/2015-10-01-Time-compressively-sampled-full-waveform-inversion-with-stochastic-optimization
excerpt: '(SEG, New Orleans)'
date: 2015-10-01
venue: 'Time compressively sampled full-waveform inversion with stochastic optimization'
paperurl: 'https://slim.gatech.edu/Publications/Public/Conferences/SEG/2015/louboutin2015SEGtcs/louboutin2015SEGtcs.html'
citation: ' Mathias Louboutin,  Felix Herrmann, &quot;Time compressively sampled full-waveform inversion with stochastic optimization.&quot; Time compressively sampled full-waveform inversion with stochastic optimization, 2015.'
---
(SEG, New Orleans)

[Access paper here](https://slim.gatech.edu/Publications/Public/Conferences/SEG/2015/louboutin2015SEGtcs/louboutin2015SEGtcs.html){:target="_blank"}

Time-domain Full-Waveform Inversion (FWI) aims to image the subsurface of the earth accurately from field recorded data and can be solved via the reduced adjoint-state method. However, this method requires access to the forward and adjoint wavefields that are meet when computing gradient updates. The challenge here is that the adjoint wavefield is computed in reverse order during time stepping and therefore requires storage or other type of mitigation because storing the full time history of the forward wavefield is too expensive in realistic 3D settings. To overcome this challenge, we propose an approximate adjoint-state method where the wavefields are subsampled randomly, which drastically the amount of storage needed. By using techniques from stochastic optimization, we control the errors induced by the subsampling. Examples of the proposed technique on a synthetic but realistic 2D model show that the subsampling-related artifacts can be reduced significantly by changing the sampling for each source after each model update. Combination of this gradient approximation with a quasi-Newton method shows virtually artifact free inversion results requiring only 5\% of storage compared to saving the history at Nyquist. In addition, we avoid having to recompute the wavefields as is required by checkpointing.
