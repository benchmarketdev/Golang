# Fabric Genesis Block

This genesis block is used to bootstrap the ordering `system` channel, which the orderers use to authorize and orchestrate creation of other channels. 

By default, the channel ID encoded into the genesis block by `configtxgen` will be `testchainid`. It is recommended that you modify this identifier to something which will be globally unique.

## How to Inspect Genesis Block

