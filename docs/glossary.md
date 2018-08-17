## Glossary

Here, we clearly define the relevant terms needed to understand the preceding pipeline specification (in no particular order).

### Inputs
the minimum set of image data, data manifest and pipeline recipe, from which a pipeline can generate the desired gene expression matrix and spatial locations of transcripts and cells.

### Pipeline
a sequence of data processing steps to process the inputs into the desired outputs.

### Pipeline Component
a single data processing step in the pipeline, as defined by its input and output file formats, e.g., the spot-detection component takes as input an image and outputs a table of spot locations, shapes, and intensities.

### Pipeline Component Algorithm
a specific algorithm type that adheres to the specified input and output file formats required by the component it belongs to. For example, a spot-detection component algorithm can be realized as a Gaussian blob detector or a connected components labeller. Both find spots and accept the same inputs and produce the same outputs, hence belong to the same component. However, the underlying properties of the algorithms (and parameterizations) may be quite different.

### Pipeline Specification
a document describing the above terms in detail, i.e., this document.

### Pipeline Implementation
actual code for the pipeline. This code will be packaged as a well-documented Python library and corresponding command line tool for use by consortium members to facilitate easy sharing and comparison of results across labs/methods.

### Manifest
The data manifest is a file that includes necessary information about the hybridization images, auxiliary images, and codebook. The SpaceTx manifest format is described in detail abovebelow.

### Image Tile
a single plane, single channel 2D image. In the manifest, each tile has information about it’s (X,Y,Z) coordinates in space, and information about which hybridization round (H) and/or fluorescence channel (C) it was acquired under.

### Field of View (FOV)
a collection of Iimage Tiles corresponding to a specific volume or plane of the sample, under which the signal for all color channels and all hybridization rounds were acquired. All tiles within this FOV are the same size, but the manifest allows for different spatial coordinates for different hybridization rounds or channels (to accommodate slight movement between rounds, for example).

### Hybridization Images
The hybridization image data for an experiment, including any form of fluorescence readout.

### Auxiliary Images
Any user-submitted additional images for analysis beyond the hybridization images. These images may be of lower dimension than the hybridization images (e.g., single color channel images), but should span the same spatial extent as the hybridization images acquired under the same FOV.

Examples of such data may include:
Nuclei (DAPI or similar nuclear stain): this required image shows cell nuclei and is crucial for cell segmentation further on down the pipeline.

Other stains or labels: these optional (but recommended) image(s), including but not limited to antibody stains, may capture additional information about cell boundaries or subcellular structure that will be useful for cell segmentation and/or additional spatial analyses.

### Registration
refers to the process of aligning multiple images of the same spatial location, most commonly across multiple rounds of hybridization within a FOV.

### Stitching
the process of combining images from multiple fields of view into a larger image that spans the extent of the sample.