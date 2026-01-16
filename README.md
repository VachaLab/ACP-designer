# ACP-designer

<p align="center">
  <img src="./graphics/sampled_mps.png" alt="DUCKTOOLS Logo" width="150" height="150">
</p>
<p align="center">
  <img src="./graphics/RoVa_logo.png" alt="DUCKTOOLS Logo" width="150" height="150">
</p>

## Overview

**ACP-designer** is a ML-based toolbox for design of peptide-based anticancer therapeutic agents. Developed by CEITEC - [Robert Vacha group](https://vacha.ceitec.cz)

This toolbox enables rapid and cost-effective design of novel Mastoparan-like anticancer sequences. It contains simple generative model coupled with cytotoxicity filter to ensure seamless filtering for potential therapeutical candidates

---

## Features

1. **Generative model**

2. **Cytotoxicity filter**

3. **additional filters**

---

## Installation

### Local Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/karatedava/ACP-designer.git
   cd ACP-designer
   ```
2. **Install Miniconda**  
   Download and install Miniconda by following the [official Miniconda installation guide](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions).

3. **Create a Conda Environment**  
   Create and activate a Python 3.12 environment:
   ```bash
   conda create -n acp_designer python=3.12
   conda activate acp_designer
   ```
4. **Install Dependencies**  
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Web Application
No installation required! Access 'ACP-designer' full functionality via our web application:  
👉 **[Web App](https://peptide-predictor.cloud.e-infra.cz)**
Unfortunatelly only possible within Masaryk University intranet. Accessibility to the 'outside world' will be provided after security risk will be resolved

---

## Running ACP_designer (Local Installation)

**Generation of new ACPs**
   ```bash
   python run_cli.py --id 01 --nbatch 100
   ```

**Generation of new ACPs + mutation of desired sequence**
   ```bash
   python run_cli.py --id 01 --nbatch 100 --mutate INWKGIAAMAKKLL
   ```

### Command-Line Parameters
Customize runs with these parameters:

| Parameter       | Description                                              | Options/Default                     |
|-----------------|----------------------------------------------------------|-------------------------------------|
| `--id`   | run id to mark each run uniquely           | integer value, always required |
| `--nbatch`        | controls amount of generated peptides               | `100` (default)                     |
| `--device`      | device                              | `config_safe` (default)             |
| `--mutate`          | sequnce to mutate                                  | string of amino acids |

---

## Future Plans
*Work in progress!*  