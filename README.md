# ImageFrequency

## Motivarion

Radiomics is a method that extracts features from medical images using data-characterization algorithms (Gillies et al., 2016). Radiomics have been developed based on the concept that medical images contain information that reflects underlying pathophysiology (Gillies et al., 2016). To derive the radiomic feature from a medical image, intensity levels, texture heterogeneity patterns, and shape of the lesion (Lambin et al., 2012). The potential of radiomics has been shown across multiple tumor types, including the brain, head and neck, cervix, and lung cancer tumors. Radiomic features extracted from MRI, PET, or CT images, were associated with several clinical outcomes, and hence, potentially provide complementary information for decision support in clinical practice (van Griethuysen et al., 2017). However, the character of the lesion is affected by the surrounding tissue. A lesion on the medical image should be characterized by the interrelation between the lesion and surrounding tissue as well as the property of the lesion itself (Lambin et al., 2012; Janiszewska, 2020; Hobbs et al., 2003). We introduce a new radiomics feature that quantitatively analyzes the interrelation between lesions and surrounding tissue focusing on the value change of rows and columns in a medical image.

## Method

Image frequency is obtained by applying Fourier analysis to the arraya of correlation coefficients calculated from adjacent columns or rows. First, we calculate the correlatio coefficients between adjacent rows or columns, and obtai array of correlation coefficients.

$X_{ij}$ denotes the pixel value of $i$-th row and $j$-th column in a $m\times n$ medical image $(1\le i\le m, 1\le j\le n)$. For simplicity, we assume a medical image is a gray-scale image and $X_{ij}$ is integer in the range  $0\le X_{ij}\le 255$.


Let $r_{i,j}$ be the correlation coefficient between $i$-th and $j$-th row. Let $R_{i,j}$ be the correlation coefficient between  $i$-th and $j$-th columns. 
Image frequency is obtained by applying Fourier analysis to the array of correlation coefficients calculated from adjacent columns or rows. First, we calculate the correlation coefficients between adjacent rows or columns, and obtain array of correlation coefficients. Figure below shows the procedures to calculating the image frequencies.

<img src="https://github.com/TakumaUsuzaki/ImageFrequency/blob/main/bitmap.png">


$$[r_{1,2}, r_{2,3}, \cdots, r_{m-2,m-1}, r_{m-1,m}]$$

$$[R_{1,2}, R_{2,3}, \cdots, R_{n-2,n-1}, R_{n-1,n}].$$

By applying Fourier analysis to these arrays, we obtain frequency of the arrays,

$$[r_{1,2}, r_{2,3}, \cdots, r_{n-2,n-1}, r_{m-1,m}]  \xrightarrow{\textrm{Fourier analysis}} f$$

$$[R_{1,2}, R_{2,3}, \cdots, R_{n-2,n-1}, R_{n-1,n}] \xrightarrow{\textrm{Fourier analysis}} F.$$

## Example & Test

As an example, we use a lung nodule image on CT. 

<img src="https://github.com/TakumaUsuzaki/ImageFrequency/blob/main/mal5_LIDC-IDRI-0072_6.png">


When you execute '__main__.py',
```
python __main__.py
```
you are asked the path of the input image.

```
Please input the image file path: 
```

The relative path of the test image is '../images/test.png', so you input this as following.

```
Please input the image file path: ../images/test.png
```
Then you obtain the image frequency for columns and rows.
```
Image frequency for column: 0.20392156862745098
Image frequency for row: 0.2549019607843137
```

## Citation
When you use code in this repository, please cite papers below.

[A new radiomics feature: image frequency analysis Takuma Usuzaki, Kengo Takahash, Kazuma Umemiya
arXiv 2021.11.10; doi: https://doi.org/10.48550/arXiv.2111.05855](https://arxiv.org/abs/2111.05855)

## Acknowledgement
The authors acknowledge the National Cancer Institute and the Foundation for the National Institutes of Health, and their critical role in the creation of the free publicly available LIDC/IDRI database used in this study. Data used in this research were obtained from The Cancer Imaging Archive (TCIA) sponsored by the Cancer Imaging Program, DCTD/NCI/NIH, https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI.
