# <div align="center"> NIST SD302: Data Exploration and Filtering </div>

[NIST Special Database 302](https://www.nist.gov/itl/iad/image-group/nist-special-database-302) has been split into several parts from SD302a to SD302i. Our focus is on NIST SD302b and NIST SD302h exclusively. 

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

We explore the subject in the database by counting the subject or person by uisng [count_subject.py](https://github.com/skconan/NIST_SD302_Latent-Rolled_Mates_Filtering_Report/blob/71e280996707a3c0cc1ca7a9cad27de87b8dc166/src/count_subject.py)

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


In [data_filter.ipynb](https://github.com/skconan/NIST_SD302_Latent-Rolled_Mates_Filtering_Report/blob/71e280996707a3c0cc1ca7a9cad27de87b8dc166/notebook/data_filtering.ipynb), We perform filtering on latent fingerprint images from NIST SD302h using finger position labels from `finger_positions.csv`, considering corresponding mates present in NIST SD302b (devices: U and V)


## <div align="center"> Convert LFFS files to Images </div>

The LFFS format includes Field Number `13.999`, indicating a LATENT FRICTION RIDGE IMAGE. We read LFFS files starting from `13.999` until `IEND` flag. These contents are passed into an `io.BytesIO` object created from the encoded image's bytes. We utilize `Image.open` from the PIL library to open and save the image into files. The source code for this process is available in [lffs_to_image.py](https://github.com/skconan/NIST_SD302_Latent-Rolled_Mates_Filtering_Report/blob/71e280996707a3c0cc1ca7a9cad27de87b8dc166/src/lffs_to_image.py).


## <div align="center">Refrence</div>
    
- [Data Format for the Interchange of Fingerprint, Facial & Other Biometric Information ANSI/NIST-ITL 1-2011 NIST Special Publication 500-290 Edition 3](https://www.nist.gov/publications/data-format-interchange-fingerprint-facial-other-biometric-information-ansinist-itl-1-1)

- [Special Publication (NIST SP) - 500-290e3](https://doi.org/10.6028/NIST.SP.500-290e3)

    - [NIST.SP.500-290e3.pdf] (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.500-290e3.pdf)

- [SYNTHETIC LATENT FINGERPRINT GENERATOR](https://arxiv.org/abs/2208.13811)


## <div align="center">Citing SFP</div>

If you are using SFP or benchmarks in your research, kindly reference the following.

	@ARTICLE{10526230,
	  author={Kriangkhajorn, Supakit and Horapong, Kittipol and Areekul, Vutipong},
	  journal={IEEE Access}, 
	  title={Spectral Filter Predictor for Progressive Latent Fingerprint Restoration}, 
	  year={2024},
	  volume={12},
	  number={},
	  pages={66773-66800},
	  keywords={Fingerprint recognition;Image restoration;Friction;Frequency-domain analysis;Filtering;Image matching;Deep learning;Image restoration;Image forensics;Machine learning;Fingerprint recognition;image restoration;image enhancement;image filtering;image forensics;machine learning},
	  doi={10.1109/ACCESS.2024.3397729}}

or

	S. Kriangkhajorn, K. Horapong and V. Areekul, "Spectral Filter Predictor for Progressive Latent Fingerprint Restoration," in IEEE Access, vol. 12, pp. 66773-66800, 2024, doi: 10.1109/ACCESS.2024.3397729.

<br/>
## <div align="center">Contact</div>

If you have any questions or need assistance, reach us at supakit.kr@gmail.com.

