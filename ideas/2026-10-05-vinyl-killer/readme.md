# what it is

This idea is about physical music on a card. 

A collectible card with a music album card that actually contains the music. It is not a QR code, URL, streaming token, or ID pointing to music elsewhere.

# why

People like vinyl bc it’s a collectible and pretty.

But vinyls are too big and heavy and fragile. 

I think this can be replaced with super thin contactless cards the size of football Panini cards or baseball cards.

# how it works 

We want this to be passive in the sense of no battery or power supply. We also want the music to be stored inside.

The card has:

* Flash storage containing the actual album/audio
* No battery
* No electrical contacts
* No optical code / magnetic stripe
* 13.56 MHz inductive power harvesting — placing the card on/in the player powers it wirelessly
* MCU + BLE radio — currently nRF52840
* 2.4 GHz antenna for transmitting the audio/data to the player
* Target thickness around 0.8 mm

The player has
- two separate jobs: power the card inductively and receive the music wirelessly. The important architectural choice we landed on was that 13.56 MHz is power only; we aren’t trying to squeeze the album through NFC. BLE carries the data.

Diagram

```
             DECA AUDIO CARD
        63 × 88 mm / ~0.8 mm
┌─────────────────────────────────────┐
│                                     │
│     13.56 MHz inductive coil        │
│   ┌─────────────────────────────┐   │
│   │                             │   │
│   │   Rectifier + reservoir     │   │
│   │          │                  │   │
│   │          ▼                  │   │
│   │     Power regulation        │   │
│   │          │                  │   │
│   │          ▼                  │   │
│   │      nRF52840 MCU ───────┐  │   │
│   │          │               │  │   │
│   │          ▼               ▼  │   │
│   │    128/256 MB        2.4 GHz│   │
│   │     QSPI NOR         antenna│   │
│   │      AUDIO              │   │   │
│   │                         │   │   │
│   └─────────────────────────│───┘   │
└─────────────────────────────│───────┘
                              │
                         BLE data
                              │
                              ▼
                 DECA PLAYER / READER
┌─────────────────────────────────────┐
│                                     │
│ USB-C power                         │
│     │                               │
│     ├──► 13.56 MHz transmitter      │
│     │          │                    │
│     │       POWER                    │
│     │          │                    │
│     │          ▲                    │
│     │       [ CARD ]                │
│     │          │                    │
│     │       BLE AUDIO/DATA          │
│     │          ▼                    │
│     └──► BLE receiver               │
│              │                      │
│              ▼                      │
│        Decode / playback            │
│              │                      │
│              ▼                      │
│          DAC / amplifier            │
│              │                      │
│              ▼                      │
│           SPEAKERS                  │
│                                     │
└─────────────────────────────────────┘
```
