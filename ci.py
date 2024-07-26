import wandb 

print(f"the version of wandb is : {wandb.__version__}")

assert wandb.__version__ == '2.1.01', f'expected 2.1.01, but got a different version: {wandb.__version__}'
