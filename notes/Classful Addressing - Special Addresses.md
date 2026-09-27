> [!theorem] Special In-Block Reserved Addresses
> Within any network block, two addresses cannot be assigned to regular hosts:
> 1. **Network Address (Network ID)**: The very first IP address in the block, obtained by setting **all host ID bits to 0**.
>    * Used by routers in routing tables to navigate packets to the target network.
> 2. **Direct Broadcast Address (DBA)**: The very last IP address in the block, obtained by setting **all host ID bits to 1**.
>    * Used to deliver a packet simultaneously to every host inside that specific network block.

> [!formula] Usable Host Addresses Formula
> For a network allocated $h$ host ID bits:
> $$\text{Total Addresses} = 2^h$$
> $$\text{Usable Host Addresses} = 2^h - 2$$
> The two subtracted addresses correspond to the Network ID and the Direct Broadcast Address.

> [!definition] Limited Broadcast Address
> An address with all 32 bits set to `1` (`255.255.255.255`).
> * Used by a local node to broadcast a message strictly to hosts residing on its own physical local link.
> * Routers block and never forward limited broadcast packets across network boundaries.
