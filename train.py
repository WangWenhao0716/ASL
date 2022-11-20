# The realization of the norm-ratio based loss.
# We assume that the mini-batch size is 32, and there are 4 GPUs.

scales = scales.reshape((32,4))
        
loss_scale = 0
for i in range(32):
  count = 0
  while count<5:
      num = torch.randint(low=0,high=4,size=[2])
      select = scales[i][num]
      if(max(select)==min(select)):
          count = count + 1
      else:
          count = 5

  position = num + 4 * i
  feat = s_features[position]
  _, in_1 = torch.max(select,dim=0)
  _, in_2 = torch.min(select,dim=0)
  loss_scale = loss_scale + torch.exp(1-torch.norm(feat[in_1])/torch.norm(feat[in_2])) 

loss_scale = loss_scale/32
