.. include:: ../hip_header_msg.rst

CCEP computation with Brainstorm
**********************************

.. figure:: /tutorials/art/TUTORIAL_CCEP_computation_with_brainstorm/tutorial_ccep_header.png
	:width: 600px
	:align: center

	**Visualization of CCEPs.** *The average response of a stimulation train was extracted from SEEG data using* :doc:`Brainstorm</applications/APP_Brainstorm>` *.*

Disclaimer
==========

The methods and software used in this tutorial have not been certified for clinical practice and should be considered for 
research purposes only.  

About this tutorial
====================

Electrical stimulation applied (sub)cortically can elicit CCEPs, recorded remotely from the stimulation site.
The objective of this tutorial is to guide HIP users in computing the average response of a stimulation train extracted from a SEEG file using Brainstorm.
It primarily consists of a video demonstration and should be viewed as an introductory tutorial because it does not go into all the intricacies of
the processing steps used to compute CCEPs. 

For more in-depth information regarding some of the processing steps illustrated in the video,
please refer to the following official tutorials:

	* `Brainstorm's "Bad channels" tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/BadChannels>`_
	* `Brainstorm's "Montage editor" tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/MontageEditor>`_
	* `Brainstorm's "Artifact detection" tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/ArtifactsDetect>`_
	* `Brainstorm's "Power spectrum and frequency filters" tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/ArtifactsFilter>`_	
	* `Brainstorm's "Average response" tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/Averaging>`_


Requirements
=============

There are no technical requirements to follow this tutorial because the dataset and software are available on the HIP.

HIP software used in this tutorial:

	* :doc:`Brainstorm</applications/APP_Brainstorm>` (07-Jan-2022)

HIP dataset used in this tutorial:

	* "CCEP tutorial dataset" located in the shared :ref:`tutorial_data <tutorial_data>` folder.
	
Prepare the working environment
==================================

This tutorial relies on data available in the "CCEP tutorial dataset" located in the read-only shared folder called :ref:`tutorial_data <tutorial_data>`,
and the following file has to be copied in your Private Space (this is demonstrated in the video tutorial):

	* sub-anon_task-stimulation_run-01.edf

This tutorial requires to use Brainstorm, which is available on the HIP, and it is advised to initiate a new Desktop.
Please, refer to the :doc:`How to use Desktops and run applications from the App Catalog </guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>` guide if you need help with this step.
		
Compute cortico-cortical evoked potentials
===========================================

.. include:: ../hip_data_persistence.rst

There are different ways to compute CCEPs depending on your data and the analyzes you want to perform.
The processing steps used in this tutorial are derived from a pipeline developed during `The Functional Brain Tractography Project <https://f-tract.eu/>`_ 
(see [Trebaul_2018c]_ for full scientific details) which has been simplified for demonstration purposes. Notably, this tutorial shows how to: (1) import raw SEEG data into Brainstorm; (2) extract a stimulation train; (3) mark bad channels;
(4) detect the stimulation artifacts (individual pulses); (5) apply bipolar montage; (6) remove stimulation artifacts; (7) apply a band-pass filter; (8) compute the average response
across all pulses.
Depending on your objective, some of these steps might not be relevant/necessary or might be executed in a different order. 

This video tutorial (14'04'') relies on data publicly available on the HIP and
describes the different steps to compute CCEPs using Brainstorm:

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20CCEP%20computation%20with%20Brainstorm/Videos/HIP%20Tutorial%20-%20Thumbnail%20-%20CCEP%20computation%20with%20Brainstorm.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20CCEP%20computation%20with%20Brainstorm/Videos/HIP%20Tutorial%20-%20CCEP%20computation%20with%20Brainstorm.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|

References
==========

.. [Trebaul_2018c] Trebaul, L., Deman, P., Tuyisenge, V., Jedynak, M., Hugues, E., Rudrauf, D., Bhattacharjee, M., Tadel, F., Chanteloup-Forêt, B., Saubat, C., Reyes Mejia, G.C., Adam, C., Nica, A., Pail, M., Dubeau, F., Rheims, S., Trébuchon, A., Wang, H., Liu, S., Blauwblomme, T., Garces, M., De Palma, L., Valentín, A., Metsahonkala, E.-L., Petrescu, A.M., Landré, E., Szurhaj, W., Hirsch, E., Valton, L., Rocamora, R., Schulze-Bonhage, A., Mîndruţă, I., Francione, S., Maillard, L., Taussig, D., Kahane, P., David, O., 2018. Probabilistic functional tractography of the human cortex revisited. NeuroImage 181, 414–429. doi:10.1016/j.neuroimage.2018.07.039.


