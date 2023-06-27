.. include:: ../hip_header_msg.rst

How to transfer data from Micromed software to the HIP
*******************************************************

It is possible to seamlessly synchronize a database created with Micromed software (*SystemPLUS EVOLUTION* software)
so it is available in the HIP user's Private Space. This requires to set up a synchronized folder using the Nextcloud client as explained
in the :ref:`How to prepare and upload data to the HIP <upload_nextcloud>` guide and then create the database in said folder.   

Once the Nextcloud synchronized folder is ready, take the following steps:

.. figure:: /guides/art/GUIDE_How_to_transfer_data_from_Micromed_software_to_the_HIP/GUIDE_mircromed_create_db.png
	:width: 400px
	:align: center

	**1. Create a new database.** *In the SystemPLUS EVOLUTION software, go to your System View and create a new Database.
	the name of the database must be "HIP-Micromed" and the path to the database should be inside the Nextcloud synchronized folder.*

.. figure:: /guides/art/GUIDE_How_to_transfer_data_from_Micromed_software_to_the_HIP/GUIDE_mircromed_password.png
	:width: 300px
	:align: center

	**2. Specify the password.** *The password has to be "micromed" in order to initialize the database.*
	
.. figure:: /guides/art/GUIDE_How_to_transfer_data_from_Micromed_software_to_the_HIP/GUIDE_mircromed_sysplus.png
	:width: 600px
	:align: center

	**3. Check the new database.** *Your new database is created and should be visible in the SystemPLUS EVOLUTION software.*

.. figure:: /guides/art/GUIDE_How_to_transfer_data_from_Micromed_software_to_the_HIP/GUIDE_mircromed_nextcloud.png
	:width: 400px
	:align: center

	**4. Check the synchronization.** *Check in Nextcloud settings that the newly created "HIP-Micromed" database appears in the synchronized folder.*

.. figure:: /guides/art/GUIDE_How_to_transfer_data_from_Micromed_software_to_the_HIP/GUIDE_mircromed_uploaded.png
	:width: 300px
	:align: center

	**5. Transfer data to the HIP.** *Any data imported into the "HIP-Micromed" database using the SystemPLUS EVOLUTION software
	are now accessible in the HIP user's Private Space.*
