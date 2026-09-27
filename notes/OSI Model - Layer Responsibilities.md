> [!revision] Revision
> The **Open Systems Interconnection (OSI) Reference Model** is a 7-layer theoretical framework established by the ISO to enable interoperability across heterogeneous computing systems[cite: 1, 2]. Data units scale down from messages to segments, packets, frames, and bits across the physical transmission medium[cite: 2].

| Layer                  | Protocol Data Unit (PDU) | Primary Responsibilities & Keywords                                                                                        | Key Protocols / Mechanisms                   |
| :--------------------- | :----------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------- |
| **7. Application**     | Data / Message           | User interface, network access APIs, virtual terminal[cite: 1, 2]                                                          | HTTP, SMTP, FTP, DNS, Telnet[cite: 2]        |
| **6. Presentation**    | Data                     | Syntax/semantics translation, data compression, encryption/decryption[cite: 1, 2]                                          | SSL/TLS, ASCII, EBCDIC, MIME[cite: 2]        |
| **5. Session**         | Data                     | **Dialog control** (simplex/half-duplex/full-duplex), **token management**, **synchronization check-pointing**[cite: 1, 2] | NetBIOS, RPC, PPTP                           |
| **4. Transport**       | Segment                  | **End-to-end / Process-to-process delivery**, service point addressing (ports), flow control, error control[cite: 1, 2]    | TCP, UDP, SCTP[cite: 2]                      |
| **3. Network**         | Packet / Datagram        | **Host-to-host connectivity**, logical addressing (IP), routing, forwarding, fragmentation[cite: 2]                        | IPv4, IPv6, ICMP, OSPF, RIP[cite: 2]         |
| **2. Data Link (DLL)** | Frame                    | **Hop-to-hop / Node-to-node framing**, physical addressing (MAC), flow/error control, access control[cite: 2]              | Ethernet (IEEE 802.3), PPP, CSMA/CD[cite: 2] |
| **1. Physical**        | Bit stream               | Physical medium specs (electrical/optical), bit timing, bit rate control, transmission mode[cite: 2]                       | Manchester encoding, RJ-45, V.35[cite: 2]    |
coordinates transmission of bit-stream over physical medium, including representation of bits: to be transmitted, bits must be encoded into signals - electrical or optical; P.L. defines type of encoding how Os and 1s are changed to signals (e.g. 1 = +1V, 0 = -1V) bit length – data rate: P.L. defines how long a bit lasts and, accordingly, number of bits sent each second (different values for copper wire, coaxial cable, fiber-optics, ...

raming: The D.L.L divides the stream of bits received from the network layer into manageable data units called frames. physical addressing: The D.L.L adds a header to the frame to specify the NIC address of appropriate receiver on the other side (of wire). error control: The D.L.L adds reliability to the physical layer by adding a trailer with information necessary to detect / recover damaged or lost frames. access control. When two or more devices are connected to the same link, the D.L.L determines which device has control over the link at any given time.

Network Layer logical addressing: The physical addressing implemented by the data link layer handles the addressing / delivery problem locally - over a single wire. If a packet passes the network boundary another addressing system is needed to help distinguish between the source and destination network. routing: The N.L. provides the mechanism for routing/switching packets to their final destination, along the optimal path – across a large internetwork. fragmentation and reassembly: The N.L. sends messages down to the D.L.L. for transmission. Some D.L.L. technologies have limits on the length of messages that can be sent. If the packet that the N.L. wants to send is too large, the N.L. must split the packet up, send each piece to the D.L.L, and then have pieces reassembled once they arrive at the N.L. on the destination machine
Network Layer While the data link layer oversees the delivery of packets between two devices on the same network, the network layer is responsible for the source-to-destination delivery of packet across multiple networks / links

Transport Layer port addressing: Computers often run several processes at the same time. For this reason, process-to-process delivery means delivery not only from one computer to the other but also from a specific process on one computer to a specific process on the other. The transport layer header therefore must include a type of address called a port address. segmentation and reassembly: A message is divided into segments, each segment containing a sequence number. These numbers enable the transport layer to reassemble the message correctly upon arrival at the destination, and to identify and replace packets that were lost in the transmission. flow & error control: Flow & error control at this layer are performed end-to-end rather than across a single link.

he transport layer is responsible for process-to-process delivery of entire message. While the network layer gets each packet to the correct computer, the transport layer gets the entire message to the correct process on that computer.
> [!revision] Revision
> For a path with $K$ intermediate Layer-3 routers between Source and Destination:
> $$\text{Total Network Layer Visits} = K + 2$$
> $$\text{Total Data Link Layer Visits} = 2K + 2$$

> [!trap]
> Never confuse **Node-to-Node** delivery (responsibility of Layer 2 / DLL) with **Host-to-Host** delivery (Layer 3 / Network) and **Process-to-Process / End-to-End** delivery (Layer 4 / Transport)[cite: 1, 2]. Also, intermediate forwarding nodes (routers) only traverse up to Layer 3; they do not open TCP/UDP segments unless running transparent application gateways or NAT[cite: 1].

> [!question]
> **Q:** An application sends a message from Source host $S$ to Destination host $D$ passing through 2 intermediate Layer-3 routers ($R_1$ and $R_2$). How many times will the packet visit the Network Layer and Data Link Layer, respectively?  
> (A) Network Layer: 4, Data Link Layer: 4  
> (B) Network Layer: 2, Data Link Layer: 6  
> (C) Network Layer: 4, Data Link Layer: 6  
> (D) Network Layer: 3, Data Link Layer: 4  
>
> **Answer:** **(C)**  
> **Explanation:**  
> Using $K = 2$:  
> - $\text{Network Layer Visits} = K + 2 = 2 + 2 = 4$ (Source, $R_1$, $R_2$, Destination)[cite: 1].  
> - $\text{Data Link Layer Visits} = 2K + 2 = 2(2) + 2 = 6$ (Source outbound, $R_1$ in, $R_1$ out, $R_2$ in, $R_2$ out, Destination inbound)[cite: 1].
