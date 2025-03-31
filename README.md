# Modeling B-cell Affinity Maturation and Clonal Selection

This repository contains the code, data, and documentation for the mathematical modeling work presented in:

### Phased epigenetic fragility and stability accelerate the genetic evolution of B-cells

#### Auther names Mark Y Xiang 1,2,3,†, Haripriya Vaidehi Narayanan 1,2,†, Vaibhava Kesarwani 1, Tiffany Wang 1, Alexander Hoffmann 1,2,*
#### Affiliations: 1. Institute for Quantitative and Computational Biosciences, 2. Department of Microbiology, Immunology, and Molecular Genetics, 3. 3Bioinformatics Interdepartmental Program, University of California Los Angeles; Los Angeles, California 90095, USA, † These authors contributed equally to this work, * Corresponding author. Email: ahoffmann@ucla.edu.

# Overview

This study investigates the fundamental question of how epigenetic heterogeneity of B-cells affects the genetic evolution of high affinity antibody required for effective immune responses.

We developed a probabilistic, agent-based model to simulate:
* Affinity-based selection in the light zone
* Proliferation and somatic hypermutation in the dark zone
* The impact of fragility and stability of the epigenetic cell state on affinity maturation

# Geeting Started

## Clone the repository:
```bash
git clone https://github.com/signalingsystemslab/GC_evolution_model.git
cd GC_evolution_model
```

## Install dependencies:
It is recommended to use a virtual environment
```bash
python3 - m venv venv
source venv/bin/activate
pip install - r requirements.txt
```

## Run a basic simulation:
Generate simulations regarding Figure 1 results
```bash
bash Model_simulation/Simulation_Fig1.sh
```

Generate simulations regarding Figure 2 and 3 results
```bash
bash Model_simulation/Simulation_Fig23.sh
```

Generate simulations regarding Figure 4 results
```bash
bash Model_simulation/Simulation_Fig4.sh
```

# Acknowledgements

#### We thank the members of the Hoffmann lab for valuable discussions and feedback on the manuscript, particularly Helen Huang, Chengyuan Li, Xiaolu Guo, Patrick Yuan, and Joseph Schirle as well as Roy Wollman and Eric Deeds for critical feedback and/or review of our manuscript.

# Contact

For questions or suggestions, feel free to open an issue or contact

#### Mark Xiang - markxiang@g.ucla.edu





