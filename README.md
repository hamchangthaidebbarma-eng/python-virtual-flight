# Python Virtual Flight

A small PySimVerse drone mission that connects to a virtual drone, performs a
square flight pattern, rotates in place, and lands.

## Project files

| File | Purpose |
| --- | --- |
| `flight_mission.py` | Runs the complete virtual-drone mission |
| `requirements.txt` | Python dependency required by the mission |
| `pyproject.toml` | Basic project metadata and tool configuration |

## Requirements

- Python 3.9 or newer
- A PySimVerse installation and a running PySimVerse-compatible simulator
- PySimVerse `0.14` (installed by the project requirements)

Install the dependency in a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Then install the project requirements:

```bash
python -m pip install -r requirements.txt
```

The mission uses PySimVerse's ZeroMQ drone interface. By default it binds the
command publisher to port `5550` and connects to state/video streams on ports
`5556` and `5557`. Override these endpoints when starting the mission:

```powershell
$env:PYSIMVERSE_HOST = "*"
$env:PYSIMVERSE_COMMAND_PORT = "5550"
$env:PYSIMVERSE_STATE_PORT = "5556"
$env:PYSIMVERSE_VIDEO_PORT = "5557"
python flight_mission.py
```

## Run the mission

```bash
python flight_mission.py
```

The mission connects to the simulator, takes off, flies forward/right/backward/left,
rotates 90 degrees, and lands. The movement distance passed to PySimVerse is
`100` for each leg.

## Development

Keep simulator-specific behavior in `flight_mission.py` and run the file from
the repository root so the local environment and installed dependencies are
resolved consistently.
