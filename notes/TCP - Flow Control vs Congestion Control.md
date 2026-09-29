A fundamental conceptual distinction in computer networking is the difference between Flow Control and Congestion Control[cite: 1].

| Dimension               | Flow Control                                                                 | Congestion Control                                                                      |
| :---------------------- | :--------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **Primary Goal**        | Prevents the sender from overwhelming a **slow receiver's** buffer[cite: 1]. | Prevents all competing senders from overwhelming the **network core routers**[cite: 1]. |
| **Bottleneck Location** | Destination Host Receive Memory Buffer[cite: 1].                             | Intermediate Router Output Queue Buffers[cite: 1].                                      |
| **Mechanism**           | Receiver-driven via advertised window (`rwnd`)[cite: 1].                     | Sender-driven dynamic window adjustment (`cwnd`) based on loss/ACKs[cite: 1].           |
| **Feedback Form**       | Explicit metric in the 16-bit TCP header window field[cite: 1].              | Implicit inference (packet loss, timeouts, duplicate ACKs)[cite: 1].                    |

> [!theorem] Effective Sender Window Size Invariant
> The actual maximum volume of unacknowledged data a TCP sender is permitted to transmit into the network is strictly governed by the minimum of the congestion window and the receiver window:
> $$\text{Sender Window Size} = \min(\text{cwnd}, \text{rwnd})$$[cite: 1]
> * When $\text{cwnd} < \text{rwnd}$: The network core is the bottleneck (Congestion limited)[cite: 1].
> * When $\text{rwnd} < \text{cwnd}$: The receiver host buffer is the bottleneck (Flow control limited)[cite: 1].
> * By default, in standard analytical problem-solving, the receiver window is assumed to be large ($\text{rwnd} \to \infty$) unless specified otherwise, making `cwnd` the sole bottleneck[cite: 1].
