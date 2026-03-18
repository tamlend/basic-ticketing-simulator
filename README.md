# Basic SOC Ticketing Simulator

Simple interactive Python tool to simulate core SOC analyst workflows: creating SIEM alerts as tickets, triaging (assign/severity), resolving with notes, viewing details, and cancelling bad inputs.

## Features
- Create tickets from simulated SIEM alerts
- Assign tickets to analysts
- Close tickets with resolution notes
- View full ticket details (including notes)
- List overview with status, severity, assignee, and note count
- Cancel ticket creation at any step ('back')
- Input validation & user-friendly prompts

## Skills Demonstrated
- Incident lifecycle management
- Basic triage and resolution workflow
- Python scripting for SOC tooling
- User experience considerations (cancel flow, validation)

## How to Run
1. Clone the repo: `git clone https://github.com/tamlend/basic-ticketing-simulator.git`
2. Navigate: `cd basic-ticketing-simulator`
3. Run: `py ticketing_sim.py` (or `python ticketing_sim.py`)

## Screenshots

### 1. Main Menu
![Main Menu](screenshots/Screenshot%202026-03-18%20141159.png)

### 2. Creating a Ticket
![Create Ticket - Description](screenshots/Screenshot%202026-03-18%20141254.png)

### 3. Severity Selection & Validation
![Severity Input](screenshots/Screenshot%202026-03-18%20141352.png)

### 4. Ticket List with Status & Notes
![Ticket List](screenshots/Screenshot%202026-03-18%20141444.png)

### 5. Full Ticket Details View
![Ticket Details with Notes](screenshots/Screenshot%202026-03-18%20141509.png)

### 6. Error Handling
![Error Handling](screenshots/Screenshot%202026-03-18%20141414.png)
