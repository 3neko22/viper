#!/bin/bash
#SBATCH --job-name=PROBA_ENEKO
#SBATCH -D ..
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=12GB
#SBATCH --gres=gpu:1
#SBATCH --output=slurm_output.out
#SBATCH --error=slurm_output.err
#SBATCH --mail-type=all
#SBATCH --mail-user=eamor002@ikasle.ehu.eus

source /gaueko0/users/eamor002/venvs/Tximista_GPT/bin/activate

srun python probak.py