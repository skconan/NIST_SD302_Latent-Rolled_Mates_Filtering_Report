# NIST SD302: Data Exploration and Cleaning

[NIST Special Database 302](https://www.nist.gov/itl/iad/image-group/nist-special-database-302) has been split into several parts from SD302a to SD302i. we use only NIST SD302b and NIST SD302h. 

### NIST SD302b

The SD 302b directory structure is organized as follows:

    images
        - baseline                   # Collection type. Contain device code R, S, U, and V.
            - R                      # Device code
                - 1000               # Resolution
                    - slap           # Impression type
                        - png        # Image format
                    - slap-segmented
                        - ...
                - 500
                    - ...
            - ...

<br/>

<b> 
Count the subjects for each device. </b>

We explore the subject in the database by counting the subject or person by uisng [count_person.py](https://gitlab.com/ksip/nist_sd302/-/blob/fe7f09e732095130cab32e599f9189dc2abe554d/src/count_person.py)

Image names are in the form SUBJECT_ACTIVITY_HAND_ENCOUNTER_TECHNIQUE_DIGITIZER_RESOLUTION_DEPTH_CHANNELS_LPNUMBER_SOURCE.EXT


<table>
    <thead>
        <td>
            Device Code
        </td>
        <td>
            Number of subjects
        </td>
    </thead>
    <tr>
        <td>
            R
        </td>
        <td>
           92
        </td>
    </tr>
    <tr>
        <td>
           S
        </td>
        <td>
          108
        </td>
    </tr>
    <tr>
        <td>
           R and S
        </td>
        <td>
          200
        </td>
    </tr>
    <tr>
        <td>
           U
        </td>
        <td>
          200
        </td>
    </tr>
    <tr>
        <td>
           V
        </td>
        <td>
          200
        </td>
    </tr>
</table>   

<br/>

### NIST SD302h


The SD 302h directory structure is organized as follows:

    ebts                        # Record format
        - latent                # Collection type
            - lffs              # Transaction type
                - original     
                    - 1000      # Resolution, in PPI
                - enhanced
                    - ...
        - checksum_latent_lffs_enhanced.csv # File checksums
        - checksum_latent_lffs_original.csv
                    


## Filtering

- WE filter the data has mate in NIST SD302u and v by using [data_cleaning.ipynb](https://gitlab.com/ksip/nist_sd302/-/blob/fe7f09e732095130cab32e599f9189dc2abe554d/notebook/data_cleaning.ipynb)


## Reading .lffs

- Refrence
    
    - [Data Format for the Interchange of Fingerprint, Facial & Other Biometric Information ANSI/NIST-ITL 1-2011 NIST Special Publication 500-290 Edition 3](https://www.nist.gov/publications/data-format-interchange-fingerprint-facial-other-biometric-information-ansinist-itl-1-1)

    - [Special Publication (NIST SP) - 500-290e3](https://doi.org/10.6028/NIST.SP.500-290e3)

- Field Number

    - 13.999 - LATENT FRICTION RIDGE IMAGE (End with "IEND")

## Filtering the rolled and latent mates

- Reference

    - [SYNTHETIC LATENT FINGERPRINT GENERATOR](https://arxiv.org/abs/2208.13811)

- The finger position annotation in the SD302h subset.

- Use only first impression

- 

ไม่ยึดชื่อไฟล์ แต่เอาชื่อไฟล์ไปเช็ค fgp จาก csv เลยปรากฏว่า อันที่ไฟล์มี X บอกเป็น unknown ใน csv มี fgp บอก เลยเลือกมาแต่ยังเกินอยู่ เลยเลือกเฉพาะ impression แรก ก้ได้พอดีเลยแล้วก็อ่านรูปจาก lffs เอาเลยก็เลยสอดคล้องกับ paper ที่ให้มี่เค้าดูแต่ 302h
