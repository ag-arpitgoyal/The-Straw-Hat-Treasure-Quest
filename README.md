# The Straw Hat Treasure Quest

## Overview

The **Straw Hat Treasure Quest** is a Python-based treasure management system designed to efficiently handle and track treasures assigned to a crew. Inspired by themes of adventure and exploration, this project demonstrates the use of object-oriented programming and data structures to manage treasures and crew members dynamically.

## Features

- **CrewMate Management**: Manage crew members who can carry treasures, keeping track of their load and assigned treasures.
- **Treasure Tracking**: Each treasure has a unique ID, size, arrival time, and completion time, allowing for organized management.
- **Heap-Based Load Balancing**: The system utilizes a heap to assign treasures to crewmates based on their current load, optimizing resource distribution.
- **Dynamic Updates**: Treasures can be added or reassigned as needed, allowing for flexible management of the treasury.

## Project Structure

The project consists of the following key components:

1. **CrewMate Class** (`crewmate.py`):
   - Represents a crew member with attributes for load and a list of assigned treasures.

2. **Treasure Class** (`treasure.py`):
   - Represents individual treasures with attributes like ID, size, arrival time, and completion time.

3. **StrawHatTreasury Class** (`strawhat_treasury.py`):
   - Manages the overall treasure collection, crewmates, and related functionalities, including adding treasures and calculating completion times.

4. **Heap Management** (`heap.py`):
   - Implements a heap structure to prioritize crewmates based on their load when assigning treasures.

5. **Main Script** (`main.py`):
   - A test script for running and debugging the treasury management system.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ag-arpitgoyal/The-Straw-Hat-Treasure-Quest.git
   cd The-Straw-Hat-Treasure-Quest
