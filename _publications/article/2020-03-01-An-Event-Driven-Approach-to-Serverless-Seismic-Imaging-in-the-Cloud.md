---
title: "An Event-Driven Approach to Serverless Seismic Imaging in the Cloud"
etype: 'article'
collection: publications
permalink: /publication/2020-03-01-An-Event-Driven-Approach-to-Serverless-Seismic-Imaging-in-the-Cloud
excerpt: '(IEEE Transactions on Parallel and Distributed Systems)'
date: 2020-03-01
venue: 'An Event-Driven Approach to Serverless Seismic Imaging in the Cloud'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/IEEETPDS/2020/witte2019TPDedas/witte2019TPDedas.html'
citation: ' Philipp Witte,  Mathias Louboutin,  Henryk Modzelewski,  Charles Jones,  James Selvage,  Felix Herrmann, &quot;An Event-Driven Approach to Serverless Seismic Imaging in the Cloud.&quot; An Event-Driven Approach to Serverless Seismic Imaging in the Cloud, 2020.'
---
(IEEE Transactions on Parallel and Distributed Systems)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/IEEETPDS/2020/witte2019TPDedas/witte2019TPDedas.html){:target="_blank"}

Adapting the cloud for high-performance computing (HPC) is a challenging task, as software for HPC applications hinges on fast network connections and is sensitive to hardware failures. Using cloud infrastructure to recreate conventional HPC clusters is therefore in many cases an infeasible solution for migrating HPC applications to the cloud. As an alternative to the generic lift and shift approach, we consider the specific application of seismic imaging and demonstrate a serverless and event-driven pproach for running large-scale instances of this problem in the cloud. Instead of permanently running compute instances, our workflow is based on a serverless architecture with high throughput batch computing and event-driven computations, in which computational resources are only running as long as they are utilized. We demonstrate that this approach is very flexible and allows for resilient and nested levels of parallelization, including domain decomposition for solving the underlying partial differential equations. While the event-driven approach introduces some overhead as computational resources are repeatedly restarted, it inherently provides resilience to instance shut-downs and allows a significant reduction of cost by avoiding idle instances, thus making the cloud a viable alternative to on-premise clusters for large-scale seismic imaging.
