##################################################
# Training Config
##################################################
workers = 1                 # number of Dataloader workers
epochs = 150                # number of epochs
batch_size = 12             # batch size
learning_rate = 1e-3        # initial learning rate

##################################################
# Model Config
##################################################
image_size = (448, 448)     # size of training images
net = 'resnet101'  # feature extractor
num_attentions = 32     # number of attention maps
beta = 5e-2                 # param for update feature centers

##################################################
# Loss Config
##################################################
use_arcface = True          # whether to use ArcFace loss instead of cross-entropy
arcface_s = 64.0           # scale parameter for ArcFace
arcface_m = 0.5            # margin parameter for ArcFace
arcface_loss_type = 'arcface'  # 'arcface', 'sphereface', or 'cosface'

##################################################
# Memory Optimization Config
##################################################
use_gradient_checkpointing = True  # Use gradient checkpointing to save memory (trades memory for compute time)

##################################################
# Dataset/Path Config
##################################################
tag = 'ndtwin'                # 'aircraft', 'bird', 'car', or 'dog'

# saving directory of .ckpt models
save_dir = './ND_TWIN/wsdan-resnet101-cal/'
model_name = 'model.ckpt'
log_name = 'train.log'

# checkpoint model for resume training
ckpt = False
# ckpt = save_dir + model_name