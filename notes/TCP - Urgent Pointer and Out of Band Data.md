> [!definition] Urgent Data Mechanism
> The Urgent Pointer provides a mechanism for sending interrupt-driven priority signals (such as `Ctrl+C` abort commands in Telnet/SSH)[cite: 1].
> * When $\text{URG} = 1$, TCP places the urgent data at the very beginning of the segment payload[cite: 1].
> * The Urgent Pointer specifies the byte offset where the urgent payload ends and regular data begins[cite: 1]:
>   $$\text{Urgent Data End Byte} = \text{Segment Sequence Number} + \text{Urgent Pointer}$$[cite: 1]
> * TCP does not provide true out-of-band delivery; urgent data is multiplexed in-line with the existing segment stream[cite: 1].
