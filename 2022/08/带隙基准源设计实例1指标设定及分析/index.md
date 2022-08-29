# 带隙基准源设计实例：（1）指标设定及分析


从今年 4 月份开始，我在 bilibili 平台陆续发布了[《带隙基准源设计》](https://space.bilibili.com/39142721/channel/collectiondetail?sid=358546&)系列视频，直到近日才更新完毕。在视频结尾，我计划出一系列带隙基准源的设计实例，以方便大家对带隙基准源的设计流程有一个更直观的认识。

最开始的计划是采用视频的方式进行带隙基准源的设计实况，但考虑到指标设定、电路结构分析、晶体管参数计算、电路仿真和版图绘制等步骤都需要较为详细的讲解，因此决定采用博客的形式进行设计实例的分享。

本文是带隙基准源设计实例的第一讲，主要给出了带隙基准源的设计指标及对应的模块架构框图。需要注意的是，此处给出的仅仅是预期指标和初步的架构框图，在后续设计过程中，我们也会根据实时的设计进展进行微调。

## 带隙基准源的设计指标

此次设计的带隙基准源指标如下表所示，包括

| Parameter               | Symbol               | Description                                | Min | Typ | Max | Unit                    |
| :---------------------- | :------------------- | :----------------------------------------- | :-- | :-- | :-- | :---------------------- |
| Input Voltage           | $V_\mathrm{in}$      |                                            |     | 2.5 |     | $\mathrm{V}$            |
| Operating Temperature   | $T$                  |                                            | -40 |  27 |  80 | $\mathrm{^\circ C}$     |
| Quiescent Current       | $I_\mathrm{q}$       |                                            |     | 500 |     | $\mathrm{\mu A}$        |
| Power Down Current      | $I_\mathrm{pd}$      |                                            |     |   1 |  10 | $\mathrm{nA}$           |
|                         |                      |                                            |     |     |     |                         |
| Temperature Coefficient | $TC$                 |                                            |     |  20 |     | $\mathrm{ppm/^\circ C}$ |
| Output Voltage          | $V_\mathrm{out,400}$ |                                            |     | 400 |     | $\mathrm{mV}$           |
|                         | $V_\mathrm{out,800}$ |                                            |     | 800 |     | $\mathrm{mV}$           |
| Output Voltage Accuracy | $\Delta_\mathrm{v}$  | typical PVT case                           |     |   5 |     | %                       |
| Output Current          | $I_\mathrm{out,10}$  |                                            |     |  10 |     | $\mathrm{\mu A}$        |
|                         | $I_\mathrm{out,20}$  |                                            |     |  20 |     | $\mathrm{\mu A}$        |
| Output Current Accuracy | $\Delta_\mathrm{i}$  | typical PVT case                           |     |   5 |     | %                       |
|                         |                      |                                            |     |     |     |                         |
| Power Up Time           | $t_\mathrm{pu}$      | 5% $\Delta_i$ ($\Delta_v$), worst PVT case |     |   5 |  10 | $\mathrm{\mu s}$        |
| Power Down Time         | $t_\mathrm{pd}$      | 5% $\Delta_i$ ($\Delta_v$), worst PVT case |     |   5 |  10 | $\mathrm{\mu s}$        |
|                         |                      |                                            |     |     |     |                         |
| Power Supply Rejection  | $PSR_\mathrm{DC}$    | DC                                         |     |  80 |     | $\mathrm{dB}$           |
|                         | $PSR_\mathrm{1kHz}$  | 1 kHz                                      |     |  60 |     | $\mathrm{dB}$           |
|                         | $PSR_\mathrm{1MHz}$  | 1 MHz                                      |     |  40 |     | $\mathrm{dB}$           |
| Ouptut Noise (Voltage)  | $n_\mathrm{DC}$      | DC                                         |     |   1 |     | $\mathrm{nV/\sqrt{Hz}}$ |
|                         | $n_\mathrm{100kHz}$  | 100 kHz                                    |     | 0.5 |     | $\mathrm{nV/\sqrt{Hz}}$ |
|                         | $n_\mathrm{10MHz}$   | 10 MHz                                     |     | 0.1 |     | $\mathrm{nV/\sqrt{Hz}}$ |
| Ouptut Noise (Current)  | $n_\mathrm{DC}$      | DC                                         |     |  20 |     | $\mathrm{pA/\sqrt{Hz}}$ |
|                         | $n_\mathrm{100kHz}$  | 100 kHz                                    |     |  10 |     | $\mathrm{pA/\sqrt{Hz}}$ |
|                         | $n_\mathrm{10MHz}$   | 10 MHz                                     |     |   2 |     | $\mathrm{pA/\sqrt{Hz}}$ |
