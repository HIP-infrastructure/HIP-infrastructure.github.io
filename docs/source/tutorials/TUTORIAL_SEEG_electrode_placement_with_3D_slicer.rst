SEEG electrode placement with 3D Slicer
---------------------------------------

.. figure:: /tutorials/art/TUTORIAL_SEEG_electrode_placement_with_3D_slicer/tutorial_3dslicer_header.png
	:width: 650px
	:align: center

	**3D visualization of SEEG electrodes.** *SEEG electrodes have been generated and placed using* :doc:`3D Slicer</applications/APP_3D_Slicer>` *.*

Disclaimer
::::::::::

The methods and software used in this tutorial have not been certified for clinical practice and should be considered for 
research purposes only.  

About this tutorial
:::::::::::::::::::

The objective of this tutorial is to guide HIP users in placing (non-rigid) SEEG electrodes on a post-implantation volume using 3D Slicer.
It primarily  consists of a video demonstration and should be viewed as an introductory tutorial because it does not go into all
the intricacies of the placement of SEEG electrodes.
For more in-depth information regarding electrode placement using 3D Slicer, please refer to
the `dedicated documentation <https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html>`_.

Requirements
::::::::::::

There are no technical requirements to follow this tutorial because the dataset and software are available on the HIP.

HIP softwares used in this tutorial:

	* :doc:`MRIcroGL</applications/APP_MRIcroGL>` (1.2)
	* :doc:`FSL</applications/APP_FSL>` (6.0.5.2)
	* :doc:`3D Slicer</applications/APP_3D_Slicer>` (4.11)

HIP dataset used in this tutorial:

	* :doc:`Data for electrodes labelling </datasets/DATASET_Data_for_electrodes_labelling>` (rev1.0)
	
.. _prepare_environment_cico:

Prepare the working environment
:::::::::::::::::::::::::::::::

This tutorial relies on data available in the dataset named :doc:`Data for electrodes labelling </datasets/DATASET_Data_for_electrodes_labelling>`, 
and the following folder has to be copied in your Private Space (this is demonstrated in the video tutorial):

	* /Data_for_electrodes_labelling/Case1


This tutorial requires to use several softwares, all available on the HIP, and it is advised to initiate a new Desktop.
Please, refer to the :doc:`How to use Desktops and run applications from the App Catalog </guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>` guide if you need help with this step.

.. _place_SEEG_cico:

Place SEEG electrodes with 3D Slicer
::::::::::::::::::::::::::::::::::::

.. include:: ../hip_data_persistence.rst

The accurate placement of SEEG electrodes requires some knowledge and a good understanding of the implantation procedure
(an implantation scheme or equivalent) and of the type of material that has been implanted (SEEG electrode type/characteristics)
and some expertise in brain anatomy. 
It is also important to work on a high-resolution CT scan or T1 MRI scan acquired after the implantation of the depth electrodes so that
the recording contacts appear either in hypersignal or in hyposignal.

This video tutorial (19'30'') relies on data publicly available on the HIP and
desribes the different steps to label (non-rigid) SEEG electrodes, from the preparation of the imaging data using MRIcroGL and FSL, to the 
placement and exportation of SEEG contacts using 3D Slicer.

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20Epileptogenicity%20map%20computation%20with%203D%20Slicer/Videos/HIP%20Tutorial%20-%20Thumbnail%20-%20EEG%20electrode%20placement%20with%203D%20Slicer.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20Epileptogenicity%20map%20computation%20with%203D%20Slicer/Videos/HIP%20Tutorial%20-%20EEG%20electrode%20placement%20with%203D%20Slicer.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>

|
