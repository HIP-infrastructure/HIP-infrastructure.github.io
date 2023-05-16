3D Slicer
***********

3D Slicer is a free, open source and multi-platform software package widely used for medical, biomedical,
and related imaging research ([Fedorov_2012]_).

Official resources
===================

	
	* `3D Slicer website <https://www.slicer.org/>`_ 
	* `3D Slicer documentation <https://slicer.readthedocs.io/en/latest/>`_ 
	* `3D Slicer tutorials <https://www.slicer.org/wiki/Documentation/4.10/Training>`_ 
	* `3D Slicer wiki <https://www.slicer.org/wiki/Main_Page>`_ 
	* `3D Slicer download <https://download.slicer.org/>`_ 
	* `3D Slicer GitHub <https://github.com/Slicer/Slicer>`_
	
Configure 3D Slicer on the HIP in order to use modules and extensions
======================================================================

.. important::

   These configuration steps only need to be performed once. 

This section explains how to configure 3D Slicer so extra modules and extensions from the "Extensions Manager" can be installed.


Start 3D Slicer in a new :doc:`Desktop</guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>` and take the following steps:

.. figure:: /applications/art/APP_3D_Slicer/APP_3DSLICER_settings.png
	:width: 600px
	:align: center

	**1. Open 3D Slicer settings.** In the menu bar, select "Edit" > "Application Settings".
	
.. figure:: /applications/art/APP_3D_Slicer/APP_3DSLICER_modules.png
	:width: 600px
	:align: center

	**2. Add a new module path.** In the "Settings" side menu, select "Modules" and click on the "Add" button under the "Paths" section. This will open a file browser.

.. figure:: /applications/art/APP_3D_Slicer/APP_3DSLICER_browse.png
	:width: 400px
	:align: center

	**3. Select your nextcloud folder.** In the file browser, browse to your /home/<HIP_USER> directory where <HIP_USER> is your HIP username and select the "nextcloud" folder before clicking on the "Choose" button.
	The file browser will close itself.
	
.. figure:: /applications/art/APP_3D_Slicer/APP_3DSLICER_validate.png
	:width: 600px
	:align: center

	**4. Save modifications.** The path to your nextcloud folder should now appear in the panel titled "Additional module paths". 
	At the bottom of the "Settings" window, click on the "OK" button to save your modifications.
	
.. figure:: /applications/art/APP_3D_Slicer/APP_3DSLICER_restart.png
	:width: 300px
	:align: center

	**5. Restart 3D Slicer.** A pop-up window will ask you to restart 3D Slicer. Click "Yes".
	
3D Slicer will automatically close itself but will not restart. Please wait for the application to be fully shutdown and restart it manually.

You are now ready to install and use extensions from 3D Slicer "Extensions Manager":


.. figure:: /applications/art/APP_3D_Slicer/APP_3DSLICER_extmanager.png
	:width: 700px
	:align: center

	**6. Open 3D Slicer Extensions Manager.** In the menu bar, select "View" > "Extensions Manager".


.. figure:: /applications/art/APP_3D_Slicer/APP_3DSLICER_exinstall.png
	:width: 600px
	:align: center

	**7. Install extensions.** The middle tab "Install Extensions" lets you browse and install new extensions from an online catalog.
	Seamlessly install the desired extensions by clicking on the associated "INSTALL" button.
	You will have to restart 3D Slicer after installing new extensions as prompted in the interface. Remember that 3D Slicer will automatically close itself but needs to be restarted manually.
	The left tab "Manage Extensions (X)" where X is the number of installed extensions, lets you disable and/or uninstall any previously installed extensions.	


References
===========

.. [Fedorov_2012] Fedorov A, Beichel R, Kalpathy-Cramer J, Finet J, Fillion-Robin J-C, Pujol S, Bauer C, Jennings D, Fennessy FM, Sonka M, Buatti J, Aylward SR, Miller JV, Pieper S, Kikinis R. 3D Slicer as an Image Computing Platform for the Quantitative Imaging Network. Magnetic Resonance Imaging., 2012, 30(9):1323-41.
