import torch
import torch.nn as nn

###MC1
data_mc1 = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
print(softmax_function(data_mc1))
#tensor([0.0900, 0.2447, 0.6652]) - c)

###MC2
#es1: tensor([0.0900, 0.2447, 0.6652]) - c)

#MC3
#es1: tensor([0., 0., nan]) - c)

#MC4
#es1: tensor([0.0900, 0.2447, 0.6652]) - b)

#MC5
#es2: - a)

#MC6
#es2: - b)

#MC7
#es2: - a)

#MC8
#es2: - c)

#MC9
#es3: - b)

#MC10
#es3: - b)

#MC11
#es4: - a)

#MC11
#es4: - d)