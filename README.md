# SDLC-of-a-music-studio
StudioStream: Session Booking System 🎙️
StudioStream is a lightweight management solution designed for music recording studios. It streamlines the Software Development Life Cycle (SDLC) by providing a structured way to manage studio rooms, sound engineers, and client session billing.

📑 Table of Contents
SDLC Overview

System Architecture

Features

Installation

Usage

Nomenclature Guide

SDLC Overview
The development of StudioStream followed the standard six-phase Software Development Life Cycle:

Requirement Analysis: Identified the need for automated cost calculation based on room rates and staff expertise.

System Design: Modeled the relationship between physical assets (Rooms) and human capital (Engineers).

Implementation: Developed using Python, focusing on modularity and Object-Oriented Programming (OOP).

Testing: Verified mathematical logic for billing and edge cases (e.g., zero-duration sessions).

Deployment: Script-based deployment suitable for local terminal environments.

Maintenance: Designed for future extensions like equipment inventory and payment gateway integration.


Shutterstock
Explore
System Architecture
StudioStream utilizes a Class-Based Architecture to ensure data integrity and clear nomenclature.

StudioRoom: Stores room-specific metadata and base hourly rates.

SoundEngineer: Maintains staff identity and specialized labor costs.

RecordingSession: The "Controller" class that aggregates data to produce a final report.

Features
Dynamic Billing: Automatically calculates totals using the formula:

Total=(RoomRate+EngineerRate)×Hours

Session Reporting: Generates clean, human-readable summaries for clients.

Modular Design: Easily swap engineers or rooms within a single session instance.

Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/studiostream.git
Navigate to the directory:

Bash
cd studiostream
Run the application:

Bash
python main.py
Usage
The system is initialized by creating room and engineer objects, then passing them into a session object.

Python
# Create the environment
room = StudioRoom("Studio A", 100)
engineer = SoundEngineer("Jane Doe", 50)

# Book the session
session = RecordingSession("Artist Name", room, engineer, 3)
session.generate_report()
Nomenclature Guide
To maintain consistency between the design documentation and the source code, the following naming conventions must be strictly followed:

Name	Type	Description
StudioRoom	Class	The physical recording space.
SoundEngineer	Class	The technical staff member assigned.
RecordingSession	Class	The core object linking client and resources.
calculate_total_cost	Method	The primary financial logic function.
Note: This project was developed as a demonstration of SDLC principles in a Music Studio context.
