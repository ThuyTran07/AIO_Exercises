import torch

class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()
       
    def forward(self, data):
        exps = data.exp()
        sum_exps = exps.sum()
        self.softmax = exps / sum_exps
        return self.softmax

class StableSoftmax(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, data):
        max_value = data.max()
        stable_exps = (data - max_value).exp()
        sum_exps = stable_exps.sum()
        self.stable_softmax = stable_exps / sum_exps
        return self.stable_softmax


#test
data = torch.Tensor([1, 2, 3])

softmax = Softmax()
print(softmax(data))

stable_softmax = StableSoftmax()
print(stable_softmax(data))

#mc2
data_mc2 = torch.Tensor([5, 2, 4])
softmax_mc2 = Softmax()
print(softmax(data_mc2))


#mc3
data_mc3 = torch.Tensor([1, 2, 3000])
softmax_mc3 = Softmax()
print(softmax(data_mc3))
