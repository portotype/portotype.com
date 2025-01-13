# Intercom for Payments

## What

A library which you install on the FE and BE, that lets you customize subscriptions and payments flows in a low-code manner.

## Why

## For SaaS products, building pricing solutions is hard.  
- For any startup, you have to have plans, synchronize them with your payment or subscription solution, manage usage, upgrades, downgrades, upgrade flows.
- It's even harder to manage them over time, upgrading the system, doing AB testing, nudging users to it.

It costs a lot of money in engineering time, and so a solution is valuable. It is also sticky. 

## how

- ship a FE library that works like Intercom. You add 2 lines of code, once, and this code can show buttons for paid users, hide existing buttons for non-paid users, style them, show a component for pricing, display warnings to the user. The FE component can also account for the number of actions a certain user did.
- ship a BE component that ensures that users aren't bypassing the FE and sending direct actions to the BE. The BE component can also account for the number of actions that a user did.
- ship a back-office where users can create plans, with limits etc, and say which actions or buttons get limited by which plans. These can be actions in the FE or actions in the BE.

## business model

Pay for the usage of this software!
