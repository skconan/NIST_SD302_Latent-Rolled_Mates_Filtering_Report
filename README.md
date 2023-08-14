# <div align="center"> NIST SD302: Data Exploration and Filtering </div>

[NIST Special Database 302](https://www.nist.gov/itl/iad/image-group/nist-special-database-302) has been split into several parts from SD302a to SD302i. we use only NIST SD302b and NIST SD302h. 

## <div align="center"> Data Exploration </div>

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
                    


## <div align="center"> Data Filtering </div>


In [data_filter.ipynb](), We perform filtering on latent fingerprint images from NIST SD302h using finger position labels from `finger_positions.csv`, considering corresponding mates present in NIST SD302b (devices: U and V)


## <div align="center"> Convert LFFS files to Images </div>

The LFFS format includes Field Number `13.999`, indicating a LATENT FRICTION RIDGE IMAGE. We read LFFS files starting from `13.999` until `IEND` flag. These contents are passed into an `io.BytesIO` object created from the encoded image's bytes. We utilize `Image.open` from the PIL library to open and save the image into files. The source code for this process is available in [ffs_to_image.py]().


## <div align="center">Refrence</div>
    
- [Data Format for the Interchange of Fingerprint, Facial & Other Biometric Information ANSI/NIST-ITL 1-2011 NIST Special Publication 500-290 Edition 3](https://www.nist.gov/publications/data-format-interchange-fingerprint-facial-other-biometric-information-ansinist-itl-1-1)

- [Special Publication (NIST SP) - 500-290e3](https://doi.org/10.6028/NIST.SP.500-290e3)

    - [NIST.SP.500-290e3.pdf] (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.500-290e3.pdf)

- [SYNTHETIC LATENT FINGERPRINT GENERATOR](https://arxiv.org/abs/2208.13811)


## <div align="center">Citing SFP</div>

If you are utilizing the source code from this repository in your research, please reference the following.


<br/>

## <div align="center">Contact</div>

If you have any questions or need assistance, reach us at supakit.kr@gmail.com.

