import wandb 

print(f"the version of wandb is : {wandb.__version__}")

assert wandb.__version__ == '0.17.5', f'expected 0.17.5, but got a different version: {wandb.__version__}'
