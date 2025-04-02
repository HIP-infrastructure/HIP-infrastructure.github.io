.. include:: ../hip_header_msg.rst

How to prepare and upload data to the HIP
******************************************

.. figure:: /guides/art/GUIDE_How_to_prepare_and_upload_data_to_the_HIP/GUIDE_upload_hip.png
	:width: 600px
	:align: center

	**Upload data to the HIP.** *Upload data directly from the web browser or using the Nextcloud client.*
	
A Data Transfer Agreement (DTA) has to be signed between the participating institution and the CHUV prior to any data transfer taking place.

Data can only be uploaded in the Private Space of the HIP user doing the transfer. The Private Space enables the HIP user to curate the data to make
them eligible for collaboration.
Transferring data to the Collaborative or Public Spaces requires to adhere to the specifics of those spaces which are detailed in the
:doc:`how to use the HIP spaces and share data with other users </guides/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users>` guide.
It is not possible to upload or download data directly to or from the Collaborative or Public Spaces.


.. admonition:: Data stored on the HIP

   The HIP iEEG data is organized according to the FAIR principles within the ethics and regulatory frameworks that apply to medical personal data.
   User and application data on the HIP are primarily stored as files and folders either
   in the Private, Collaborative and Public Spaces.
   Please refer to the :doc:`associated guide </guides/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users>` for more information regarding the HIP spaces.



Before uploading data to the HIP
=================================

The HIP is an open-source European platform dedicated to Human intracerebral EEG data and
only iEEG data and relevant health-related or research-related data should be uploaded to the platform.

This includes but is not limited to:

	* iEEG raw data, as well as the corresponding neuroimaging raw data used to identify the anatomical location of iEEG electrodes,
	  all collected during clinical activities.
	* Health-related data collected during clinical activities such as patients’ characteristics (e.g. age, gender, MRI findings, localization of the epileptogenic zone)
	  and anatomical localization of iEEG recording leads.	 
	* Research-related data specifically collected for a research purpose during iEEG (e.g. the  :doc:`COGEPISTIM dataset </datasets/DATASET_Cogepistim>`),
	  and typically informing on the behavioral performance of patients during the research protocol 
	  (e.g. seizure recording, functional electrical stimulation, neuroanatomical imaging, cognitive research tasks or response time).

Data types and formats are not monitored or controlled, primarily due to the security principles of the HIP.
Do not upload non-iEEG related data as it goes against HIP policy and such actions might be referred.

.. admonition:: International HIP Registry
   
   All HIP data are included in the international HIP Registry coordinated by the CHUV Project Leader and Management Team,
   providing a sustained regulatory framework for collecting and storing these data. 

.. _data_controller_responsabilities:

The Data Controller responsibilities
-------------------------------------

The HIP user uploading data from patients onto the HIP is affiliated with at least one of the :ref:`HIP groups <list_identified_hip_groups>`
and will qualify as Data Controller for the corresponding data.

It is the Data Controller responsibility to secure proper data anonymization.
Data has to be pseudonymised/anonymised prior to being stored on the HIP platform depending on the DTA.

Data will be uploaded in the Data Controller’s Private Space, where they cannot be shared with HIP users from other iEEG centers,
yet can be processed with all available HIP functionalities. 


File formats
------------

The HIP primarily relies on BIDS as a common format and database and it is strongly recommended to upload data following BIDS guidelines.
For more information regarding the BIDS standard, please refer to the :ref:`Brain Imaging Data Structure section <BIDS_introduction>` of the
:doc:`How to convert data to BIDS format </guides/GUIDE_How_to_convert_data_to_BIDS_format>` guide.

Uploaded data can be processed with all available HIP functionalities but not be shared in the Collaborative of Public Space
unless they adhere to the specifics of those spaces which include BIDS validation.

The HIP provides a fully integrated tool called :ref:`BIDS importer <BIDS_importer>` which can be used to import the uploaded data
into a (new) BIDS database, taking care of data pseudonymization, normalization of formats, samplings, coordinates and other relevant metadata.
Note that the BIDS importer can only convert a limited number of :ref:`input formats <BIDS_importer_formats>` and covers a subset of
:ref:`BIDS data types <BIDS_importer_dtypes>`.

.. _uploading_data:

Uploading data to the HIP
==========================

There are currently 2 solutions for uploading data to the HIP: either directly from the web browser or using the Nextcloud client.
It is advised to use the Nextcloud client as it uses WebDAV protocol, a more robust way to upload large/numerous files.

Using the web browser
----------------------

It is possible to upload data by simply selecting the files and folders to transfer and drag and drop
them into the web browser while the Private Space web page is opened. Alternatively, it is possible to use the dedicated *Upload file* 
button on the said web page to upload data. Both solutions are illustrated in the video clips below:


.. raw:: html

   <center>	
   <video width="340" controls loop autoplay muted>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Upload%20data/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Upload_clip_dragndrop.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   <video width="340" controls loop autoplay muted>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Upload%20data/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Upload_clip_select.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|

Note that closing the web browser before the uploading/downloading process is over will abort the operation and the transfer
will not resume where it stopped.

.. _upload_nextcloud:

Using the Nextcloud client
--------------------------

The Nextcloud client uses the WebDAV protocol to seamlessly synchronize data between the HIP user's Private Space and the local desktop where 
the client is installed.

The following video guide (2'27'') shows how to download, install and configure the Nextcloud client to set up a synchronized folder:  

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Upload%20data/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Upload%20data.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Upload%20data/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Upload%20data.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|



