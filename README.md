# A Benchmark and Asymmetrical-Similarity Learning for Practical Image Copy Detection (AAAI 2023)

## The proposed NDEC dataset

![image](https://github.com/WangWenhao0716/ASL/blob/main/NDEC.png)

**Training set**

[The 100,000 negative pairs](https://drive.google.com/file/d/1Cc_8yj2vhKTA8aRROMUavp9zUkI72Cgm/view) 

The original 100,000 training images from ISC2021: Please refer to [Meta AI download page](https://ai.facebook.com/datasets/disc21-dataset/)

**Reference set**

The original 100,000 reference images from ISC2021: Please refer to [Meta AI download page](https://ai.facebook.com/datasets/disc21-dataset/)

**Query set**

[The collected 49,252 query images](https://huggingface.co/datasets/WenhaoWang/ASL/resolve/main/query_images_h5.tar)

**Groudtruth**

[The groundtruth file for the query set](https://drive.google.com/file/d/1ZrPNoa3mTAxl6lViVjNtN90i20VSuzJs/view?usp=share_link)


## ASL 

![image](https://github.com/WangWenhao0716/ASL/blob/main/ASL.png)

**Step 1**

Please first review the code of two baselines in our paper from [D^2LV](https://github.com/WangWenhao0716/ISC-Track1-Submission) and [BoT](https://github.com/WangWenhao0716/ISC-Track2-Submission).

**Step 2**

Please refer to the ```train.py``` for the norm-ratio based loss.

**Step 3**

Please integrate  the ```train.py``` into the training code of Step 1.

**Step 4**

Please refer to the ```test.py``` to find our how we perform testing.

**Step 5**

Please integrate the ```test.py``` into the test code of Step 1.

**Step 6 (Optional)**

You can also integrate ```train.py``` and ```test.py``` to other baselines, such as [EsViTp](https://github.com/sun-xl/ISC2021), [CNNCL](https://github.com/lyakaap/ISC21-Descriptor-Track-1st), and [EfNet](https://github.com/socom20/facebook-image-similarity-challenge-2021).


## Citation

If you use the proposed dataset or find the ASL helpful, please cite our work:
```
@inproceedings{wang2023benchmark,
  title={A benchmark and asymmetrical-similarity learning for practical image copy detection},
  author={Wang, Wenhao and Sun, Yifan and Yang, Yi},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={37},
  number={3},
  pages={2672--2679},
  year={2023}
}
```

Our work is mainly based on our two former competition (ISC2021) winner solutions:

```
@article{wang2021d,
  title={D\^{} 2LV: A Data-Driven and Local-Verification Approach for Image Copy Detection},
  author={Wang, Wenhao and Sun, Yifan and Zhang, Weipu and Yang, Yi},
  journal={arXiv preprint arXiv:2111.07090},
  year={2021}
}
```
```
@article{wang2021bag,
  title={Bag of Tricks and A Strong baseline for Image Copy Detection},
  author={Wang, Wenhao and Zhang, Weipu and Sun, Yifan and Yang, Yi},
  journal={arXiv preprint arXiv:2111.08004},
  year={2021}
}
```
The ISC2021 competition conclusion:
```

@InProceedings{pmlr-v176-papakipos22a,
  title = 	 {Results and findings of the 2021 Image Similarity Challenge},
  author =       {Papakipos, Zo\"e and Tolias, Giorgos and Jenicek, Tomas and Pizzi, Ed and Yokoo, Shuhei and Wang, Wenhao and Sun, Yifan and Zhang, Weipu and Yang, Yi and Addicam, Sanjay and Papadakis, Sergio Manuel and Ferrer, Cristian Canton and Chum, Ond{\v{r}}ej and Douze, Matthijs},
  booktitle = 	 {Proceedings of the NeurIPS 2021 Competitions and Demonstrations Track},
  pages = 	 {1--12},
  year = 	 {2022},
  editor = 	 {Kiela, Douwe and Ciccone, Marco and Caputo, Barbara},
  volume = 	 {176},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {06--14 Dec},
  publisher =    {PMLR},
  pdf = 	 {https://proceedings.mlr.press/v176/papakipos22a/papakipos22a.pdf},
  url = 	 {https://proceedings.mlr.press/v176/papakipos22a.html},
}
```
