Digital Hand Atlas Downloader
=============================

Description
-----------
The Digital Hand Atlas (DHA) [1, 2] dataset consists of 1390 hand radiographs, labeled
by two radiologists with an estimated patient's age. Since this dataset is a
common choise to evaluate new machine learning models, this repository provides
a script to download the entire dataset.

```bash
git clone https://github.com/razorx89/digital-hand-atlas-downloader.git
cd digital-hand-atlas-downloader
pip install -r Requirements.txt
python download.py --output_dir <target_dir>
```

Problems
--------
Some of the image links in the [DHA System](http://ipilab.usc.edu/BAAweb/) are invalid and can be recovered by having
a look at the link text instead of the link URL. However, one image is still
missing, where both the link text and URL are invalid.

```
JPEGimages/ASIF/ASIF05/5260.jpg -> JPEGimages/ASIF/ASIF05/5262.jpg
JPEGimages/BLKF/BLKF06/7090.jpg -> JPEGimages/BLKF/BLKF06/7290.jpg
JPEGimages/BLKF/BLKF12/7144.jpg -> ???
JPEGimages/BLKM/BLKM13/7022.jpg -> JPEGimages/BLKM/BLKM13/7101.jpg
JPEGimages/CAUF/CAUF14/7126.jpg -> JPEGimages/CAUF/CAUF14/7154.jpg
JPEGimages/CAUM/CAUM12/7185.jpg -> JPEGimages/CAUM/CAUM12/7186.jpg
```

Disclaimer
----------
The repository owner is __not__ the copyright holder for the digital hand atlas
dataset. Copyright is hold by the *Image Processing and Informatics Lab, 1450 San Pablo Street, Suite 2100, Los Angeles*. This script just aims to provide an easy
access to the dataset outside the DHA System, for example for testing machine
learning models efficiently.

Licence
-------
The MIT License (MIT). Please see [License File](LICENSE) for more information.

References
----------
1. Gertych A, Zhang A, Sayre J, Pospiech-Kurkowska S, Huang H. "Bone Age Assessment of Children using a Digital Hand Atlas". Computerized medical imaging and graphics: the official journal of the Computerized Medical Imaging Society, 31(4-5), pp. 322-331, 2007.

2. Aifeng Zhang, James W. Sayre, Linda Vachon, Brent J. Liu, and H. K. Huang "Racial Differences in Growth Patterns of Children Assessed on the Basis of Bone Age".
Radiology, 250(1), pp. 228-235, 2009
