##!/bin/bash

#SBATCH --time=60
#SBATCH -c 16
#SBATCH --output=ex.log
#SBATCH --gres=gpu:1
#SBATCH -p gpu

module purge
module load PyTorch/1.12.1-foss-2022a-CUDA-11.7.0
module load scikit-learn

# Submit job
python3 main.py