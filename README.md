# SOLAR-CHALLENGE-WEEK1

This repository contains the code and resources for the Solar Challenge Week 1 project.

---

## Environment Setup

Follow these steps to reproduce the development environment:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AshenafiTech/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

Run tests to verify your setup:

```bash
pytest tests/
```

---

## Usage

- Python scripts are located in the `scripts/` directory.
- Jupyter notebooks are located in the `src/notebooks/` directory.
- Modify and run files as needed.

---

## Continuous Integration

GitHub Actions workflows are set up under `.github/workflows/` for automated testing and other CI/CD tasks.

---