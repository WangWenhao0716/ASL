# The code for filtering out the "false negative" pairs.

de = []
for i in range(len(qi)):
    q = Image.open('/path/to/query_images_h5/' + qi[i] + '.jpg')
    q = q.convert("RGB")
    q = q.resize((256,256))
    q_t = transforms(q).reshape((1,3,256,256))
    features = model.module.base(q_t.cuda())
    features = features.view(features.size(0), -1)
    features = model.module.projector_feat_bn(features)
    scale_1 = torch.norm(features)
    
    r = Image.open('/path/to/reference_images/' + ri[i] + '.jpg')
    r = r.convert("RGB")
    r = r.resize((256,256))
    r_t = transforms(r).reshape((1,3,256,256))
    features = model.module.base(r_t.cuda())
    features = features.view(features.size(0), -1)
    features = model.module.projector_feat_bn(features)
    scale_2 = torch.norm(features)
    
    if(scale_1 / scale_2 > 1):
        print(i, qi[i], score[i], scale_1/scale_2)
        de.append(i)
