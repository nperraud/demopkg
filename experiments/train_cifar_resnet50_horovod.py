from demopkg.dataset import load_cifar100
from torch.utils.data import DataLoader
from demopkg.model import CNN2D
from torchvision.models import resnet50
import matplotlib.pyplot as plt

import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping, LearningRateMonitor, ModelCheckpoint
from pathlib import Path
from pytorch_lightning.loggers import WandbLogger
# output directory
from demopkg.conf import OUTPUTDIR
from demopkg.lightning import LightningClassifier


batch_size = 128
num_epochs = 50
learning_rate = 1e-3

num_classes = 100

input_channel = 3
convs = [32, 64, 128, num_classes]
n_convs = len(convs)
kernel_sizes = [5]*n_convs
strides = [2]*n_convs

net = resnet50(num_classes=num_classes)
model = LightningClassifier(net, lr_rate=learning_rate)

# load data
train, val, test = load_cifar100()
train_loader = DataLoader(train, batch_size=batch_size)
val_loader = DataLoader(val, batch_size=batch_size)
test_loader = DataLoader(test, batch_size=batch_size)

name = 'cifar100-cnn2d'

# 1. Wandb Logger
wandb_logger = WandbLogger(offline=True) # add project='projectname' to log to a specific project

# 2. Learning Rate Logger
lr_logger = LearningRateMonitor()
# 3. Set Early Stopping
early_stopping = EarlyStopping('val_loss', mode='min', patience=5)
# 4. saves checkpoints to 'model_path' whenever 'val_loss' has a new min
checkpoint_callback = ModelCheckpoint(dirpath=OUTPUTDIR / Path(name), filename='{name}_{epoch}-{val_loss:.2f}',
                                      monitor='val_loss', mode='min', save_top_k=5)

default_root_dir=OUTPUTDIR/Path(name)
default_root_dir.mkdir(parents=True, exist_ok=True)
callbacks=[lr_logger, early_stopping, checkpoint_callback]

# Training with two GPUs
trainer = pl.Trainer(max_epochs=num_epochs,logger=wandb_logger, callbacks=callbacks, 
                     default_root_dir=default_root_dir, accelerator='gpu', devices=2)
trainer.fit(model, train_dataloaders=train_loader, val_dataloaders=val_loader)